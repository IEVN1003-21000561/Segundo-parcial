from flask import Flask, render_template, request
import forms 
from FigurasForm import *
import math


app = Flask(__name__)

app.secret_key = 'clave-secreta'


@app.route("/figuras", methods=["GET", "POST"])
def figuras():
    form = forms.FigurasForm(request.form)
    area = None
    figura = None

    if request.method == "POST":
        figura = request.form["figura"]

        if figura == "triangulo":
            base = float(request.form["base"])
            altura = float(request.form["altura"])
            area = 0.5 * base * altura

        elif figura == "rectangulo":
            largo = float(request.form["largo"])
            ancho = float(request.form["ancho"])
            area = largo * ancho

        elif figura == "circulo":
            radio = float(request.form["radio"])
            area = math.pi * (radio ** 2)

        elif figura == "pentagono":
            lado = float(request.form["lado"])
            apotema = lado / (2 * math.tan(math.pi / 5))
            area = (5 / 2) * lado * apotema

    return render_template("figuras.html", form=form, area=area, figura=figura)


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/Alumnos',methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    alumnos_clase=forms.UseForm(request.form)
    if request.method=='POST'and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
        return render_template('alumnos.html', form=alumnos_clase,
                               mat=mat, nom=nom, ape=ape, em=em)

@app.route('/about')
def about():
    return "<h1>This is the about page.</h1>"

# Nueva Ruta agregada
@app.route('/index')
def index():

    titulo="IEVN1003 -PWA"
    listado=["Opera 1", "Opera 2", "Opera 3", "Opera 4"]

    return render_template('index.html', titulo=titulo, listado=listado) 

@app.route('/operas', methods=['GET', 'POST'])
def operas():

    if request.methods=='POST':
        x1=request.form.get('x1')
        x2=request.form.get('x2')
        resultado=x1+x2
    return render_template('operas.html', resultado=resultado)


@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

#


@app.route('/user/<string:user>')
def user(user):
    return "Hola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1, n2):
    return "la suma es: {}".format(n1 + n2)

@app.route("/prueba")
def prueba():
    return """
        <h1>Prueba de HTML</h1>
        <p>Esto es un parrafo</p>
        <ul>
            <li>Elemento 1</li>
            <li>Elemento 2</li>
            <li>Elemento 3</li>
        </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)