let submitButton = document.querySelector(".butterfly-search-button");

submitButton.addEventListener("click", ()=>{
    let data_post = {
        'nombre': document.querySelector(".nombre").value,
        'especie': document.querySelector(".especie").value,
        'familia': document.querySelector(".familia").value,
        'nombreCientifico': document.querySelector(".nombreCientifico").value,
        'pais': document.querySelector(".pais").value,
        'peligroExtincion': document.querySelector("#peligroExtincion").checked,
        'migratoria': document.querySelector("#migratoria").checked
       
    }
    
    fetchData(
        "http://localhost:5000/mariposa/create/",
        "POST",
        (data) => {
            document.querySelector(".form-carga").reset();
            window.location.replace("./pages/cargabutterflies.html");
        },
        data_post
    );
    
});