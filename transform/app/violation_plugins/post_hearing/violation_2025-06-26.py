# This module targets the June 26, 2025 hearing section and replaces
# the hearing section with the hardcoded replacement.
# There where to many changes to parse

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2025_06_26(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2025-06-26" in pdf_file_path:
            return True
        return False

    def run(self, store):
        # Just replace the entire hearing section with the hardcoded replacement
        # To many changes to parse
        store.set(const.HEARING_SECTION, REPLACE_HEARING_SECTION)

REPLACE_HEARING_SECTION = """ 
Transactional Hearing on Wednesday, June 25, 2025  

1. Van Leeuwen 400 Newbury Street, LLC 
Doing business as: Van Leeuwen Ice Cream 
1001 Boylston St, Boston, MA 02215 
License #:  LB-597503 
Has applied for a Common Victualler License to be exercised on the above -Premise located 400 
Newbury Street (Suite 200) AKA 1001 Boylston Street Boston MA 02115.788SF ground-level ice 
cream shop consisting of a customer area, service counter, one public restroom, and a back room for 
storage and ware washing (no seating). 
Manager:  Grant Jones 
Hours of Operation:  11:00 AM to 11:00 PM 
Granted, with a closing hour of 12:00 AM 
 
2. Van Leeuwen 86 Van Ness Fenway BOS, LLC 
Doing business as: Van Leeuwen Ice Cream 
90 Van Ness St, Boston, MA 02215 
License #:  LB-598405 
Has applied for a Common Victualler License to be exercised on the above - Premise A.K.A 
(13211341 Boylston Street) 1,143SF Ground-level ice cream shop consisting of a dining area (13 
seats), service counter, one public restroom, and a back room for storage and ware washing. 
Manager:  Grant Jones 
Hours of Operation:  11:00 AM to 11:00 PM 
Granted, with a closing hour of 12:00 AM

3. Medford Coffee, LLC 
Doing business as: Dunkin 
39 First Ave, Charlestown, MA 02129 
License #:  LB-575004 
Has applied for a Common Victualler License to be exercised on the above -1,046SF Commercial space 
in a mixed-use building located at 100 First Avenue, Building #34, Charlestown, MA (A.K.A 34 First 
Avenue). The ground floor includes a seating area for 22, with kitchen and storage in the rear. Seasonal 
public patio (AprilNovember) with seating for 16, operating during the same hours as the restaurant. 
Manager: Geo Barbosa  
Hours of Operation: 5:00 AM - 7:00 PM  
Granted 
 
4. Limerick Co., Inc. of Dorchester 
Doing business as: Blend 
1310 Dorchester Ave, Dorchester, MA 02122 
License #:  LB-99035 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned to change the 
manager of the licensed business  From: Caron ONeil To: James J. Clements. 
Attorney:  Margo Gillis 
Granted 
 
5. Mortons of Chicago/Boston Seaport, LLC 
Doing business as: Mortons Steakhouse 
2 Seaport Ln, Boston, MA 02210 
License #:  LB-99445 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned to change the 
manager of the licensed business  From: Mark R. Mahoney To: Lewis Langer. 
Attorney:  Joseph H. Devlin 
Granted 
 
6. Diamondrock Boston Tenant, LLC 
Doing business as: Hilton Boston Downtown/Faneuil Hall 
89 Broad St, Boston, MA 02110 
License #:  LB-101650 
Holder of an Innholder All-Alcoholic Beverages License has petitioned for a change of 
Officers/Directors/LLC Managers. Secondly, has petitioned to change the DBA of the licensed business 
- From: Hilton Boston Downtown/Faneuil Hall To: The Dagny. 
Granted

7. Diamondrock Boston Tenant, LLC 
Doing business as: Westin Boston Waterfront 
425 Summer St, Boston, MA 02210 
License #:  LB-101660 
Holder of an Innholder All-Alcoholic Beverages License has petitioned for a change of 
Officers/Directors/LLC Managers. 
Granted 
 
8. American Multi-Cinema, Inc. 
Doing business as: AMC Theatres Boston Common 19 
175 Temont St, Boston, MA 02111 
License #:  LB-99166 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned for a change of 
Officers/Directors. 
Granted 
 
9. American Multi-Cinema, Inc. 
Doing business as: AMC Theatres 
100 Legends Way, Boston, MA 02114 
License #:  LB-99352 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned for a change of 
Officers/Directors. 
Granted 
 
10. American Multi-Cinema, Inc. 
Doing business as: AMC 
25 District Ave, Dorchester, MA 02125 
License #:  LB-349572 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned for a change of 
Officers/Directors. 
Granted

11. 429 Broadway, LLC 
429 W Broadway, South Boston, MA 02127 
License #:  LB-99242 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned to Pledge the 
License to: Cambridge Savings Bank. 
Granted 
 
12. Alamo Seaport, LLC 
Doing business as: Alamo Drafthouse Cinema  
60 Seaport Blvd, Boston, MA 02210 
License #:  LB-99216 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned for a change in 
Ownership Interest. Secondly, has petitioned for a change of Officers/Directors/LLC Managers. Lastly, 
has petitioned to change the manager of the licensed business  From: Hannah Statton To: Vanessa 
Morales. 
Attorney:  Dennis A. Quilty 
Granted 
 
13. Tejeda Brothers Investment, LLC 
Doing business as: Miami Restaurant  
381 Centre St, Jamaica Plain, MA 02130 
License #:  LB-99632 
Holder of a Common Victualler 7 Day Wines and Malt Beverages License has petitioned to amend the 
description of the licensed business - From: In one room on first floor, kitchen & storage in the rear. To: 
3,638sf Total: 2,210sf in one main room on the first floor, kitchen and storage in the rear. 1,428sf 
additional storage in basement. Dining room seating for 40 and bar seating for 8. One main 
entrance/exit on Centre St., two additional emergency exits in rear of premises. Secondly, has petitioned 
to remove the following condition from the license: No Bar - Alcohol with food only. 
Attorney:  Kristen L. Scanlon 
Granted

14. Purple Shell Restaurant, Inc. 
Doing business as: Purple Shell Bar & Kitchen 
11 W Broadway, South Boston, MA 02127 
License #:  LB-98981 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned to transfer the 
license from the above - To: Canelos Taco and Tequila, Inc. dba Agavero, Guac & Margs (at the same 
location). Sergio Barragan Pelayo, Manager. Closing hour 2:00 AM. Secondly, has petitioned to amend 
the description of the licensed business - From: One room on the first floor, main entrance/exit on West 
Broadway, secondary entrance/exit on Dorchester Avenue, kitchen and storage area in the rear. To: 
3,941 SF restaurant on the first floor with 1 entrance/2 exits. There is a large dining room, bar with 
seating for 15, kitchen, office, 2 bathrooms, and storage area. 
Attorney:  Brian E. Burke 
Granted, with a closing hour of 1:00 AM 
 
15. Nusret Boston, LLC 
Doing business as: Nusret Steakhouse  
100 Arlington St, Boston, MA 02116 
License #:  LB-101570 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned to transfer the 
license and the location - From: Nusret Boston, LLC located at 100 Arlington St, Boston, MA 02116. 
To: First Watch Restaurants, Inc. dba First Watch #1180 located at 777 Boylston St, Boston, MA 02116. 
Premise consists of - 3,109 SQ. FT. interior restaurant space on 1st floor with 2 entrances and 3 exits; to include dining area with seating for approximately 108 and 10  bar/counter seats,
Attorney:  Elizabeth DeConti 
Granted

16. Thornton Companies, Inc. 
Doing business as: Thorntons Fenway Grille 
100 Peterborough St, Boston, MA 02215 
License #:  LB-99244 
Holder of a Common Victualler 7 Day All-Alcoholic Beverages License has petitioned to transfer the 
license and the location - From: Thornton Companies, Inc. located at 100 Peterborough St, Boston, MA 
02215 To: International Place Location, LLC dba Aries Club located at 1-2 International Place, Boston, 
MA 02110
Attorney:  Dennis A. Quilty 
Granted 
 
19. GR Restaurant and Catering Inc. 
Doing business as: Bono Restaurant and Catering  
269-271 Meridian St, East Boston, MA 02128 
License #:  LB-598009 
Has applied for a Common Victualler 7 Day All-Alcoholic Beverages License to be exercised on the 
above - Approximately 1,012 sq ft on first floor and basement of mixed-use building with counter 
seating for 10 patrons, and dining area seating for 18 patrons. Preparation and serving area at the front 
of the space, with bathrooms in the rear, and storage in the basement. The space contains 1 entrance and 
1 exit. 
Manager:  Manuel Fernando Rosas Guerrero 
Closing Time:  1:00 AM 
Deferred 
 
21. Coffee Coffee, LLC 
Doing business as: Gracenote Coffee Boston  
108 Lincoln St, Boston, MA 02111 
License #:  LB-597998 
Has applied for a Common Victualler 7 Day All-Alcoholic Beverages License to be exercised on the 
above -1562 SF coffee shop with accompanying "listening room" on 1 floor with 1 entrance and 2 exits. 
Space includes 2 rooms: the first being a coffee shop/espresso bar; the second being a larger "listening 
room" space with modular furniture/ open floor plan to experience music, film, or other programming. 
Public washroom accessible from the listening room. Office, utility and storage rooms in the rear/staff 
use only. 
Manager:  Patrick Barter 
Closing Time:  12:00 AM 
Deferred 
 
22. Cilantro Latin Kitchen Corp. 
Doing business as: Merengue Express 
1415 Tremont St, Mission Hill, MA 02120 
License #:  LB-598021 
Has applied for a Common Victualler 7 Day All-Alcoholic Beverages License to be exercised on the 
above - Approximately 1,794 square feet on the ground floor of a retail building containing an office 
lounge area , dining room, kitchen in the rear and two restrooms. Premise has one (1) entrance and one 
(1) exit. 
Manager:  Nivia Pina 
Closing Time:  10:00 PM 
Attorney:  Michael Vigorito 
Deferred

======================
 
31. FAS, LLC 
Doing business as: Mesob Restaurant 
1746-1752 Washington St 
Boston, MA 02118
License #: LB-595045 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: May 14, 2025 
Manager: Ariam Berhame 
Closing Time: 1:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License 

32. 490 Harrison Restaurant, LLC 
Doing business as: Capri 
480-490 Harrison Ave 
Boston, MA 02118
License #: LB-595024
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: May 28, 2025 
Manager: William Clark 
Closing Time: 2:00 AM 
Granted - A Restricted All Alcoholic Beverage License pursuant to Chapter 383 of the Acts of 2006

33. Wash El Beverages, LLC 
1395-1405 Washington St 
Roxbury, MA 02118
License #: LB-596687
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: June 4, 2025 
Manager: Peter Georgantas 
Closing Time: 2:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License

34. The Weston Way LLC 
300 Warren St. 
Roxbury, MA 02119
License #: LB-592818
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: April 16, 2025 
Manager: Clayton Weston 
Closing Time: 2:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License 

35. KKR Holdings, LLC 
Doing business as: District 7 Cafe 
376 Warren St. 
Roxbury, MA 02119
License #: LB-595032 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: May 14, 2025 
Manager: Royal Smith 
Closing Time: 2:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License 
 
36. Cool Shade Jamaican Restaurant, LLC 
Doing business as: Cool Shade Jamaican Restaurant 
388 Blue Hill Ave. 
Dorchester, MA 02121
License #: LB-592810 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: April 16, 2025 
Manager: Andre Williams 
Closing Time: 11:00 PM 
Granted - A Zip Code restricted All Alcoholic Beverages License

37. M&K Restaurant Group, LLC 
Doing business as: Blasis Kitchen & Bar 
762 Adams St. 
Dorchester, MA 02122
License #: LB-593662 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: April 30, 2025 
Manager: Maria S. Blasi 
Closing Time: 12:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License on the condition 
that the Licensee surrenders the existing Wines and Malt Beverages with Liqueurs License 

38. 1010 Morrissey Corp. 
Doing business as: Milkweed 
1010 William T. Morrissey Blvd. 
Dorchester, MA 02122 
License #: LB-596016
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: May 28, 2025 
Manager: David Cawley 
Closing Time: 12:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License 

39. Pizza 24 Inc. 
Doing business as: Pizza 24 
301 Adams St. 
Dorchester, MA 02122 
License #: LB-597972
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: June 25, 2025 
Manager: Manuel Da Rosa 
Closing Time: 11:00 PM 
Granted - A Zip Code restricted Wines and Malt Beverages License

40. Ravello, LLC 
Doing business as: Molinaris 
789 Adams St. 
Dorchester, MA 02124 
License #: LB-587130
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: February 12, 2025 
Manager: Jeffrey Cincotta 
Closing Time: 11:00 PM 
Granted - A Zip Code restricted All Alcoholic Beverages License 

41. Gourmet Kreyol, LLC 
Doing business as: Doune & Pepe 
657 Washington St. 
Dorchester, MA 02124 
License #: LB-592854 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: April 16, 2025 
Manager: Nathalie Lecorps 
Closing Time: 12:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License 
 
42. DQC, Inc. 
Doing business as: Chilacates Cantina 
1211 Dorchester Ave. 
Dorchester, MA 02125
License #: LB-598023
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: June 25, 2025 
Manager: Aleska Ramirez 
Closing Time: 1:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License

43. AAA Restaurant, LLC 
Doing business as: AAA Restaurant 
3141 Washington St. 
Jamaica Plain, MA 02130
License #:  LB-592817
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: April 16, 2025 
Manager: Paula Martinez 
Closing Time: 11:00 PM 
Granted - A Zip Code restricted All Alcoholic Beverages License 

44. Mr. Drinky LLC 
Doing business as: Mr. Drinky 
606 Centre St. 
Jamaica Plain, MA 02130
License #: LB-596653
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: June 4, 2025 
Manager: Alan Wong 
Closing Time: 1:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License 

45. Tejeda Brothers Investment LLC 
Doing business as: Miami Restaurant 
381 Centre St. 
Jamaica Plain, MA 02130
License #: LB-598072
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: June 25, 2025 
Manager: Leandro Tejeda 
Closing Time: Monday-Wednesday 11 PM, Thursday-Sunday 1 AM
Attorney:  Kristen L. Scanlon 
Granted - A Zip Code restricted All Alcoholic Beverages License on the condition 
that the Licensee surrenders the existing Wines and Malt Beverages with Liqueurs License

46. ATCF, LLC 
Doing business as: Knoll Street Tavern 
1410 Centre St. 
Roslindale, MA 02131
License #: LB-587892
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: February 26, 2025 
Manager: Andrew Tremble 
Closing Time: 1:00 AM 
Granted - A Zip Code restricted All Alcoholic Beverages License 

47. sweeties, LLC 
Doing business as: sweeties 
48 Corinth St. 
Roslindale, MA 02131
License #: LB-593736
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: April 30, 2025 
Manager: Anika Gramsey
Closing Time: 10:00 PM 
Granted - A Zip Code restricted All Alcoholic Beverages License

48. O'Brien & Armstrong, Inc. 
Doing business as: The Green T Coffee Shop 
873 South St. 
Roslindale, MA 02131 
License #: LB-596679
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: June 4, 2025 
Manager: Braden Armstrong 
Closing Time: 10:00 PM 
Granted - A Zip Code restricted All Alcoholic Beverages License

49. Nawiya, Inc. 
Doing business as: Somtum Modern Thai Cuisine 
1894 Centre St. 
West Roxbury, MA 02132 
License #:  LB-584372
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: January 22, 2025 
Manager: Patrasuda Cooper 
Closing Time: 8:30 PM 
Granted - A Zip Code restricted Wines and Malt Beverages License 

50. Boston Pickle Club, Inc. 
Doing business as: Boston Pickle Club 
91 Sprague St. 
Hyde Park, MA 02136
License #: LB-593664
Has applied for a Common Victualler 7-Day All Wines and Malt Beverages License - Hearing Date: April 30, 2025 
Manager: Steven Hauck 
Closing Time: 10:00 PM 
Granted - A Zip Code restricted Wines and Malt Beverages License 

51. Con Rua, LLC 
Doing business as: Mos Tavern & Kitchen 
571-575 Washington St. 
Brighton, MA 02135
License #: LB-592801
Has applied for a Common Victualler 7-Day All Alcoholic Beverages - License Hearing Date: April 16, 2025 
Manager: Candice Dowling 
Closing Time: 1:00 AM 
Granted - An Oak Square restricted All Alcoholic Beverages License
"""