const apiUrl = "http://127.0.0.1:5000/get_RSTRU";

// GET-Anfrage an die API senden
fetch(apiUrl)
  .then(response => {
    // Überprüfen, ob die Antwort erfolgreich war (Statuscode 200)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Antwort als JSON formatieren und zurückgeben
    return response.json();
  })
  .then(data => {
    // Hier kannst du mit den Daten aus der API arbeiten
    console.log(data);
  })
  .catch(error => {
    // Fehlerbehandlung
    console.error('There was a problem with the fetch operation:', error);
  });





