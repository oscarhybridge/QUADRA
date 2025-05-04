#cv4WLC2pw47t2ZCJ

from flask import Flask
#Desde el archivo routes quiero que importes la funcion 'cargar_rutas'
from routes import cargar_rutas

from extensions import db



app = Flask(__name__)
app.secret_key = '9as8df9as8df9a8sdf908a09sdf890asdf098as'

#1.- Configuremos la app para conectarse a una db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.acrgiifzmjcatueerayy:cv4WLC2pw47t2ZCJ@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
#postgresql://postgres:[YOUR-PASSWORD]@db.acrgiifzmjcatueerayy.supabase.co:5432/postgres

#2.- Desactivamos el seguimiento de modificaciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#Cargamos las rutas creadas desde el archivo routes.py
cargar_rutas(app)
app.run(port=8000)


#El metodo run le va a indicar nuestro servidor que va a comenzar
# a recibir peticiones
#puerti 8080: le indica al usuario que accedera al servidor que creamos
#puerto 22: Este puerto crea uan conexion ssh con una computadora