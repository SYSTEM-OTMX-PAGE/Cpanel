from database import database as mongoDB
from flask import Flask, render_template, session, redirect, flash,request

BD = mongoDB.ConexionMongo()

def perfil():
    if session["ROL"] == "administrador":
        titulo ="Informacion "+str(session["USER"])
        Administradores = BD['admin']
        Admin = Administradores.find_one({'email':session["USER"]})#REVISAR PORQUE NO OBTIENE EL CAMPO EMAIL (MUESTRA TODO LO QUE TIENE USER)
        print(Admin)
        return render_template('PERFIL/perfil.html', titulo=titulo, admin=Admin)

#CHECAR ESTO xd
def actualizarPassword(key,campo):
    if session ["ROL"] == "administrador":
        Administradores = BD["admin"]
        dato = request.form["password"]
        if dato:
            print(dato)
            Administradores.update_one({'correo':key}, {'$set':{campo:dato}}) 
        return perfil()                   
    