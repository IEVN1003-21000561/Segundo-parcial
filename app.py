<<<<<<< HEAD
from flask import Flask, render_template, request, make_response, jsonify
import json
import math
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_pizza'

@app.route('/')
def home():
    return "Hello, World"

@app.route('/index')
def index():
    titulo = "IEVN1003 - PWA"
    listado = ["Opera 1", "Opera 2", "Opera 3"]
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/about')
def about():
    return "<h1>Esta es la página About.</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"ID: {id} | Nombre: {username}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"Número: {n}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route("/prueba")
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
    <p>Esto es un párrafo</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
    '''

@app.route("/operas", methods=['GET', 'POST'])
def operas():
    resultado = None
    if request.method == 'POST':
        x1 = float(request.form.get('x1', 0))
        x2 = float(request.form.get('x2', 0))
        resultado = x1 + x2
    return render_template('operas.html', resultado=resultado)

@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    distancia_resultado = None
    x1 = y1 = x2 = y2 = 0
    
    if request.method == 'POST':
        x1 = float(request.form.get('x1', 0))
        y1 = float(request.form.get('y1', 0))
        x2 = float(request.form.get('x2', 0))
        y2 = float(request.form.get('y2', 0))
        
        distancia_resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distancia_resultado = round(distancia_resultado, 3)
    
    return render_template('distancia.html', 
                         distancia=distancia_resultado,
                         x1=x1, y1=y1, x2=x2, y2=y2)

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    mat = 0
    nom = ""
    ape = ""
    email = ""
    estudiantes = []
    datos = {}
    
    alumno_clas = forms.UserForm(request.form)
    
    if request.method == 'POST':
        if request.form.get("btnElimina") == 'eliminar':
            response = make_response(render_template('Alumnos.html', form=alumno_clas))
            response.delete_cookie('usuario')
            return response
        
        if alumno_clas.validate():
            mat = alumno_clas.matricula.data
            nom = alumno_clas.nombre.data
            ape = alumno_clas.apellido.data
            email = alumno_clas.correo.data
            
            datos = {
                'matricula': mat,
                'nombre': nom.strip(),
                'apellido': ape.strip(),
                'email': email.strip()
            }
            
            data_str = request.cookies.get("usuario")
            if data_str:
                try:
                    estudiantes = json.loads(data_str)
                except:
                    estudiantes = []
            
            estudiantes.append(datos)
    
    response = make_response(render_template('Alumnos.html',
                                            form=alumno_clas,
                                            mat=mat,
                                            nom=nom,
                                            ape=ape,
                                            email=email))
    
    if request.method == 'POST' and datos:
        response.set_cookie('usuario', json.dumps(estudiantes))
    
    return response

@app.route("/get_cookie")
def get_cookie():
    data_str = request.cookies.get("usuario")
    if not data_str:
        return "No hay cookie guardada", 404
    estudiantes = json.loads(data_str)
    return jsonify(estudiantes)

@app.route("/figuras", methods=['GET', 'POST'])
def figuras():
    form = forms.FigurasForm(request.form)
    area = ""
    figura = ""
    
    if request.method == 'POST' and form.validate():
        figura = request.form.get('figura')
        v1 = form.valor1.data
        v2 = form.valor2.data

        if figura == 'circulo':
            area = math.pi * (v1 ** 2)
        elif figura == 'triangulo':
            area = (v1 * v2) / 2
        elif figura == 'rectangulo':
            area = v1 * v2
        elif figura == 'pentagono':
            area = (v1 * v2) / 2

    return render_template('figuras.html', form=form, area=area, figura=figura)

@app.route("/layout")
def layout():
    return render_template('layout.html')

@app.route("/pizzas", methods=['GET', 'POST'])
def pizzas():
    nombre = ""
    direccion = ""
    telefono = ""
    fecha = ""
    pedidos = []
    total_pedido = 0
    mensaje = ""
    mostrar_ventas = False
    ventas = []
    total_dia = 0
    
    if request.method == 'POST':
        
        if request.form.get("btnVerVentas") == 'ver':
            ventas_str = request.cookies.get("ventas")
            if ventas_str:
                ventas = json.loads(ventas_str)
                total_dia = sum(v['total'] for v in ventas)
            mostrar_ventas = True
            
            data_str = request.cookies.get("pedidos")
            if data_str:
                pedidos = json.loads(data_str)
                total_pedido = sum(p['subtotal'] for p in pedidos)
            
            cliente_str = request.cookies.get("cliente")
            if cliente_str:
                cliente = json.loads(cliente_str)
                nombre = cliente['nombre']
                direccion = cliente['direccion']
                telefono = cliente['telefono']
                fecha = cliente.get('fecha', '')
            
            return render_template('pizzas.html',
                                 pedidos=pedidos,
                                 total_pedido=total_pedido,
                                 nombre=nombre,
                                 direccion=direccion,
                                 telefono=telefono,
                                 fecha=fecha,
                                 mostrar_ventas=mostrar_ventas,
                                 ventas=ventas,
                                 total_dia=total_dia)
        
        
        if request.form.get("btnQuitar"):
            indice = int(request.form.get("btnQuitar"))
            data_str = request.cookies.get("pedidos")
            if data_str:
                pedidos = json.loads(data_str)
                if 0 <= indice < len(pedidos):
                    pedidos.pop(indice)
            
            cliente_str = request.cookies.get("cliente")
            if cliente_str:
                cliente = json.loads(cliente_str)
                nombre = cliente['nombre']
                direccion = cliente['direccion']
                telefono = cliente['telefono']
                fecha = cliente.get('fecha', '')
            
            total_pedido = sum(p['subtotal'] for p in pedidos)
            
            response = make_response(render_template('pizzas.html', 
                                                    pedidos=pedidos,
                                                    total_pedido=total_pedido,
                                                    nombre=nombre,
                                                    direccion=direccion,
                                                    telefono=telefono,
                                                    fecha=fecha))
            response.set_cookie('pedidos', json.dumps(pedidos))
            return response
        
  
        if request.form.get("btnQuitarTodo") == 'quitar_todo':
            response = make_response(render_template('pizzas.html',
                                                    mensaje="",
                                                    total_pedido=0,
                                                    nombre="",
                                                    pedidos=[],
                                                    direccion="",
                                                    telefono="",
                                                    fecha=""))
            response.delete_cookie('pedidos')
            response.delete_cookie('cliente')
            return response
        
        
        if request.form.get("btnTerminar") == 'terminar':
            data_str = request.cookies.get("pedidos")
            cliente_str = request.cookies.get("cliente")
            
            if data_str and cliente_str:
                pedidos = json.loads(data_str)
                cliente = json.loads(cliente_str)
                
                total = sum(pedido['subtotal'] for pedido in pedidos)
                
                
                venta = {
                    'nombre': cliente['nombre'],
                    'direccion': cliente['direccion'],
                    'telefono': cliente['telefono'],
                    'fecha': cliente.get('fecha', ''),
                    'pedidos': pedidos,  
                    'total': total
                }
                
                
                ventas_str = request.cookies.get("ventas")
                ventas = []
                if ventas_str:
                    ventas = json.loads(ventas_str)
                
                
                ventas.append(venta)
                
                total_dia = sum(v['total'] for v in ventas)
                
                mensaje = f"Pedido de {cliente['nombre']} confirmado"
                
                response = make_response(render_template('pizzas.html',
                                                        mensaje=mensaje,
                                                        total_pedido=0,
                                                        nombre="",
                                                        pedidos=[],
                                                        direccion="",
                                                        telefono="",
                                                        fecha="",
                                                        mostrar_ventas=False,
                                                        ventas=ventas,
                                                        total_dia=total_dia))
                response.set_cookie('ventas', json.dumps(ventas))
                response.delete_cookie('pedidos')
                response.delete_cookie('cliente')
                return response
        
        
        nombre = request.form.get('nombre', '').strip()
        direccion = request.form.get('direccion', '').strip()
        telefono = request.form.get('telefono', '').strip()
        fecha = request.form.get('fecha', '').strip()
        tamano = request.form.get('tamano')
        num_pizzas_str = request.form.get('num_pizzas', '0')
        
        try:
            num_pizzas = int(num_pizzas_str)
        except:
            num_pizzas = 0
        
        if nombre and direccion and telefono and tamano and num_pizzas > 0:
            precio_base = 0
            if tamano == 'chica':
                precio_base = 40
            elif tamano == 'mediana':
                precio_base = 80
            elif tamano == 'grande':
                precio_base = 120
            
            ingredientes = []
            precio_ingredientes = 0
            if request.form.get('jamon'):
                ingredientes.append('Jamon')
                precio_ingredientes += 10
            if request.form.get('pina'):
                ingredientes.append('Pina')
                precio_ingredientes += 10
            if request.form.get('champinones'):
                ingredientes.append('Champinones')
                precio_ingredientes += 10
            
            ingredientes_texto = ', '.join(ingredientes) if ingredientes else 'Sin ingredientes'
            
            subtotal = (precio_base + precio_ingredientes) * num_pizzas
            
            pedido = {
                'tamano': tamano.capitalize(),
                'ingredientes': ingredientes_texto,
                'num_pizzas': num_pizzas,
                'subtotal': subtotal
            }
            
            cliente = {
                'nombre': nombre,
                'direccion': direccion,
                'telefono': telefono,
                'fecha': fecha
            }
            
            data_str = request.cookies.get("pedidos")
            if data_str:
                try:
                    pedidos = json.loads(data_str)
                except:
                    pedidos = []
            else:
                pedidos = []
            
            pedidos.append(pedido)
            total_pedido = sum(p['subtotal'] for p in pedidos)
            
            response = make_response(render_template('pizzas.html',
                                                    pedidos=pedidos,
                                                    total_pedido=total_pedido,
                                                    nombre=nombre,
                                                    direccion=direccion,
                                                    telefono=telefono,
                                                    fecha=fecha,
                                                    mostrar_ventas=False,
                                                    ventas=[],
                                                    total_dia=0))
            
            response.set_cookie('pedidos', json.dumps(pedidos))
            response.set_cookie('cliente', json.dumps(cliente))
            return response
    
    
    data_str = request.cookies.get("pedidos")
    if data_str:
        try:
            pedidos = json.loads(data_str)
            total_pedido = sum(p['subtotal'] for p in pedidos)
        except:
            pedidos = []
    
    cliente_str = request.cookies.get("cliente")
    if cliente_str:
        try:
            cliente = json.loads(cliente_str)
            nombre = cliente['nombre']
            direccion = cliente['direccion']
            telefono = cliente['telefono']
            fecha = cliente.get('fecha', '')
        except:
            pass
    
    return render_template('pizzas.html',
                          pedidos=pedidos,
                          total_pedido=total_pedido,
                          nombre=nombre,
                          direccion=direccion,
                          telefono=telefono,
                          fecha=fecha,
                          mostrar_ventas=mostrar_ventas,
                          ventas=ventas,
                          total_dia=total_dia,
                          mensaje=mensaje)
=======
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
>>>>>>> 1317c8c23f0228b2ae5db8fdbb9773c0dcd23a3f

if __name__ == '__main__':
    app.run(debug=True)