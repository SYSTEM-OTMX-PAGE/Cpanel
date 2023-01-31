from flask import Blueprint,session,redirect, flash
import funciones.BasesDatos.funciones_BD as RouteBD


Mongo_routes = Blueprint("Mongo_routes",__name__)

@Mongo_routes.route('/bases-datos')
def MongoBD():
    try:
        if "administrador" in session["ROL"]:
            return RouteBD.bases()
        else:
            flash("POR FAVOR INICIA SESION")
            return redirect('/login')
    except Exception as e:
        flash("ERROR EN EL SERVIDOR: "+str(e))
        return redirect('/login')            

@Mongo_routes.route('/bases_colecciones/<key>')
def colecctions_bd(key):
    try:
        if "administrador" in session["ROL"]:
            return RouteBD.bdcolecctions(key)
        else:
            flash("POR FAVOR INICIA SESION")
            return redirect('/login')
    except Exception as e:
        flash("ERROR EN EL SERVIDOR: "+str(e))
        return redirect('/login')      

@Mongo_routes.route('/informacion_coleccion/<key>')
def informacion_coleccion(key):
    try:
        if "administrador" in session["ROL"]:
            return RouteBD.collectionsInfo(key)
        else:
            flash("POR FAVOR INICIA SESION")
            return redirect('/login')
    except Exception as e:
        flash("ERROR EN EL SERVIDOR: "+str(e))
        return redirect('/login')                             
             

@Mongo_routes.get('/cerrar-sesion')
def close_session():
    session.pop('ROL', None)
    session.pop('USER', None)
    flash("SESION FINALIZADA")
    return redirect('/login')

        