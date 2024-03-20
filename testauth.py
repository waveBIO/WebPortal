import requests

# URL des Servers, an den die POST-Anfrage gesendet werden soll
url = 'http://localhost:5000/increment_value'

# Daten, die in der POST-Anfrage gesendet werden sollen (im JSON-Format)
data = {
    'value': 30
}

# Senden der POST-Anfrage an den Server
response = requests.post(url, json=data)

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    print('Benutzer erfolgreich erstellt.')
else:
    print('Fehler beim Erstellen des Benutzers:', response.text)