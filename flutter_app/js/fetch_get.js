document.addEventListener("DOMContentLoaded", () => {
    let container = document.querySelector("#container-gestionmariposas");

    let mariposaTemplate = document.querySelector("#container-tabla-carga");

    if (mariposaTemplate) {
        let mariposaForm = mariposaTemplate.cloneNode(true);

        mariposaTemplate.remove();

        fetchData(
            "http://127.0.0.1:5000/api/mariposa/",
            "GET",
            (data) => {
                console.log(data);

                for (const mariposa of data) {
                    console.log(mariposa);

                    let newMariposa = mariposaForm.cloneNode(true);

                    newMariposa.querySelector("#nombre").innerHTML = mariposa.nombre;
                    newMariposa.querySelector("#especie").innerHTML = mariposa.especie;
                    newMariposa.querySelector("#familia").innerHTML = mariposa.familia;
                    newMariposa.querySelector("#nombreCientifico").innerHTML = mariposa.nombreCientifico;
                    newMariposa.querySelector("#pais").innerHTML = mariposa.pais;

                    container.appendChild(newMariposa);
                }
            }
        );
    } else {
        console.error("Template element with ID '#container-tabla-carga' not found.");
    }
});