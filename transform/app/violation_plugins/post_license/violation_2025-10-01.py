# This module targets the September 17, 2020 hearing section and fixes
# the company name by removing the quotes around it.

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2025_10_01(Plugin):
    priority = 10

    def query(self, store):
        print("="*40)
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2025-10-01" in pdf_file_path:
            return True
        return False

    def run(self, store):
        entity = "voting_minutes_2025-10-01.pdf_3"
        license_text_data = store.get(const.LICENSE_TEXT_DATA)
    
        if entity in license_text_data:
            fixed = license_text_data[entity]
            fixed +="\nDeferred - Board will hold a second hearing to consider this application after the applicant hosts another community meeting"
            license_text_data[entity] = fixed
