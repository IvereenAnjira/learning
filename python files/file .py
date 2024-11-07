# Adding the rest of the data provided by the user
import pandas as pd
additional_data = data = [
    {"latitude": 7.62329, "longitude": 5.22087, "location": "AT AROWOLO COMP. / OKE AROWOLO , ODO ADO ADO 'B'  INISA ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF AROWOLO'S HOUSE / OKE AROWOLO ADO 'B'  INISA ADO EKITI EKITI"},
    {"latitude": None, "longitude": None, "location": "ST. MICHEAL PRY. SCH. BK.III / WATER WKS. AREA III ADO 'D' IJIGBO ADO EKITI EKITI"},
    {"latitude": None, "longitude": None, "location": "IN FRONT OF OMOLEYE'S COMP. / OMOLEYE COMP. ADO 'D' IJIGBO ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "ST. MICHEAL PRY. SCH. BK.IV / WATER WKS. AREA IV ADO 'D' IJIGBO ADO EKITI EKITI"},
    {"latitude": None, "longitude": None, "location": "IN FRONT OF AGIRIS HOUSE / AGIRI'S COMP. ADO 'D' IJIGBO ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF OKE AFA COMP. / OKE AFA ADO 'D' IJIGBO ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "OLOWOYO'S HOUSE / OLOWOYO COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "BISHOP FATOYINBO HOUSE / IGBELE ADO 'E'  IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF AYEDUN FAMILY'S HOUSE / OLUKERE ADO 'E'  IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF MR. AJAYI'S HOUSE / IGIRIGIRI AREA ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF AJAYI'S HOUSE / AJAYI'S COMP. ADO 'E'  IGBELE ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "IN FRONT OF MRS. AJAYI'S HOUSE / AJAYI'S COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "IN FRONT OF FATUMBI'S HOUSE / FATUMBI'S COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "IN FRONT OF ODUTAYO'S HOUSE / ODUTAYO'S COMP. ADO 'E'  IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF OGIDAN'S HOUSE / OGIDAN COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF TAYO'S HOUSE / TAYO'S COMP. ADO 'E'  IGBELE ADO EKITI EKITI"},
    {"latitude": 41.66667, "longitude": 2.0, "location": "IN FRONT OF FATOYINBO'S HOUSE / FATOYINBO COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": None, "longitude": None, "location": "IN FRONT OF IGE'S HOUSE / IGE'S COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "IN FRONT OF IGILE FAMILY'S HOUSE / IGILE COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "ST. ANDREW'S PRY. SCH. / OKE OWODE ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 41.66667, "longitude": 2.0, "location": "IN FRONT OF EBIRA'S HOUSE / EBIRA COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF AGILINTI'S HOUSE / AGILINTI COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "IN FRONT OF FASEYI'S HOUSE / FASEYI'S COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF ODOFIN'S HOUSE / ODOFIN COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.85, "longitude": 4.33333, "location": "IN FRONT OF ELEGBA'S HOUSE / ELEGBA COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF FATOYINBO'S HOUSE / FATOYINBO COMP. ADO 'E'  IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF TAYO'S HOUSE / TAYO'S COMP. ADO 'E'  IGBELE ADO EKITI EKITI"},
    {"latitude": 41.66667, "longitude": 2.0, "location": "IN FRONT OF OLUSOGA'S HOUSE / OLUSOGA COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": None, "longitude": None, "location": "IN FRONT OF OMESI'S HOUSE / OMESI COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF AKANJI'S HOUSE / AKANJI COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF AJAYI'S HOUSE / AJAYI COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF MRS. AJAYI'S HOUSE / AJAYI COMP. ADO 'E' IGBELE ADO EKITI EKITI"},
    {"latitude": 7.62329, "longitude": 5.22087, "location": "IN FRONT OF AJAYI'S HOUSE / AJAYI COMP. ADO 'E'  IGBELE ADO EKITI EKITI"}
]

# Merging additional data with the original dataset
data.extend(additional_data)

# Creating a DataFrame from the complete dataset
df = pd.DataFrame(data)

# Saving the DataFrame to an Excel file
output_file = 'EKITI_geocoded.csv'
df.to_csv(output_file, index=False)

output_file