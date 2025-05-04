from models import Usuario

from models import PuestoComida

#Un archivo que contiene todas las acciones que un usuario pueda realizar
#Necesitamos un metodo para que elusuario pueda crear una cuenta
def crear_cuenta(nombre, lastname, email, password, username):
    # Creamos un objeto de tipo usuario que contendra la informacion para la db
    usuario_existentes = Usuario.query.filter_by(email=email).first()
#Revisamos si lo que regresa esa query es diferente a None
    if usuario_existentes is not None:
        print('El correo ya existe en la db')
        return{'status':'error', 'error':'El correo ya esta registrada'}
    
    #Esto solo se ejecuta si en la db no existe la cuenta que el usuario 
    #esta registrado


    nuevo_usuario = Usuario(name = nombre, lastname = lastname, email = email, username = username)
    nuevo_usuario.hashear_password(password_original=password)
    #Guardamos este nuevo objeto en la db
    nuevo_usuario.save()
    return{'status':'ok', 'email':email}

def iniciar_sesion(email, password):
    usuario_existentes = Usuario.query.filter_by(email=email).first()

    if usuario_existentes is None:
        print('La cuenta no existe')
        return {'status': 'error', 'error': 'La cuenta no existe'}

    if usuario_existentes.verificar_password(password_plano=password):
        print('Inicio de sesión exitoso :D')
        
        return {
            'status': 'ok',
            'email': email,
            'usuario_id': usuario_existentes.id  # 👈 Esta línea es clave
        }

    else:
        print('La contraseña es incorrecta')
        return {'status': 'error', 'error': 'Contraseña incorrecta :('}



def crear_puesto(nombre, direccion, telefono, usuario_id):
    try:
        nuevo_puesto = PuestoComida(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            usuario_id=usuario_id
        )
        nuevo_puesto.save()
        return {"status": "ok", "mensaje": "Ubicación guardada correctamente"}
    except Exception as e:
        print("Error al guardar ubicación:", e)
        return {"status": "error", "mensaje": "No se pudo guardar la ubicación"}