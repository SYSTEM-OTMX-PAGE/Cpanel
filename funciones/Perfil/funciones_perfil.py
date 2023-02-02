from database import database as mongoDB
from flask import Flask, render_template, session, redirect, flash,request

def DataBase(tabla):
    BD = mongoDB.ConexionMongo()
    datos = BD[tabla]
    return datos

def perfil():
    if session["ROL"] == "administrador":
        titulo ="Informacion "+str(session["USER"])
        return render_template('PERFIL/perfil.html',titulo=titulo)

#CHECAR ESTO xd
def actualizarPerfil(request):
    if request.method == "POST" :
        try:
            datos = DataBase("admin")
            password = datos.update_one({'password': request.form['password']})    
            print(password)
        except Exception as e:
            print("ERROR AL ACTUALIZAR PASSWORD: "+str(e))