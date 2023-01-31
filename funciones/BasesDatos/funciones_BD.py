from database import database as mongoDB 
from flask import Flask, render_template, session, redirect, flash


BD = mongoDB.ConsultaGeneral()
COLECCIONES = mongoDB.ConexionMongo()

def bases():
    if session["ROL"] == "administrador":  
        titulo = "Bases de datos MongoDB"
        bases = BD.list_database_names()  
        print(bases)
        return render_template('BD/database.html',titulo=titulo,bases=bases)
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect('/login')
        
def bdcolecctions(key):
    if session["ROL"] == "administrador":    
        consulta = mongoDB.consulta_colecciones(key).list_collection_names()
        bd_menu = BD.list_database_names()
        return render_template('INFORMACION_BD/informacion_bd.html',consulta=consulta, bd_menu=bd_menu)
        


        
              

  
    