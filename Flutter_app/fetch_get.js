let container = document.querySelector(".container");

let mariposaTemplate = document.querySelector(".form-carga");




fetchData(
    "http://localhost:5000/mariposa/",
    "GET",
    (data) => {
        console.log(data);

        let mariposas = [];

        for(const mariposa of data) {
            console.log(mariposa);
          
            let newMariposa = mariposaCompleted.cloneNode(true);

            newMariposa.querySelector(".nombre").innerHTML = mariposa.nombre;
            newMariposa.querySelector(".especie").innerHTML = mariposa.especie;
            newMariposa.querySelector(".familia").innerHTML = mariposa.familia;
            newMariposa.querySelector(".nombreCientifico").innerHTML = mariposa.nombreCientifico;
            newMariposa.querySelector(".pais").value = mariposa.pais;
            newMariposa.querySelector(".peligroExtincion").checkbox = mariposa.peligroExtincion;
            newMariposa.querySelector(".migratoria").checkbox = mariposa.migratoria;
          
            mariposas.push(newMariposa);
        }
    }
);
