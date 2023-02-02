from flask import Blueprint, render_template,session,flash,redirect, request
import funciones.Perfil.funciones_perfil as RoutePerfil

Perfil_routes = Blueprint("Perfil_routes",__name__)

@Perfil_routes.route('/informacion-perfil')
def informacion_perfil():
    try:
        if "administrador" in session["ROL"]:
            return RoutePerfil.perfil()
        else:
            flash("POR FAVOR INICIA SESION")
            return redirect('/login')
    except Exception as e:
        flash("ERROR EN EL SERVIDOR: "+str(e))
        return redirect('/login')            

@Perfil_routes.route('/actualizar-password',methods=['POST'])
def password():
    if request.method == 'POST':
        return RoutePerfil.actualizarPerfil(request) and redirect('/informacion-perfil')
