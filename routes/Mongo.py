from flask import Blueprint,session,redirect, flash, jsonify
import funciones.BasesDatos.funciones_BD as RouteBD


Mongo_routes = Blueprint("Mongo_routes",__name__)

@Mongo_routes.route('/bases-datos')
def MongoBD():
    try:
        if "administrador" in session["ROL"]:
            return RouteBD.Bases()
        else:
            flash("POR FAVOR INICIA SESION")
            return redirect('/login')
    except Exception as e:
        flash("ERROR EN EL SERVIDOR: "+str(e))
        return redirect('/login')            

@Mongo_routes.route('/bases_colecciones/<key>')
def CollectionsBD(key):
    try:
        if "administrador" in session["ROL"]:
            return RouteBD.bdColecctions(key)
        else:
            flash("POR FAVOR INICIA SESION")
            return redirect('/login')
    except Exception as e:
        flash("ERROR EN EL SERVIDOR: "+str(e))
        return redirect('/bases-datos')      


@Mongo_routes.route('/informacion_coleccion/<nameDataBase>,<colection>')


def InformacionColeccion(nameDataBase,colection):
            
    try:
        if "administrador" in session["ROL"]:
            return RouteBD.datosColeccion(nameDataBase, colection)
        else:
            flash("POR FAVOR INICIA SESION")
            return redirect('/login')
    except Exception as e:
        print("ERROR EN EL SERVIDOR: "+str(e))
        return redirect('/bases-datos')                             
        

@Mongo_routes.get('/cerrar-sesion')
def close_session():
    session.pop('ROL', None)
    session.pop('USER', None)
    flash("SESION FINALIZADA")
    return redirect('/login')

        