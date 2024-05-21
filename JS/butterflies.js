document.addEventListener("DOMContentLoaded", () => {
    let mariposas = [];

    // Cargar datos del archivo JSON
    fetch('../data/mariposas.json')
        .then(response => response.json())
        .then(data => {
            mariposas = data;

            // Función de búsqueda avanzada
            document.getElementById('buscar-mariposas').addEventListener('click', () => {
                const familiaInsectoInput = document.getElementById('familia-insecto');
                const generoInsectoInput = document.getElementById('genero-insecto');
                const especieInsectoInput = document.getElementById('especie-insecto');
                const ubicacionInput = document.getElementById('ubicacion');

                const familiaInsecto = familiaInsectoInput.value.trim().toLowerCase();
                const generoInsecto = generoInsectoInput.value.trim().toLowerCase();
                const especieInsecto = especieInsectoInput.value.trim().toLowerCase();
                const ubicacion = ubicacionInput.value.trim().toLowerCase();

                const resultados = mariposas.filter(mariposa => {
                    const matchFamilia = !familiaInsecto || (mariposa["flia"] && mariposa["flia"].toLowerCase() === familiaInsecto);
                    const matchGenero = !generoInsecto || (mariposa["gen"] && mariposa["gen"].toLowerCase() === generoInsecto);
                    const matchEspecie = !especieInsecto || (mariposa["especie"] && mariposa["especie"].toLowerCase() === especieInsecto);
                    const matchUbicacion = !ubicacion || (mariposa["ubic"] && mariposa["ubic"].toLowerCase() === ubicacion);

                    return matchFamilia && matchGenero && matchEspecie && matchUbicacion;
                });

                mostrarResultados(resultados, 'butterfly-results');
            });

            // Función de búsqueda general
            document.getElementById('butterfly-search-button').addEventListener('click', () => {
                const keyword = document.getElementById('butterfly-search-input').value.trim().toLowerCase();

                const resultados = mariposas.filter(mariposa => {
                    for (let key in mariposa) {
                        if (mariposa.hasOwnProperty(key) && mariposa[key].toLowerCase().includes(keyword)) {
                            return true;
                        }
                    }
                    return false;
                });

                mostrarResultados(resultados, 'butterfly-search-results');
            });
        })
        .catch(error => console.error('Error al cargar el JSON:', error));

    // Función para mostrar resultados
    function mostrarResultados(resultados, contenedorId) {
        const contenedorResultados = document.getElementById(contenedorId);
        contenedorResultados.innerHTML = '';

        if (resultados.length > 0) {
            resultados.forEach(mariposa => {
                const div = document.createElement('div');
                div.classList.add('result-item');
                div.textContent = ` Familia del Insecto: ${mariposa["flia"]}, 
                                    Género del Insecto: ${mariposa["gen"]}, 
                                    Especie del Insecto: ${mariposa["especie"]}, 
                                    Ubicación: ${mariposa["ubic"]}`;
                contenedorResultados.appendChild(div);
            });
        } else {
            contenedorResultados.innerHTML = '<div class="result-item">No se encontraron resultados</div>';
        }
    }
});
