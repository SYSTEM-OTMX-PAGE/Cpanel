from database import database as mongoDB
from flask import Flask, render_template, session, redirect, flash

def perfil():
    if session["ROL"] == "administrador":
        titulo ="Informacion "+str(session["USER"])
        return render_template('PERFIL/perfil.html',titulo=titulo)

def actualizarPassword():
     return       