document.addEventListener("DOMContentLoaded", () => {
    let mariposas = [];

    // Cargar datos del archivo JSON
    fetch('../data/mariposas.json')
        .then(response => response.json())
        .then(data => {
            mariposas = data;
        })
        .catch(error => console.error('Error al cargar el JSON:', error));

    // Función de búsqueda avanzada
    document.getElementById('buscar-mariposas').addEventListener('click', () => {
        const familiaBotanica = document.getElementById('familia-botanica').value.toLowerCase();
        const generoPlanta = document.getElementById('genero-planta').value.toLowerCase();
        const especiePlanta = document.getElementById('especie-planta').value.toLowerCase();
        const familiaInsecto = document.getElementById('familia-insecto').value.toLowerCase();
        const generoInsecto = document.getElementById('genero-insecto').value.toLowerCase();
        const especieInsecto = document.getElementById('especie-insecto').value.toLowerCase();
        const ubicacion = document.getElementById('ubicacion').value.toLowerCase();

        const resultados = mariposas.filter(mariposa => {
            return (!familiaBotanica || (mariposa["Familia Botánica"] && mariposa["Familia Botánica"].toLowerCase().includes(familiaBotanica))) &&
                   (!generoPlanta || (mariposa["Género de la planta"] && mariposa["Género de la planta"].toLowerCase().includes(generoPlanta))) &&
                   (!especiePlanta || (mariposa["Especie de la planta"] && mariposa["Especie de la planta"].toLowerCase().includes(especiePlanta))) &&
                   (!familiaInsecto || (mariposa["Familia del Insecto"] && mariposa["Familia del Insecto"].toLowerCase().includes(familiaInsecto))) &&
                   (!generoInsecto || (mariposa["Género del Insecto"] && mariposa["Género del Insecto"].toLowerCase().includes(generoInsecto))) &&
                   (!especieInsecto || (mariposa["Especie del Insecto"] && mariposa["Especie del Insecto"].toLowerCase().includes(especieInsecto))) &&
                   (!ubicacion || (mariposa["Ubicación"] && mariposa["Ubicación"].toLowerCase().includes(ubicacion)));
        });

        mostrarResultados(resultados, 'butterfly-results');
    });

    // Función para mostrar resultados
    function mostrarResultados(resultados, contenedorId) {
        const contenedorResultados = document.getElementById(contenedorId);
        contenedorResultados.innerHTML = '';

        if (resultados.length > 0) {
            resultados.forEach(mariposa => {
                const div = document.createElement('div');
                div.classList.add('result-item');
                div.textContent = `Familia Botánica: ${mariposa["Familia Botánica"]}, 
                                    Género de la planta: ${mariposa["Género de la planta"]}, 
                                    Especie de la planta: ${mariposa["Especie de la planta"]}, 
                                    Familia del Insecto: ${mariposa["Familia del Insecto"]}, 
                                    Género del Insecto: ${mariposa["Género del Insecto"]}, 
                                    Especie del Insecto: ${mariposa["Especie del Insecto"]}, 
                                    Ubicación: ${mariposa["Ubicación"]}`;
                contenedorResultados.appendChild(div);
            });
        } else {
            contenedorResultados.innerHTML = '<div class="result-item">No se encontraron resultados</div>';
        }
    }
});
