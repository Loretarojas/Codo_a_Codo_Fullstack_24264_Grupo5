let container = document.querySelector("");
let mariposasCompleto = document.querySelector("");
let mariposasId = document.querySelector("");

let mariposa_completo = mariposasCompleto.cloneNode(true);
let mariposa_id = mariposasId.cloneNode(true);

mariposasCompleto.remove();
mariposasId.remove();

fetchData(
    "http://127.0.0.1:5000/mariposa/",
    "GET",
    (data) => {
        console.log(data);

        let mariposas = [];

        for(const mariposa of data){
            console.log(mariposa);

            let newMariposa = mariposa_completo.cloneNode(true);
           
            newMariposa.querySelector("").innerHTML = mariposa.id;
         

            mariposas.push(newMariposa);

        }
       container.replaceChildren(...mariposas);                                                 
    }
 );
