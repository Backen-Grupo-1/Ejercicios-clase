from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

anuncios = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    grupo = "Grupo 1"
    objetivo = "Aprender a desarrollar aplicaciones web con Flask en este curso."
    integrantes = [
        {"nombre": "Ana", "edad": 25, "profesion": "Ingeniera"},
        {"nombre": "Luis", "edad": 30, "profesion": "Desarrollador"},
        {"nombre": "Carlos", "edad": 28, "profesion": "Analista"},
        {"nombre": "María", "edad": 26, "profesion": "Diseñadora"}
    ]
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("about.html", 
                           grupo=grupo,
                           objetivo=objetivo,
                           integrantes=integrantes,
                           fecha_hora=fecha_hora_actual)

@app.route("/perfil")
def perfil():
    nombre = request.args.get("nombre", "Usuario")
    edad = request.args.get("edad", "Desconocida")
    profesion = request.args.get("profesion", "Estudiante")

    return render_template("perfil.html", 
                           nombre=nombre, 
                           edad=edad, 
                           profesion=profesion)

@app.route("/anuncio", methods=["GET", "POST"])
def anuncio():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        contenido = request.form.get("contenido")
        prioridad = request.form.get("prioridad", "media")

        if not titulo or not contenido:
            return "El título y el contenido son obligatorios", 400

        nuevo_anuncio = {
            "titulo": titulo,
            "contenido": contenido,
            "prioridad": prioridad,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        anuncios.append(nuevo_anuncio)
        
        return redirect(url_for("ver_anuncios"))
    
    return render_template("anuncio.html")

@app.route("/anuncios")
def ver_anuncios():
    return render_template("anuncios.html", anuncios=anuncios)

if __name__ == "__main__":
    app.run(debug=True)