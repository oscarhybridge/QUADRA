# Este archivo va a almacenar única y exclusivamente rutas de nuestro servidor
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from methods import crear_cuenta, iniciar_sesion, crear_puesto


def cargar_rutas(app):

    # Este bloque de código es la base para todas las rutas
    @app.route('/')
    def pagina():
     usuario_id = session.get('usuario_id')
     return render_template('index.html', usuario_id=usuario_id)


    # Ruta para login
    @app.route('/login')
    def informacion_oscar():
        return render_template('login.html')

    # Ruta para signup
    @app.route('/signup')
    def datos():
        return render_template('signup.html')

    # Esta ruta va a manejar la información del login
    @app.route('/manipulacion', methods=['POST'])
    def manipular_datos():
        email = request.form.get('email')
        password = request.form.get('password')

        print(f'''
        Email: {email}
        Password: {password}
        ''')

        resultado = iniciar_sesion(email, password)

        # Si ocurre error, redirigir de nuevo al login y mostrar mensaje
        
        
        if resultado['status'] == 'error':
            flash(resultado['error'], category='error')
            return redirect(url_for('informacion_oscar'))

        # Si todo bien, redirigimos a la página principal
        session['usuario_id'] = resultado['usuario_id']
        return redirect(url_for('pagina'))


    # Esta ruta manejará el registro del usuario
    @app.route('/datos_crear_cuenta', methods=['POST'])
    def obtener_datos_cuenta():
        nombre = request.form.get('name')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        
        print(f'''
        Nombre: {nombre}
        Lastname: {lastname}
        Email: {email}
        Password: {password}
        Username: {username}
        ''')
        
        crear_cuenta(nombre, lastname, email, password, username)
        
        return redirect(url_for('pagina'))

    # Ruta para guardar ubicación
    @app.route('/guardar_ubicacion', methods=['POST'])
    def guardar_ubicacion():
        data = request.json
        # Si tienes sesión activa o algún identificador de usuario, úsalo.
        usuario_id = 10  # Por ahora puedes poner un ID fijo para pruebas

        resultado = crear_puesto(
            nombre=data.get('nombre'),
            direccion=data.get('direccion'),
            telefono=data.get('telefono'),
            
            usuario_id=usuario_id
        )

        return jsonify(resultado), 200 if resultado["status"] == "ok" else 400

