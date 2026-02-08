# This module targets the February 13, 2025 hearing section and adds
# the Zip Code restricted licenses to the hearing section.

from app import constants as const
from app.violation_plugins.base import Plugin


class Violation_2025_02_13(Plugin):
    priority = 10

    def query(self, store):
        pdf_file_path = store.get(const.PDF_FILE_PATH)
        if "voting_minutes_2025-02-13" in pdf_file_path:
            return True
        return False

    def run(self, store):
        hearing_section = store.get(const.HEARING_SECTION)
        # Append the Zip Code restricted licenses to the hearing section
        hearing_section += APPENDED_HEARING_SECTION
        store.set(const.HEARING_SECTION, hearing_section)

APPENDED_HEARING_SECTION = """ 
 
100. Crystal Spoons, LLC 
1950 Washington St. 
Roxbury, MA 02118 
License #: LB-580947
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: November 20, 2024
Manager: Srinivas Desaneedi 
Closing Time: 2:00 AM  
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 
 

101. Siraj Corporation
Doing business as: El Centro 
474 Shawmut Ave. 
Roxbury, MA 02118 
License #:  LB-584103 
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 15, 2025
Manager: Rabiul Islam 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License on the 
condition that the Licensee surrenders the existing Wines and Malt Beverages with Liqueurs License


102. Dominican Kitchen, Inc.
Doing business as: La Parada Dominican Kitchen 
3094 Washington St. 
Roxbury, MA 02119 
License #: LB-578141
Has applied for a Common Victualler 7-Day Wines and Malt Beverages with Liqueurs License - Hearing Date: October 30, 2024 
Manager: Yonatan Pena 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages with Liqueurs License 
 
103. Commonwealth Zoological Corporation 
Doing business as: Zoo New England 
1 Franklin Park Rd. 
Boston, MA 02121 
License #: LB-578146
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Andrew Robinson 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Community Space All Alcoholic Beverages License 
 
104. One Family Diner, Inc.
Doing business as: One Family Diner 
260 Bowdoin St.
License #: LB-581512
Dorchester, MA 02122 
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: November 20, 2024 
Manager: Rachel Silveira 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages License

105. Minina Cafe, Inc.
Doing business as: Minina Cafe 
432 Geneva Ave. 
Dorchester, MA 02122 
License #:  LB-584080 
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: January 15, 2025 
Manager: Alejandra Rosa 
Closing Time: 10:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages License 
 

106. Murls Kitchen, LLC 
Doing business as: Murls Kitchen 
10-18 Bowdoin St. 
Dorchester, MA 02124 
License #: LB-000000
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: December 11, 2024 
Manager: Shaniel Walker 
Closing Time: 2:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License  

107. Fresh Food Generation LLC 
Doing business as: Fresh Food Generation 
191 Talbot Ave. 
Dorchester, MA 02124 
License #: LB-583884
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 8, 2025 
Manager: Carla Cassandria Campbell 
Closing Time: 9:00 PM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License

108. Blue Mountain Jamaican Restaurant, LLC 
Doing business as: Blue Mountain Jamaican Restaurant 
1301 Blue Hill Ave. 
Mattapan, MA 02128 
License #: LB-583841
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 8, 2025 
Manager: Marcia Satchell 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 


109. Florenza, Inc.  
Doing business as: Florenza 
164-170 Sumner St. 
East Boston, MA 02128 
License #: LB-574154
Has applied for a Common Victualler 7-Day Wines and Malt Beverages with Liqueurs License - Hearing Date: September 25, 2024 
Manager: Stefano Bruno 
Closing Time: 10:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages with Liqueurs License 
 

110. Con Sabor A Colombia, Inc. 
244 Meridian St. 
East Boston, MA 02128 
License #: LB-577182
Has applied for a Common Victualler 7-Day Wines and Malt Beverages with Liqueurs License - Hearing Date: October 16, 2024 
Manager: Jose Dario Gomez 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages with Liqueurs License 
 

111. Eastie Caffe Dello Sport, Inc. 
Doing business as: Caffe Dello Sport Eastie 
973 Saratoga St. 
East Boston, MA 02128 
License #: LB-578142
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Mivan Spencer 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 
 

112. Angelas Cafe II, Inc. 
Doing business as: Angelas Cafe 
1012 Bennington St. 
East Boston, MA 02128 
License #: LB-578145
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Ixchel Garcia 
Closing Time: 12:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License on the 
condition that the Licensee surrenders the existing Wines and Malt Beverages with Liqueurs License 
 

113. Jeffries Yacht Club 
565 Sumner St. 
East Boston, MA 02128 
License #: LB-582291
Has applied for a Club All-Alcoholic Beverages License - Hearing Date: December 11, 2024 
Manager: Brian George 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Community Space All Alcoholic Beverages License 


114. F&H, Inc.  
Doing business as: Mi Pueblito Restaurant 
333 Border St. 
East Boston, MA 02128 
License #: LB-583866
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 8, 2025 
Manager: Ferdy L. Argueta 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License on the 
condition that the Licensee surrenders the existing Wines and Malt Beverages with Liqueurs License 
 

115. CabanaLV, Inc. 
Doing business as: Cabana Grill 
254 Bennington St. 
East Boston, MA 02128 
License #: LB-583877
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 8, 2025
Manager: Pedro Lopez 
Closing Time: 2:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License on the 
condition that the Licensee surrenders the existing Wines and Malt Beverages with Liqueurs License 
 

116. Altamira Banquets, LLC 
Doing business as: Mi Pueblito Orient Heights 
964 Saratoga St. 
East Boston, MA 02128 
License #:  LB-584086
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 15, 2025 
Manager: Altamira Carpio 
Closing Time: 11:00 PM 
Active - The Board will hold this application in an active status for two years  

117. Gigu, LLC 
Doing business as: Cafe Gigu 
102 Meridian St. 
East Boston, MA 02128 
License #:  LB-584070
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 15, 2025 
Manager: Paula A. Osorio 
Closing Time: 1:00 AM 
Active - The Board will hold this application in an active status for two years 
 

118. La Abundancia Bakery Corporation 
Doing business as: La Abundancia Restaurant 
59 Meridian St. 
East Boston, MA 02128 
License#: LB439777
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 22, 2025 
Manager: Nuri E. Garcia Montano 
Closing Time: 12:30 AM 
Active - The Board will hold this application in an active status for two years 
 

119. Cholo Brothers, LLC 
Doing business as: Peruvian Taste Restaurant 
78 Arlington Ave. 
Charlestown, MA 02129 
License #:  LB-584097
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: January 15, 2025 
Manager: Jose Villafranca 
Closing Time: 10:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wine and Malt Beverages License

120. DTDA Enterprises, Inc. 
Doing business as: Don Tequeno y Dona Arepa 
403A Centre St. 
Jamaica Plain, MA 02130 
License #: LB550017
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: January 15, 2025 
Manager: Joel Marte 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages License 
 

121. Stoked Pizza JP, LLC 
Doing business as: Stoked Pizza 
3484 Washington St. 
Jamaica Plain, MA 02130 
License #: LB-578143
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: January 15, 2025 
Manager: Toirm Miller 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 
 
122. Pinales Kitchen, Inc. 
Doing business as: Mangu Dominican Bistro 
264 Hyde Park Ave. 
Jamaica Plain, MA 02130 
License #: LB-580946
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: November 13, 2024
Manager: Ingrid Pinales Avalo 
Closing Time: 9:00 PM 

Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages License

123. Amabaka Corporation 
Doing business as: Momo Masala 
2 Perkins St. 
Jamaica Plain, MA 02130 
License #: LB-582324
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: December 11, 2024 
Manager: Dao Thach 
Closing Time: 10:00 PM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 
 
124. JP BBQ, Inc. 
Doing business as: BB.Q Kitchen 
654 Centre St. 
Jamaica Plain, MA 02130 
License #: LB-583839
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: January 8, 2025 
Manager: Purita Jongchalermchai 
Closing Time: 10:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages License 

125. Mi Finca Mexican Foods, LLC 
Doing business as: Mi Finca Mexican Restaurant and Pizzeria 
4249 Washington St. 
Roslindale, MA 02131 
License #: LB-582370
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: December 11, 2024 
Manager: Oscar Bonilla 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted Wines and Malt Beverages License 
 

126. S & S Restaurant LLC 
Doing business as: Harrys All American 
1410-1420 Centre St. 
Roslindale, MA 02131 
License #: LB-582320
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: December 11, 2024 
Manager: Edneia V. Santiago 
Closing Time: 11:00 PM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License  


127. Little Haiti International Cuisine, LLC 
Doing business as: Little Haiti International Cuisine 
1184 Hyde Park Ave. 
Hyde Park, MA 02136 
License #: LB-577222
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 16, 2024 
Manager: George Craan 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 
 
128. Gelas Corp. 
Doing business as: Las Delicias Colombianas 2 
1231 River St. 
Hyde Park, MA 02136 
License #: LB-578144
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Miguel Angel Gallego 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Zip Code restricted All Alcoholic Beverages License 

129. 567 Washington St, LLC 
Doing business as: SubRosa and Humaari 
567 Washington St. 
Brighton, MA 02135 
License #: LB-577208
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 16, 2024 
Manager: Matthew Pennino 
Closing Time: 1:00 AM 
Granted - The Board voted to approve an Oak Square restricted All Alcoholic Beverages License 
 
130. Kal Yummy Corp 
Doing business as: Cafe Lava and Bento 
290-298 Washington St. 
Brighton, MA 02135 
License #: LB-551991
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: March 5, 2024 
Manager: Kim Thu Nguyen 
Closing Time: 9:00 PM 
Active - The Board will hold this application in an active status for two years 
 
131. Flagship Restaurant Group, LLC 
Doing business as: Forcella 
33 North Square 
Boston, MA 02113 
License #: LB-98922
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: August 7, 2024 
Manager: Shannon MacGowan 
Closing Time: 2:00 AM 
Active - The Board will hold this application in an active status for two years 
 

132. Locale, Inc. 
Doing business as: Locale 
350-352 Hanover St. 
Boston, MA 02113 
License #: LB-574260
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: September 25, 2024 
Manager: Jennifer Matarazzo 
Closing Time: 11:00 PM 
Active - The Board will hold this application in an active status for two years 

133. Hunan Gourmet LLC 
Doing business as: Hunan Gourmet 
45 Beach St. 
Boston, MA 02111 
License #: LB-542519
Has applied for a Common Victualler 7-Day Wines and Malt Beverages License - Hearing Date: September 26, 2024 
Manager: Zhichao Chang 
Closing Time: 10:30 PM 
Active - The Board will hold this application in an active status for two years 
 

134. Huntington Theatre Company, Inc. 
Doing business as: Huntington Theatre 
264 Huntington Ave. 
Boston, MA 02115 
License #: LB-577211
Has applied for a General On-Premise All Alcoholic Beverages License - Hearing Date: October 16, 2024 
Manager: Katherine Herzig 
Closing Time: 1:00 AM 
Granted - The Board voted to approve a Community Space All Alcoholic Beverages License

135. Antico Forno, Inc. 
Doing business as: Antico Forno 
93-95 Salem St. 
Boston, MA 02113 
License #: LB-577217
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 16, 2024 
Manager: Carla Gomes 
Closing Time: 1:00 AM 
Active - The Board will hold this application in an active status for two years 
 

136. Terramia, Inc. 
Doing business as: Terramia 
98 Salem St. 
Boston, MA 02113 
License #: LB-577220
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 16, 2024 
Manager: Carla Gomes 
Closing Time: 11:00 PM 
Active - The Board will hold this application in an active status for two years 
 

137. Seaport Innovation Center Hospitality, LLC 
75 Northern Ave. 
Boston, MA 02210 
License #: LB-580948
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Rebecca Louise Donner 
Closing Time: 2:00 AM 
Active - The Board will hold this application in an active status for two years 
 

138. LMPBTR, LLC 
Doing business as: Silver Dove Afternoon Tea 
18 Tremont St. 
Boston, MA 02108 
License #: LB-580949
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Patrick Brewster 
Closing Time: 10:00 PM 
Active - The Board will hold this application in an active status for two years 
 

139. Pappare, LLC 
Doing business as: Pappare Ristorante 
358-364 Hanover St. 
Boston, MA 02113 
License #: LB-580950
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Frank Pellino 
Closing Time: 12:00 AM 
Active - The Board will hold this application in an active status for two years 
 

140. Il Panino, Inc. 
Doing business as: Il Panino 
11 Parmenter St. 
Boston, MA 02113 
License #: LB-580951
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Frank DePasquale 
Closing Time: 11:00 PM 
Active - The Board will hold this application in an active status for two years 
 

141. SMG Newbury Restaurant, LLC 
Doing business as: Serafina 
235A Newbury St. 
Boston, MA 02116 
License #: LB-580952
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Bryan Sayers 
Closing Time: 1:00 AM 
Active - The Board will hold this application in an active status for two years 


142. Nite Lite Cafe, LLC 
Doing business as: 89 Charles 
89 Charles St. 
Boston, MA 02114 
License #:  LB-99779
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: October 30, 2024 
Manager: Gennaro Riccio 
Closing Time: 12:00 AM 
Active - The Board will hold this application in an active status for two years 


143. 85 Harvard Ave LLC 
Doing business as: Tofu Story 
85 Harvard Ave. 
Allston, MA 02134 
License #: LB-581522
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: November 20, 2024 
Manager: Jin Chong 
Closing Time: 2:00 AM 
Active - The Board will hold this application in an active status for two years

144. 204 Hanover Corp. 
Doing business as: North End Lobster Co. 
204 Hanover St. 
Boston, MA 02113 
License #: LB-581520
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: November 20, 2024 
Manager: Adriana Ioana Travaglione 
Closing Time: 1:00 AM 
Active - The Board will hold this application in an active status for two years 
 

145. W Entertainment Group Inc. 
Doing business as: Viva Karaoke & Studios 
204 Tremont St. 
Boston, MA 02116 
License #: LB-581524
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: November 20, 2024 
Manager: Henry Wong 
Closing Time: 2:00 AM 
Active - The Board will hold this application in an active status for two years 
 

146. JC & Friends, Inc. 
Doing business as: KChickin 
86 Peterborough St. 
Boston, MA 02215 
License #: LB-582328
Has applied for a Common Victualler 7-Day All Alcoholic Beverages License - Hearing Date: December 11, 2024 
Manager: Shirley Wong 
Closing Time: 10:00 PM 
Active - The Board will hold this application in an active status for two years 
"""