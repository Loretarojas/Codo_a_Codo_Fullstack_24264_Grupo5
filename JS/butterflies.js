document.addEventListener('DOMContentLoaded', () => {
    const plantas = [
        { nombre: 'Verbena', tipo: 'exterior', tamano: 'pequeño', vida: 'anual' },
        { nombre: 'Coneflower', tipo: 'exterior', tamano: 'mediano', vida: 'perenne' },
        { nombre: 'Buddleja', tipo: 'exterior', tamano: 'grande', vida: 'perenne' },
        { nombre: 'Asclepia', tipo: 'exterior', tamano: 'mediano', vida: 'perenne' },
        { nombre: 'Verbena', tipo: 'exterior', tamano: 'pequeño', vida: 'perenne' },
        { nombre: 'Salvia', tipo: 'exterior', tamano: 'mediano', vida: 'perenne' },
        { nombre: 'Mariposario', tipo: 'exterior', tamano: 'grande', vida: 'perenne' },
        { nombre: 'Milenrama', tipo: 'exterior', tamano: 'mediano', vida: 'perenne' },
        { nombre: 'Coreopsis', tipo: 'exterior', tamano: 'mediano', vida: 'perenne' },
        { nombre: 'Zinnia', tipo: 'exterior', tamano: 'pequeño', vida: 'anual' },
        { nombre: 'Menta', tipo: 'exterior', tamano: 'mediano', vida: 'perenne' },
        { nombre: 'Echinacea', tipo: 'exterior', tamano: 'mediano', vida: 'perenne' },
        { nombre: 'Caléndula', tipo: 'exterior', tamano: 'mediano', vida: 'anual' },
    ];

    const mariposas = [
        { nombre: 'Monarca', tamano: 'grande', colores: 'naranja', vida: 'media', reproduccion: 'medio', migracion: 'si' },
        { nombre: 'Blanca de la col', tamano: 'pequeno', colores: 'blanco', vida: 'corta', reproduccion: 'corto', migracion: 'no' },
        { nombre: 'Mariposa almirante', tamano: 'mediano', colores: 'negro y rojo', vida: 'media', reproduccion: 'medio', migracion: 'no' },
        { nombre: 'Mariposa julia', tamano: 'mediano', colores: 'naranja y negro', vida: 'media', reproduccion: 'medio', migracion: 'no' },
        { nombre: 'Mariposa espejitos', tamano: 'pequeno', colores: 'azul y naranja', vida: 'corta', reproduccion: 'medio', migracion: 'no' },
        { nombre: 'Mariposa tigre', tamano: 'pequeno', colores: 'negro y amarillo', vida: 'corta', reproduccion: 'corto', migracion: 'no' },
        { nombre: 'Mariposa monarca', tamano: 'grande', colores: 'naranja y negro', vida: 'media', reproduccion: 'medio', migracion: 'si' },
        { nombre: 'Mariposa aleta de golondrina', tamano: 'pequeno', colores: 'azul y negro', vida: 'corta', reproduccion: 'corto', migracion: 'no' }
    ];

    const filtrarResultadosPlantas = () => {
        console.log("Buscando plantas...");
        
        const tipoPlanta = document.querySelector('#tipo-planta').value;
        const tamanoPlanta = document.querySelector('#tamano-planta').value;
        const vidaPlanta = document.querySelector('#vida-planta').value;

        const plantasFiltradas = plantas.filter(planta => {
            return (tipoPlanta === '' || planta.tipo === tipoPlanta) &&
                   (tamanoPlanta === '' || planta.tamano === tamanoPlanta) &&
                   (vidaPlanta === '' || planta.vida === vidaPlanta);
        });

        const plantResults = document.querySelector('#plant-results');
        plantResults.innerHTML = plantasFiltradas.map(planta => `<p>${planta.nombre}</p>`).join('');
    };

    const filtrarResultadosMariposas = () => {
        const tamanoMariposa = document.querySelector('#tamano-mariposa').value;
        const coloresMariposa = document.querySelector('#colores-mariposa').value;
        const vidaMariposa = document.querySelector('#vida-mariposa').value;
        const reproduccionMariposa = document.querySelector('#reproduccion-mariposa').value;
        const migracionMariposa = document.querySelector('#migracion-mariposa').value;

        const mariposasFiltradas = mariposas.filter(mariposa => {
            return (tamanoMariposa === '' || mariposa.tamano === tamanoMariposa) &&
                   (coloresMariposa === '' || mariposa.colores === coloresMariposa) &&
                   (vidaMariposa === '' || mariposa.vida === vidaMariposa) &&
                   (reproduccionMariposa === '' || mariposa.reproduccion === reproduccionMariposa) &&
                   (migracionMariposa === '' || mariposa.migracion === migracionMariposa);
        });

        const butterflyResults = document.querySelector('#butterfly-results');
        butterflyResults.innerHTML = mariposasFiltradas.map(mariposa => `<p>${mariposa.nombre}</p>`).join('');
    };

    document.querySelector('#buscar-plantas').addEventListener('click', filtrarResultadosPlantas);
    document.querySelector('#buscar-mariposas').addEventListener('click', filtrarResultadosMariposas);
});
