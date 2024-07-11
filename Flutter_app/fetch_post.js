let submitButton = document.querySelector("#butterfly-search-button");

submitButton.addEventListener("click", ()=>{
    let data_post = {
        'nombre': document.querySelector("#nombre").value,
        'asunto': document.querySelector("#asunto").value
    }
    
    fetchData(
        "http://localhost:5000/contacto/create/",
        "POST",
        (data) => {
            document.querySelector("#formulario").reset();
            window.location.replace("../index.html");
        },
        data_post
    );
    }
);