# This module targets the August 1, 2025 hearing section and fixes
# 5. Eataly Boston, LLC which has no license number

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2024_08_01(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2024-08-01" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)
        fixed = hearing_section.replace(
            "800 Boylston St, Boston, MA 02199",
            "800 Boylston St, Boston, MA 02199/nLicense #: LB99355",
        )
        store.set(const.HEARING_SECTION, fixed)
