#SQL -> Querys
#El traductor de phyton a sql es la herramienta SQLAlchemy
from extensions import db
#Vamos a importar el modulo para hashear contraseñas
from werkzeug.security import generate_password_hash, check_password_hash
#generate_password_hash -> recibe un texto y lo hashea en una serie de caracteres
#con longitud igual en todos los caso

#check_password_hash recibe dos datos:
#1.- El hash que esta en la base de datos
#2.- Contraseña que el usuario escribio

#Vamos a crear un modelo
#Un modelo es un plano de como se ve la tabla en sql

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String, nullable=False)
    username = db.Column(db.String(120), nullable=False)
   
   #Tenemos el metodo para cifrar las contraseñas
    def hashear_password(self, password_original):
         
         self.password = generate_password_hash(password_original)
   
    def verificar_password(self, password_plano):
        return check_password_hash(self.password, password_plano)
        
    
    def save(self):
       #Creamos una conexión con la base de datos para añadir información
       db.session.add(self)
       #Nos aseguramos que los cambios se hagan
       db.session.commit()

       
    def delete(self):
       db.session.delete(self)
       #Nos aseguramos de que los cambios se guarden
       db.session.commit()



class PuestoComida(db.Model):
    __tablename__ = 'puestoComida'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', backref='puestos')  # Relación con el usuario

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()