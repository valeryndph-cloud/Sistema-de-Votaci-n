document.addEventListener("DOMContentLoaded", () => {
    const formulario = document.querySelector("[data-formulario-voto]");

    if (!formulario) {
        return;
    }

    formulario.addEventListener("submit", (evento) => {
        const identificacion = document.querySelector("#documento");

        if (!identificacion.value.trim()) {
            evento.preventDefault();
            identificacion.focus();
        }
    });
});