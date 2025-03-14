// Archivo: script.js
document.addEventListener("DOMContentLoaded", () => {
    const timeline = document.getElementById("timeline");

    const events = [
        { year: "1900", event: "Inicio del uso de energía hidroeléctrica." },
        { year: "1950", event: "Primeros paneles solares comerciales." },
        { year: "2000", event: "Avances significativos en energías limpias." }
    ];

    events.forEach(e => {
        const div = document.createElement("div");
        div.innerHTML = `<strong>${e.year}</strong>: ${e.event}`;
        timeline.appendChild(div);
    });
});
