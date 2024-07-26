document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('butterfly-search-button');
    if (button) {
        button.addEventListener('click', function() {
            let data_post = {
                'nombre': document.querySelector("#form-carga #nombre").value,
                'especie': document.querySelector("#form-carga #especie").value,
                'familia': document.querySelector("#form-carga #familia").value,
                'nombreCientifico': document.querySelector("#form-carga #nombreCientifico").value,
                'pais': document.querySelector("#form-carga #pais").value
            }

            fetchData(
                "http://127.0.0.1:5000/api/mariposa/create/",
                "POST",
                (data) => {
                    document.querySelector("#form-carga").reset();
                    window.location.replace("../pages/gestionbutterflies.html");
                },
                data_post
            );

        });
    } else {
        console.error('El botón no se encontró en el DOM.');
    }
});