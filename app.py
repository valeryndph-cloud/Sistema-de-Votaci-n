from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave-temporal-votacion"

CANDIDATOS = [
	{"id": 1, "nombre": "Ana Torres", "propuesta": "Una comunidad más participativa."},
	{"id": 2, "nombre": "Bruno Martinez", "propuesta": "Transparencia en cada decisión."},
	{"id": 3, "nombre": "Camila Rojas", "propuesta": "Más oportunidades para todos."},
]


@app.get("/")
def candidatos():
	return render_template("candidatos.html", candidatos=CANDIDATOS)


@app.route("/votar/<int:candidato_id>", methods=["GET", "POST"])
def votar(candidato_id):
	candidato = next((item for item in CANDIDATOS if item["id"] == candidato_id), None)
	if candidato is None:
		return "Candidato no encontrado", 404

	if request.method == "POST":
		flash(f"Tu voto por {candidato['nombre']} fue enviado.", "success")
		return redirect(url_for("candidatos"))

	return render_template("votar.html", candidato=candidato)


if __name__ == "__main__":
	app.run(debug=True)

# Ejemplo básico para identificar al ganador en app.py
def obtener_ganador(votos):
    if not votos:
        votos = {"Opción A": 0, "Opción B": 0}
    ganador = max(votos, key=votos.get)
    return ganador