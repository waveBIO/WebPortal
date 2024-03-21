import pyodbc
import json

server = 'NB-GRS-AS'
database = 'SIGNUM_GRSDEMO_FL'
username = 'GRS'
password = 'SIGNUM'

conn = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()
cursor.execute("select KONTEXT, TYPE, SUBTYPE, FID, ID, PID, TEXT, FTYPE from RSTRU where KONTEXT = 'KRED' and WEBPUBLISH = 1")# KRED RSTRU
rows1 = cursor.fetchall()

results1 = []

for row in rows1:

    row_dict1 = {
        "FID" : row[3],
        "Text" : row[6],
        "FType" : row[7]
    }

    results1.append(row_dict1)

json_data1 = results1
###############################
cursor.execute("select KONTEXT, TYPE, SUBTYPE, FID, ID, PID, TEXT, FTYPE from RSTRU where KONTEXT = 'ROHKRED' and WEBPUBLISH = 1")# ROHKRED RSTRU
rows2 = cursor.fetchall()

results2 = []

for row in rows2:
    row_dict2 = {
        "FID" : row[3],
        "Text" : row[6],
        "FType" : row[7]
    }

    results2.append(row_dict2)

json_data2 = results2

print(json_data1)
print(json_data2)

cursor.close