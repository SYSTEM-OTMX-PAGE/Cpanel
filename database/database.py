from pymongo import MongoClient 
import certifi 

MONGO_URL = 'mongodb+srv://SYSTEM-OTMX:Cop07234MON@propsito-general.bzeyl6z.mongodb.net/?retryWrites=true&w=majority'

ca=certifi.where()

def ConexionMongo():#AQUI ES DONDE SE GUARDAN LAS CREDENCIALES DE LOS USUARIOS
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        base_datos = client["CPANEL"]     
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")
    return base_datos       

def ConsultaColecciones(key):#MUESTRA LAS COLECCIONES DE LA BD SELECCIONADO POR EL USUARIO
        base = Conexion()[key]     
        return base     

def Conexion(): #CONSULTA GENERAL DE BDS
    try:
        client = MongoClient(MONGO_URL, tlsCAfile=ca)
        return client
    except ConnectionError:
        print("ERROR xd")
        return client