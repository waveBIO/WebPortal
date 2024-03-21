const apiUrl1 = "http://127.0.0.1:5000/get_KREDSTRU";

const apiUrl2 = "http://127.0.0.1:5000/get_ROHKREDSTRU";

// GET-Anfrage an die API senden
fetch(apiUrl1)
  .then(response => {
    // Überprüfen, ob die Antwort erfolgreich war (Statuscode 200)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    // Antwort als JSON formatieren und zurückgeben
    return response.json();
  })
  .then(data => {
    console.log(data.result);
    // Hier kannst du mit den Daten aus der API arbeiten
    const jsonDataElement = document.getElementById('json-data');
    const dataList = document.createElement('ul');

    data.result.forEach(element => {
      const listItem = document.createElement('li');
      listItem.textContent = JSON.stringify(element);
      dataList.appendChild(listItem);
    });

    jsonDataElement.appendChild(dataList);
  })
  .catch(error => {
    // Fehlerbehandlung
    console.error('There was a problem with the fetch operation:', error);
  });


// GET-Anfrage an die API senden
fetch(apiUrl2)
  .then(response => {
    // Überprüfen, ob die Antwort erfolgreich war (Statuscode 200)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    // Antwort als JSON formatieren und zurückgeben
    return response.json();
  })
  .then(data => {
    console.log(data.result);
    // Hier kannst du mit den Daten aus der API arbeiten
    const jsonDataElement = document.getElementById('json-data');
    const dataList = document.createElement('ul');

    data.result.forEach(element => {
      const listItem = document.createElement('li');
      listItem.textContent = JSON.stringify(element);
      dataList.appendChild(listItem);
    });

    jsonDataElement.appendChild(dataList);
  })
  .catch(error => {
    // Fehlerbehandlung
    console.error('There was a problem with the fetch operation:', error);
  });




