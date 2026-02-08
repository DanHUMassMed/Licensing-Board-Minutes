# This module targets the October 23, 2025 hearing section and adds
# the Zip Code restricted licenses to the hearing section.

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2025_10_23(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2025-10-23" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)
        # Append the Zip Code restricted licenses to the hearing section
        hearing_section += APPENDED_HEARING_SECTION
        store.set(const.HEARING_SECTION, hearing_section)

APPENDED_HEARING_SECTION = """ 

101. Shunny Day LLC 
Doing business as: Mondo 
563 Columbus Ave. 
Boston, MA 02118 
License #:  LB-601426 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: July 29, 2025 
Manager: Spenser Payne 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 
 
102. El Barrio MX, LLC 
Doing business as: El Barrio Mexican Grill 
809-811 Harrison Ave. 
Boston, MA 02118 
License #:  LB-601427
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: July 29, 2025 
Manager: Joandry J. Vasquez 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License

103. J.J. & R., LLC  
Doing business as: The Mix Vault 
720A-720 Shawmut Ave. 
Roxbury, MA 02119 
License #:  LB-601428
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: July 29, 2025 
Manager: Rufus J Faulk 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 
 
104. Altamira Banquets, LLC 
Doing business as: Mi Pueblito Orient Heights 
964 Saratoga St. 
East Boston, MA 02128 
License #:  LB-584086 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 15, 2025 
Manager: Altamira Carpio 
Closing Time: 11:00 PM 
Active - The Board will hold this application in an active status for two years 
 
105. Gigu, LLC 
Doing business as: Cafe Gigu 
102 Meridian St. 
East Boston, MA 02128 
License #:  LB-584070 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 15, 2025 
Manager: Paula A. Osorio 
Closing Time: 1:00 AM 
Active - The Board will hold this application in an active status for two years 
 
106. La Abundancia Bakery Corporation 
Doing business as: La Abundancia Restaurant
59 Meridian St. 
East Boston, MA 02128 
License #:  LB-584345
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 22, 2025 
Manager: Nuri E. Garcia Montano 
Closing Time: 12:30 AM 
Active - The Board will hold this application in an active status for two years

107. Los Arrieros Restaurant, Inc. 
Doing business as: Los Arrieros Restaurant 
13 Meridian St. 
East Boston, MA 02128
License #:  LB-588316 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: February 26, 2025 
Manager: Felix Ospina 
Closing Time: 2:00 AM 
Active - The Board will hold this application in an active status for two years 
 
108. Italian Express, LLC 
Doing business as: Italian Express 
336 Sumner St. 
East Boston, MA 02128 
License #:  LB-593698 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: April 30, 2025 
Manager: James Iannuzzi 
Closing Time: 1:00 AM 
Active - The Board will hold this application in an active status for two years 

109. GR Restaurant and Catering Inc. 
Doing business as: Bono Restaurant and Catering 
269-271 Meridian St. 
East Boston, MA 02128 
License #:  LB-598009
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: June 25, 2025 
Manager: Manuel Fernando Rosas Guerrero 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Neighborhood Restricted License pursuant to Chapter 287 of the Acts of 2014 

110. 355 Bennington Holdings, LLC 
355 Bennington St. 
East Boston, MA 02128 
License #:  LB-599562
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: July 16, 2025 
Manager: Kyle Warwick 
Closing Time: 2:00 AM 
Active - The Board will hold this application in an active status for two years

"""