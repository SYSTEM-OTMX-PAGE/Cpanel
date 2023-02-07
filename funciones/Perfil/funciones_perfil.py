from database import database as mongoDB
from flask import Flask, render_template, session, redirect, flash,request
from werkzeug.security import generate_password_hash

BD = mongoDB.ConexionMongo()

def perfil():
    if session["ROL"] == "administrador":
        titulo ="Informacion "+str(session["USER"])
        Administradores = BD['admin']
        Admin = Administradores.find_one({'email':session["USER"]})
        return render_template('PERFIL/perfil.html', titulo=titulo, admin=Admin)


def actualizarPassword(key,campo):
    if session ["ROL"] == "administrador":
        try:
            Administradores = BD['admin']
            dato = request.form['password']
            if dato:
                dato = generate_password_hash(dato, method='sha256')
                Administradores.update_one({'email':key}, {'$set':{campo:dato}}) 
                flash("CONTRASEÑA ACTUALIZADA CORRECTAMENTE")
                return perfil()
        except Exception as e:
            flash("ERROR FALLO LA ACTUALIZACION DE CONTRASEÑA: "+str(e))        
            return perfil()                   
    