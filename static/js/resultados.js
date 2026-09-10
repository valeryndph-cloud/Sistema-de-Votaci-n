const resultados = [
    {
        nombre: "Juan Pérez",
        partido: "Partido A",
        votos: 25
    },
    {
        nombre: "María López",
        partido: "Partido B",
        votos: 18
    },
    {
        nombre: "Carlos Ruiz",
        partido: "Partido C",
        votos: 12
    }
];


const totalVotos = resultados.reduce(
    (total, candidato) => total + candidato.votos,
    0
);


const tabla = document.getElementById("tablaResultados");

tabla.innerHTML = "";


resultados.forEach(candidato => {

    const porcentaje = ((candidato.votos / totalVotos) * 100).toFixed(2);

    const fila = document.createElement("tr");

    fila.innerHTML = `
        <td>${candidato.nombre}</td>
        <td>${candidato.partido}</td>
        <td>${candidato.votos}</td>
        <td>${porcentaje}%</td>
    `;

    tabla.appendChild(fila);

});


document.getElementById("totalResultados").textContent = totalVotos;


const ganador = resultados.reduce(
    (mayor, candidato) =>
        candidato.votos > mayor.votos ? candidato : mayor
);


document.getElementById("ganador").textContent = ganador.nombre;