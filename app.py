from flask import Flask, render_template
from database import conectar, crear_base_datos, agregar_candidatos

app = Flask(__name__)


crear_base_datos()
agregar_candidatos()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/resultados")
def resultados():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT candidatos.nombre,
               candidatos.partido,
               COUNT(votos.id) AS votos
        FROM candidatos
        LEFT JOIN votos
        ON candidatos.id = votos.candidato_id
        GROUP BY candidatos.id
    """)

    candidatos = cursor.fetchall()

    conexion.close()

    lista_candidatos = []

    for candidato in candidatos:
        lista_candidatos.append({
            "nombre": candidato[0],
            "partido": candidato[1],
            "votos": candidato[2]
        })

    total_votos = sum(candidato["votos"] for candidato in lista_candidatos)

    if lista_candidatos:
        ganador = max(
            lista_candidatos,
            key=lambda candidato: candidato["votos"]
        )
    else:
        ganador = {
            "nombre": "Sin resultados"
        }

    return render_template(
        "resultados.html",
        candidatos=lista_candidatos,
        total_votos=total_votos,
        ganador=ganador
    )


if __name__ == "__main__":
    app.run(debug=True)