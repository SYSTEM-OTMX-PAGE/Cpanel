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
    try:    
        cliente = MongoClient(MONGO_URL,tlsCAfile=ca)
        base = cliente[key]  
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")
    return base     
    
def DocumentosColecciones(key):#MUESTRA LOS DOCUMENTOS QUE CONTIENE LA COLECCION SELECCIONADA
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        base = client[key]
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")    
    return base

def ConsultaGeneralBases():#ESTO MUESTRA TODAS LAS BD DEL CLUSTER DE MONGO
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        bases = client
    except ConnectionError:
        print("ERROR EN LA BASE DE DATOS")  
    return bases           
 
