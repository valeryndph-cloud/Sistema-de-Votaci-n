console.log("Módulo de resultados cargado");

// Buscar candidatos en la tabla
function filtrarResultados() {
    const filtro = document.getElementById("filtro").value.toLowerCase();
    const filas = document.querySelectorAll("#tablaResultados tr");

    filas.forEach(function (fila) {
        const candidato = fila.cells[0].textContent.toLowerCase();
        const partido = fila.cells[1].textContent.toLowerCase();

        if (candidato.includes(filtro) || partido.includes(filtro)) {
            fila.style.display = "";
        } else {
            fila.style.display = "none";
        }
    });
}

// Ordenar candidatos de mayor a menor cantidad de votos
function ordenarPorVotos() {
    const tabla = document.getElementById("tablaResultados");
    const filas = Array.from(tabla.querySelectorAll("tr"));

    filas.sort(function (a, b) {
        const votosA = parseInt(a.cells[2].textContent);
        const votosB = parseInt(b.cells[2].textContent);

        return votosB - votosA;
    });

    filas.forEach(function (fila) {
        tabla.appendChild(fila);
    });
}