#Este archivo nos ayudara a evitar las importaciones circulares
from flask_sqlalchemy import SQLAlchemy
#creamos un objeto de tipo SQLAlchemy que va a controlar toda la base de datos
db = SQLAlchemy()