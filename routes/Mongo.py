from flask import Blueprint, render_template
import funciones.BasesDatos.funciones_BD as RouteBD

Mongo_routes = Blueprint("Mongo_routes",__name__)

@Mongo_routes.route('/BASES-DATOS')
def MongoBD():
    return RouteBD.bases()


        