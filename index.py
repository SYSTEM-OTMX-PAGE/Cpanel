from flask import Flask, render_template, request, redirect, url_for, session, flash
import funciones.Login.funciones_login as Login
import os

app = Flask(__name__)
app.host = '0.0.0.0'
app.port = os.getenv('PORT')
app.secret_key = b'\xd4\x8a\xa7\x9f\xf39i\x17|>\xad\xa6R]\xc0W\xc8\xa3M\x852\xa34>'

#FUNCIONES DEL HOME CPANEL
#***HOMEPAGE***
@app.route('/CPANEL')
def homepage():
    if session["ROL"] == "administrador":
        return render_template('CPANEL/home.html', titulo ="Bienvenido: " +str(session["USER"]))
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect(url_for('sign_in'))  

#FUNCIONES PARA LOGIN

#***FUNCION DE RUTA PRINCIPAL***
@app.route('/')
def index():
    return redirect(url_for('sign_in'))

#***FUNCION PARA MANDAR Y RECIBIR DATOS DE LOGIN***
@app.route('/login', methods = ['GET','POST'])
def sign_in():
    if request.method == 'POST':
        return Login.login(request)
    elif request.method == 'GET':
        return render_template('LOGIN/index.html', titulo = "INICIAR SESION")    

  

           

#ENDPOINT

if __name__ == '__main__':
    app.run(host=app.host, port=app.port, debug=True)    