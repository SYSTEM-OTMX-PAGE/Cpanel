from pymongo import MongoClient #importamos mongo para la base de datos
import certifi #importamos certifi para que sea segura la conexion de base de datos

MONGO_URL = 'mongodb+srv://SYSTEM-OTMX:Cop07234MON@propsito-general.bzeyl6z.mongodb.net/?retryWrites=true&w=majority'

ca=certifi.where()
def dbConecction():
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        db=client
        print(client.list_database_names())
    except ConnectionError:
        print("Error en la bd")
    return db        
    
