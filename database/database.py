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

def consulta_colecciones(key):
    try:    
        cliente = MongoClient(MONGO_URL,tlsCAfile=ca)
        base = cliente[key]
        return base   
        
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")
    
def informacion_colecciones(key):
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        base = client[key]
        return base
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")    


def ConsultaGeneral():#poner nombres mas especificos pero faciles y correspondientes a este archivo ejemplo, consulta_database() y respetas los mismo para todos ls nobre
    #es decir si empieza con mayuscula , minusculas etc
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        bases = client
    
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")  

    return bases           
 
