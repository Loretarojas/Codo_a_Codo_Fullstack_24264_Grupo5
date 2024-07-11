let container = document.querySelector(".container");
let contactosCompleto = document.querySelector(".api-complete");
let contactosId = document.querySelector(".api-id");

let contacto_completo = contactosCompleto.cloneNode(true);
let contacto_id = contactosId.cloneNode(true);

contactosCompleto.remove();
contactosId.remove();

fetchData(
    "http://127.0.0.1:5000/contacto/",
    "GET",
    (data) => {
        console.log(data);

        let contactos = [];

        for(const contacto of data){
            console.log(contacto);

            let newContacto = contacto_completo.cloneNode(true);
           
            newContacto.querySelector(".contacto").innerHTML = contacto.id;
         

            contactos.push(newContacto);

        }
       container.replaceChildren(...contactos);                                                 
    }
 );
