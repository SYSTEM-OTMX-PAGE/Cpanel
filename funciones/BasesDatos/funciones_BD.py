from database import database as mongoDB
from flask import Flask, render_template


BD = mongoDB.ConsultaGeneral()



def bases():
    titulo = "Bases de datos MongoDB"
    bases = BD.list_database_names()
    return render_template('BD/database.html',titulo=titulo,bases=bases)
        

  
    