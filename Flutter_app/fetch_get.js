let container = document.querySelector(".container");


fetchData(
    "http://127.0.0.1:5000/mariposa/",
    "GET",
    (data) => {
        console.log(data);

        let mariposas = [];

        for(const mariposa of data){
            console.log(mariposa);

        let newMariposa = document.createElement("div");

        newMariposa.querySelector(".nombre").innerHTML = mariposa.nombre;
        newMariposa.querySelector(".especie").innerHTML = mariposa.especie;
        newMariposa.querySelector(".familia").innerHTML = mariposa.familia;
        newMariposa.querySelector(".nombrecientifico").innerHTML = mariposa.nombrecientifico;
        newMariposa.querySelector(".informacion").innerHTML = mariposa.informacion;
        newMariposa.querySelector(".pais").id = `pais-${mariposa.id}`;
        newMariposa.querySelector("#migratoria").id = `migratoria-${mariposa.id}`;


        mariposas.push(newMariposa);
        }

    }
 );
