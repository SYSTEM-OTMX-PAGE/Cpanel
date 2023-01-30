from database import database as mongoDB
from flask import Flask, render_template, session, redirect, flash


BD = mongoDB.ConsultaGeneral()

def bases():
    if session["ROL"] == "administrador":  
        titulo = "Bases de datos MongoDB"
        bases = BD.list_database_names()  
        return render_template('BD/database.html',titulo=titulo,bases=bases)
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect('/login')

        
              

  
    