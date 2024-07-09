let submitButton = document.querySelector("#Formulario #Crear");

submitButton.addEventListener("click", ()=>{
    let data_post = {
        'familia': document.querySelector("#Formulario #Titulo").value,
        'gen': document.querySelector("#Formulario #Descripcion").value
    }
    
    fetchData(
        "http://localhost:5000/api/mariposas/create/",
        "POST",
        (data) => {
            document.querySelector("#Formulario").reset();
            window.location.replace("../index.html");
        },
        data_post
    );
    }
);