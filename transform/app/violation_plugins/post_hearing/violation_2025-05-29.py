# This module targets the May 29, 2025 hearing section and fixes
# the address for the license application by adding a newline.

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2025_05_29(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2025-05-29" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)

        fixed = hearing_section.replace(
            "16. Democracy 154 Maverick LLC \n \n154 Maverick St, East Boston, MA 02128",
            "16. Democracy 154 Maverick LLC\n\n154 Maverick St, East Boston, MA 02128\nLicense #:  LB-000000",
        )
        store.set(const.HEARING_SECTION, fixed)
