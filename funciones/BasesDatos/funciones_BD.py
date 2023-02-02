from database import database as mongoDB 
from flask import Flask, render_template, session, redirect, flash

PRUEBA = mongoDB.ConexionMongo()

def Bases():
    if session["ROL"] == "administrador":  
        titulo = "Bases de datos MongoDB"
        bases = mongoDB.ConsultaGeneralBases().list_database_names()  
        return render_template('BD/database.html',titulo=titulo,bases=bases)
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect('/login')
        
def bdColecctions(key):
    if session["ROL"] == "administrador":    
        consulta = mongoDB.ConsultaColecciones(key).list_collection_names()
        bd_menu = mongoDB.ConsultaGeneralBases().list_database_names() 
        return render_template('INFORMACION_BD/informacion_bd.html',consulta=consulta, bd_menu=bd_menu)
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect('/login')

#REVISAR ESTO PORQUE UN NO FUNCIONA :C
def CollectionsInfo(key):
   documentos = mongoDB.DocumentosColecciones(key)
  
   return key
    

    
    
    


        
              

  
    