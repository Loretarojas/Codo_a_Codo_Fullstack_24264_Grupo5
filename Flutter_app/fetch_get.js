let container = document.querySelector(".container");

let mariposaTemplate = document.querySelector(".form-carga");

fetchData(
    "http://localhost:5000/mariposa/",
    "GET",
    (data) => {
        console.log(data);

        for(const mariposa of data) {
            console.log(mariposa);
          
            let newMariposa = mariposaTemplate.cloneNode(true);

            newMariposa.querySelector("#nombre").innerHTML = mariposa.nombre;
            newMariposa.querySelector("#especie").innerHTML = mariposa.especie;
            newMariposa.querySelector("#familia").innerHTML = mariposa.familia;
            newMariposa.querySelector("#nombreCientifico").innerHTML = mariposa.nombreCientifico;
            newMariposa.querySelector("#pais").value = mariposa.pais;
            newMariposa.querySelector("#peligroExtincion").checked = mariposa.peligroExtincion;
            newMariposa.querySelector("#migratoria").checked = mariposa.migratoria;
          
            container.appendChild(newMariposa);
        }
    }
);
