from database import database as mongoDB 
from flask import Flask, render_template, session, redirect, flash, jsonify


def Bases():
    if session["ROL"] == "administrador":  
        titulo = "Bases de datos MongoDB"
        bases = mongoDB.Conexion().list_database_names()  
        return render_template('BD/database.html',titulo=titulo,bases=bases)
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect('/login')
        
def bdColecctions(key):
    if session["ROL"] == "administrador":    
        consulta = mongoDB.ConsultaColecciones(key).list_collection_names()
        bd_menu = mongoDB.Conexion().list_database_names() 
        return render_template('INFORMACION_BD/informacion_bd.html',consulta=consulta, bd_menu=bd_menu,nameDataBase=key)
    else:
        flash("POR FAVOR INICIA SESION")
        return redirect('/login')

def titulosC(coleccion):
    titulos =[]
    for dato in coleccion:
        titulo = list(dato.keys())
        break
    return titulo

def eliminarColeccion(database,coleccion):
    try:
        mongoDB.Conexion()[database][coleccion].drop()
        return redirect('/bases_colecciones/'+ database)
    except Exception as e:
        pass
def datosColeccion(nameDataBase, colection):
    consulta = mongoDB.Conexion()[nameDataBase][colection].find()
    datos =[]
    titulos= []
    titulos = titulosC(mongoDB.Conexion()[nameDataBase][colection].find())
    for dato in consulta:
        datos.append(list(dato.values()))
  
    bd_menu = mongoDB.Conexion().list_database_names()    
    return render_template('/INFORMACION_BD/informacion_coleccion.html',consulta=consulta,bd_menu=bd_menu,titulos = titulos,data=datos,coleccion=colection,database=nameDataBase)

    
    

    
           
        
    

    
    
    


        
              

  
    