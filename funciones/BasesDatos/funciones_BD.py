from database import database as mongoDB
from flask import flash, redirect, session

def DataBase(tabla):
    BD = mongoDB.ConsultaGeneral()
    datos = BD[tabla]
    return datos

    