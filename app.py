from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/admin")
def admin():

    total_usuarios = 100
    total_votos = 55
    votos_pendientes = total_usuarios - total_votos

    return render_template(
        "admin.html",
        total_usuarios=total_usuarios,
        total_votos=total_votos,
        votos_pendientes=votos_pendientes
    )


@app.route("/resultados")
def resultados():

    candidatos = [
        {
            "nombre": "Juan Pérez",
            "partido": "Partido A",
            "votos": 25
        },
        {
            "nombre": "María López",
            "partido": "Partido B",
            "votos": 18
        },
        {
            "nombre": "Carlos Ruiz",
            "partido": "Partido C",
            "votos": 12
        }
    ]

    total_votos = sum(candidato["votos"] for candidato in candidatos)

    ganador = max(candidatos, key=lambda candidato: candidato["votos"])

    return render_template(
        "resultados.html",
        candidatos=candidatos,
        total_votos=total_votos,
        ganador=ganador
    )


if __name__ == "__main__":
    app.run(debug=True)