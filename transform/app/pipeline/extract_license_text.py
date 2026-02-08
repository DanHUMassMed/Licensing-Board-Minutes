import logging
import os
import re
from datetime import datetime

from dateutil import parser

from app import constants as const
from app.pipeline.run_result import RunResult
from app.state.kv_store import KVStore

DEFAULT_DT = datetime(1900, 1, 1)
logger = logging.getLogger(__name__)

# Regex for the start of a license chunk: "1. ", "10. ", etc. at beginning of line
# A new chunk starts when a line begins with a number followed by a . a space and then some text
CHUNK_START_RE = re.compile(r"^\d+\.\s+.+")

# Regex for identifying a license number pattern (case-insensitive, flexible spacing/colon)
# Matches "License#", "license #", "LICENSE : #", etc.
LICENSE_NUMBER_RE = re.compile(r"license\s*:?\s*#\s*:?", re.IGNORECASE)

STATUS_KEYWORDS = [
    "Active",
    "Granted",
    "Deferred",
    "RE-SCHEDULED",
    "RESCHEDULED",
    "Continued",
    "Withdrawn",
    "No Violation",
    "Failed to Appear",
    "Dismissed",
    "No Action Taken",
    "Defer",
    "Dismiss",
    "Revised",
    "Corrected",
    "Rejected",
    "Denied",
]

STOP_MARKERS = tuple(
    k.lower() for k in STATUS_KEYWORDS
)

class LicenseTextExtractorStep:
    """Extracts license text from KVStore PDF text."""

    def __init__(self, kv_store: KVStore):
        self.kv_store = kv_store

    def run(self):
        # logger.info("Starting license extraction process...")
        hearing_section = self.kv_store.get(const.HEARING_SECTION)
        pdf_file_path = self.kv_store.get(const.PDF_FILE_PATH)

        if not hearing_section:
            return RunResult(
                proceed=False, reason="Hearing section not provided in KVStore"
            )
        if not pdf_file_path:
            return RunResult(
                proceed=False, reason="PDF file path not provided in KVStore"
            )
        hearing_section = self._fix_header(hearing_section)

        hearing_section_lines = hearing_section.splitlines()
        licenses_text_data = self._extract_license_text(
            hearing_section_lines, pdf_file_path
        )
        if licenses_text_data:
            self.kv_store.set(const.LICENSE_TEXT_DATA, licenses_text_data)
        else:
            logger.warning(f"No hearings extracted from {pdf_file_path}")

        # logger.info("Text extraction process completed.")
        return RunResult()

    def _get_hearing_date(self, first_line, pdf_file_path):
        if not first_line:
            return "Date:null"

        first_line = first_line.replace(":", "")

        try:
            dt = parser.parse(
                first_line,
                fuzzy=True,
                default=DEFAULT_DT,
            )

            # 🚨 Reject inferred years
            if dt.year == DEFAULT_DT.year:
                raise ValueError("Year was inferred, not explicitly present")

            return f"Date:{dt.strftime('%Y-%m-%d')}"

        except (ValueError, OverflowError):
            logger.warning(
                f"Could not parse date from first line: {first_line!r}"
            )
            pass

        # Fallback: filename
        match = re.search(r"(\d{4}-\d{2}-\d{2})", str(pdf_file_path))
        if match:
            return f"Date:{match.group(1)}"
        else:
            logger.warning(f"Could not parse date from from filename {pdf_file_path}")
        return "Date:null"

    def _fix_header(self, text: str) -> str:
        """
        Fix broken numbered headers by merging lines where a standalone numeric
        header (e.g. "1.", "23.") appears on its own line with the following line.

        For any line that consists only of digits followed by a period, the next
        line is appended to the same line separated by a space. All other lines
        are preserved exactly, and no additional whitespace or formatting changes
        are applied.
        """
        lines = text.splitlines()
        output = []

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Match lines like "1." , "23." etc (digits followed by a dot, and nothing else)
            if re.fullmatch(r"\d+\.", line):
                # If there is a next line, merge them
                if i + 1 < len(lines):
                    merged = f"{lines[i].rstrip()} {lines[i + 1].lstrip()}"
                    output.append(merged)
                    i += 2
                    continue

            # Normal line — keep as-is
            output.append(lines[i])
            i += 1

        return "\n".join(output)


    def _first_non_empty_line(self, lines: list[str]) -> str:
        """
        Returns the first non-empty line from a list of lines.
        """
        for line in lines:
            if line.strip():
                return line.strip()
        return ""


    def _starts_with_keyword(self, line: str) -> bool:
        """
        Return True if the line starts with any known status keyword
        (case-insensitive).
        """
        line_lower = line.strip().lower()
        return line_lower.startswith(STOP_MARKERS)

    def _extract_license_text(self, hearing_section_lines, pdf_file_path):

        chunks = []
        current_chunk = []
        in_license_chunk = False   # ✅ Move outside loop

        basename = os.path.basename(pdf_file_path)

        first_non_empty_line = self._first_non_empty_line(hearing_section_lines)
        hearing_date_line = self._get_hearing_date(
            first_non_empty_line,
            pdf_file_path,
        )

        for line in hearing_section_lines:

            # Start of chunk
            if not in_license_chunk:

                if CHUNK_START_RE.match(line):
                    current_chunk = [line]
                    in_license_chunk = True

            # Inside chunk
            else:
                if self._starts_with_keyword(line):
                    current_chunk.append(line)
                    chunks.append(current_chunk)
                    current_chunk = []
                    in_license_chunk = False
                else:
                    current_chunk.append(line)

        # ✅ Flush last chunk
        if current_chunk:
            chunks.append(current_chunk)

        extracted_chunks = {}

        for idx, chunk_lines in enumerate(chunks, 1):
            chunk_text = "\n".join(chunk_lines)
            if LICENSE_NUMBER_RE.search(chunk_text):
                output_key = f"{basename}_{idx}"
                extracted_chunks[output_key] = (
                    hearing_date_line
                    + "\n"
                    + chunk_text
                )
            else:
                logger.warning(
                    f"Skipping Chunk {idx} in {basename}: {chunk_text}"
                )

        return extracted_chunks

        