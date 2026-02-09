# This module targets the January 4, 2024 hearing section and fixes
# 5. Eataly Boston, LLC which has no license number
# IVA Foods, Inc. which has no license number and we dont know what it is
# The Family Restaurant Partners which has no license number and we dont know what it is

from app import constants as const
from app.violation_plugins.base import Plugin

class Violation_2024_01_04(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2024-01-04" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)
        fixed = hearing_section.replace(
            "110 Huntington Ave, Boston, MA 02116",
            "110 Huntington Ave, Boston, MA 02116\nLicense #: LB-101625",
        )
        fixed = fixed.replace(
            "424 Cambridge St, Allston, MA 02134",
            "424 Cambridge St, Allston, MA 02134\nLicense #: LB-000000",
        )
        fixed = fixed.replace(
            "400 Dorchester St, South Boston, MA 02127",
            "400 Dorchester St, South Boston, MA 02127\nLicense #: LB-000000",
        )
        store.set(const.HEARING_SECTION, fixed)
