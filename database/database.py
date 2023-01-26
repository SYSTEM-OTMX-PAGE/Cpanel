from pymongo import MongoClient 
import certifi 

MONGO_URL = 'mongodb+srv://SYSTEM-OTMX:Cop07234MON@propsito-general.bzeyl6z.mongodb.net/?retryWrites=true&w=majority'

ca=certifi.where()

def ConexionMongo():
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        base_datos = client["CPANEL"]
        
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")
    
    return base_datos       

def ConsultaGeneral():
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        bases = client
        bases.list_database_names()
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")         
 
