from flask import  Flask, render_template, request
from datetime import  datetime


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    group = {"nombre": "Grupo de prueba", "descripcion" : "hola esto es una descripcion", "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    #lista_integrantes = [{"nombre": "Mónica C.", "Patricio H.", "Valentina L.", "Nicolás G.", "Nicolás A.", "Alan R.", "Paula R."]
    lista_integrantes = [{"nombre" : "Mónica C.", "edad" : 31, "profesion" : "backend" }]
    return render_template("about.html", descripcion = group, integrantes = lista_integrantes)

@app.route('/perfil')
def perfil():
    nombre = request.args.get('nombre', 'invitado')
    edad = request.args.get('edad', 'invitado')
    profesion = request.args.get('profesion', 'invitado')
    return render_template("perfil.html", nombre = nombre, edad = edad, profesion = profesion)



if __name__ == '__main__':
    app.run(debug = True)
