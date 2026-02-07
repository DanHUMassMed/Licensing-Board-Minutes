# This module targets the August 28, 2025 hearing section and fixes
# "02111 from being identified as an entity as it is the first digit in the line followed by a .

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2025_08_28(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2025-08-28" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)
        fixed = hearing_section.replace(
            "02111. Kai Yang",
            "02111 Kai Yang",
        )
        store.set(const.HEARING_SECTION, fixed)
