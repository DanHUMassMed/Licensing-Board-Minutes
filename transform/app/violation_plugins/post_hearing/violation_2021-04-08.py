# This module targets the January 4, 2024 hearing section and fixes
# 5 NSQ, LLC that did not have DBA or Licenses data

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2021_04_08(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_yyyy-mm-dd" in pdf_file_path:
            return True
        elif "voting_minutes_2021-04-08" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)
        fixed = hearing_section.replace(
            "5 NSQ, LLC",
            "5 NSQ, LLC\nD/B/A: Ciao Roma\n5 NORTH SQ\nBoston, MA 02113",
        )
        store.set(const.HEARING_SECTION, fixed)
