from flask import Blueprint, render_template,session,flash,redirect, request
import funciones.Perfil.funciones_perfil as RoutePerfil

Perfil_routes = Blueprint("Perfil_routes",__name__)

@Perfil_routes.route('/informacion-perfil')
def InformacionPerfil():
    return RoutePerfil.perfil()

@Perfil_routes.route('/actualizar-password/<key>,<campo>', methods=['POST'])
def UpdatePassword(key,campo):
    return RoutePerfil.actualizarPassword(key,campo)