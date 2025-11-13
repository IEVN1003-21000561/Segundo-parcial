<<<<<<< HEAD
from wtforms import Form, StringField, FloatField, EmailField, PasswordField, IntegerField, SelectField
from wtforms import validators


class PizzaForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El nombre es requerido')
    ])
    
    direccion = StringField("Direccion", [
        validators.DataRequired(message='La direccion es requerida')
    ])
    
    telefono = StringField("Telefono", [
        validators.DataRequired(message='El telefono es requerido')
    ])
    
    fecha = StringField("Fecha", [
        validators.DataRequired(message='La fecha es requerida')
    ])
    
    num_pizzas = IntegerField("Num. de Pizzas", [
        validators.DataRequired(message='El numero de pizzas es requerido')
    ])


class UserForm(Form):
    matricula = IntegerField('Matrícula', [
        validators.DataRequired(message="La matrícula es obligatoria")
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El nombre es obligatorio")
    ])
    apellido = StringField('Apellido', [
        validators.DataRequired(message="El apellido es obligatorio")
    ])
    correo = EmailField('Correo', [
        validators.DataRequired(message="El correo es obligatorio"),
        validators.Email(message="Debe ser un correo válido")
    ])


class FigurasForm(Form):
    valor1 = IntegerField(
        'Valor 1',
        [validators.DataRequired(message="Ingresa el primer valor")]
    )

    valor2 = IntegerField(
        'Valor 2',
        [validators.Optional()]
    )
=======
from wtforms import Form
from wtforms import Form, StringField,FloatField,EmailField,PasswordField,IntegerField
from wtforms  import validators
from wtforms import Form, StringField, FloatField, validators


class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message='El dato es requerido')])
    apellido=StringField("Apellido",[
        validators.DataRequired(message='El dato es requerido')])
    correo=StringField("Correo",[
        validators.Email(message='ingrese correo valido')])
    

class FigurasForm(Form):
    figura = StringField("Figura")
    base = FloatField("Base", [validators.Optional()])
    altura = FloatField("Altura", [validators.Optional()])
    largo = FloatField("Largo", [validators.Optional()])
    ancho = FloatField("Ancho", [validators.Optional()])
    radio = FloatField("Radio", [validators.Optional()])
    lado = FloatField("Lado", [validators.Optional()])
>>>>>>> 1317c8c23f0228b2ae5db8fdbb9773c0dcd23a3f
