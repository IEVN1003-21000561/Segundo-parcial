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