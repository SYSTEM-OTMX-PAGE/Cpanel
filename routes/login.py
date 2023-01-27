from flask import Blueprint, request, redirect, render_template, session, flash
import funciones.Login.funciones_login as RouteLogin

login_routes = Blueprint("login_routes", __name__)


#***FUNCION DE RUTA PRINCIPAL***
@login_routes.route('/')
def index():
    return redirect("/login")

#***FUNCION PARA MANDAR Y RECIBIR DATOS DE LOGIN***
@login_routes.route('/login', methods = ['GET','POST'])
def sign_in():
    if request.method == 'POST':
        return RouteLogin.login(request)
    elif request.method == 'GET':
        return render_template('LOGIN/index.html', titulo = "INICIAR SESION")   

#***HOMEPAGE***
@login_routes.get('/CPANEL')
def homepage():
    if session["ROL"] == "administrador":
        return render_template('CPANEL/home.html', titulo ="Bienvenido: " +str(session["USER"]))
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect('/login')          