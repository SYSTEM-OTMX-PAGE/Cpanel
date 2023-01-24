from flask import render_template
from data_base import database as mongodb

DB = mongodb.dbConecction()


def BD():
    titulo = 'BASES DE DATOS'
    bases = DB
    basesTot = bases.list_database_names()
    return render_template('/BD/database.html',titulo=titulo,menu=basesTot)

def MenuBases():
    
    return render_template('/BD/modulos/menu.html')    
