function fetchData(url, method, callback, data) {
    fetch(url, {
        method: method, // Método HTTP
        headers: {
            'Content-Type': 'application/json', // Establece el contenido como JSON
        },
        body: JSON.stringify(data) // Convierte los datos a una cadena JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => callback(data))
    .catch(error => console.error('Error en la solicitud:', error));
}