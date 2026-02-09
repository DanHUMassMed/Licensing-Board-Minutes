# This module targets the October 31, 2024 hearing section and fixes
# Line confused as a header

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2024_10_31(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2024-10-31" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)
        fixed = hearing_section.replace(
            "8. Licensee must have",
            "8 Licensee must have",
        )

        store.set(const.HEARING_SECTION, fixed)
