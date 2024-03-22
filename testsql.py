import pyodbc
import json
from datetime import datetime

server = 'NB-GRS-AS'
database = 'SIGNUM_GRSDEMO_FL'
username = 'GRS'
password = 'SIGNUM'

conn = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# cursor = conn.cursor()
# cursor.execute("select KONTEXT, TYPE, SUBTYPE, FID, ID, PID, TEXT, FTYPE from RSTRU where KONTEXT = 'KRED' and WEBPUBLISH = 1")# KRED RSTRU
# rows1 = cursor.fetchall()

# results1 = []

# for row in rows1:

#     row_dict1 = {
#         "FID" : row[3],
#         "Text" : row[6],
#         "FType" : row[7]
#     }

#     results1.append(row_dict1)

# json_data1 = results1
# ###############################
# cursor.execute("select KONTEXT, TYPE, SUBTYPE, FID, ID, PID, TEXT, FTYPE from RSTRU where KONTEXT = 'ROHKRED' and WEBPUBLISH = 1")# ROHKRED RSTRU
# rows2 = cursor.fetchall()

# results2 = []

# for row in rows2:
#     row_dict2 = {
#         "FID" : row[3],
#         "Text" : row[6],
#         "FType" : row[7],
#         "Value": ""
#     }

#     results2.append(row_dict2)

# json_data2 = results2

# # print(json_data1)
# # print(json_data2)

# jsonData = {
#     "KREDID": 1,
#     "FieldList" : json_data2
# }

# print(jsonData)

# cursor.close

# Cursor erstellen
cursor = conn.cursor()

# TSQL SELECT-Statement
sql_query = "SELECT * FROM KREDDATA WHERE kredid = 1"

# Query ausführen
cursor.execute(sql_query)

# Datensatz abrufen
row = cursor.fetchone()

# Dictionary initialisieren, um die Ergebnisse zu speichern
data = {}

# Überprüfen, ob eine Zeile zurückgegeben wurde
if row:
    # Iteriere über die Spalten und füge sie dem Dictionary hinzu
    for index, column in enumerate(cursor.description):
        column_name = column[0]
        column_value = row[index]
        # Überprüfen, ob der Spaltenwert ein Datetime-Objekt ist und in einen String konvertieren
        if isinstance(column_value, datetime):
            column_value = column_value.strftime('%Y-%m-%d %H:%M:%S')
        data[column_name] = column_value
else:
    print("Keine Datensätze gefunden.")

# JSON-Objekt initialisieren
json_data = []

# Iteriere über die Schlüssel-Wert-Paare im `data`-Dictionary
for fid, value in data.items():
    # Erstelle ein neues Dictionary für jedes Spaltenwert-Paar
    entry = {
        "Field": fid,
        "Value": value
    }
    # Füge das Eintrag-Dictionary dem JSON-Objekt hinzu
    json_data.append(entry)

# JSON-Objekt aus der Liste von Einträgen erstellen
json_output = json.dumps(json_data, indent=4)

# JSON-Output anzeigen
print(json_output)

# Verbindung schließen
conn.close()