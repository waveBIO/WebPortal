import pyodbc
import json

server = 'NB-GRS-AS'
database = 'SIGNUM_GRSDEMO_FL'
username = 'GRS'
password = 'SIGNUM'

conn = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()
cursor.execute("select KONTEXT, TYPE, SUBTYPE, FID, ID, PID, TEXT, FTYPE from RSTRU where KONTEXT = 'KRED' and WEBPUBLISH = 1")

rows = cursor.fetchall()

results = []

for row in rows:

    row_dict = {
        "FID" : row[3],
        "Text" : row[6],
        "FType" : row[7]
    }

    results.append(row_dict)

json_data = results

print(json_data)

cursor.close