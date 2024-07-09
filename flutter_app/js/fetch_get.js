let mariposasContainer = document.querySelector(".mariposas-container");
let mariposasPendingReference = document.querySelector(".mariposas-pending-reference");
let mariposasCompletedReference = document.querySelector(".mariposas-completed-reference");


let pendingMariposas = mariposasPendingReference.cloneNode(true);
let completedMariposas = mariposasCompletedReference.cloneNode(true);


mariposasPendingReference.remove();
mariposasCompletedReference.remove();


fetchData(
    "http://127.0.0.1:5000/api/mariposas/pending/",
    "GET",
    (data) => {
        console.log(data);

        let mariposas = [];

        for(const mariposas of data){
            console.log(mariposas);

            let newMariposas = mariposasPending.cloneNode(true);

            newMariposas.querySelector("h3 .familia").innerHTML = mariposas.familia;
            newMariposas.querySelector(".gen").innerHTML = mariposas.gen;
            newMariposas.querySelector(".fecha").innerHTML = mariposas.fecha_creacion;
            newMariposas.querySelector(".mariposas_id").value = mariposas.id;

            mariposas.push(newMariposas);

        }
        mariposasContainer.replaceChildren(...mariposas);
    }
 );

