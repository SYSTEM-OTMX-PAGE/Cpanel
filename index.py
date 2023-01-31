from flask import Flask
from routes.login import login_routes
from routes.Mongo import Mongo_routes
from routes.perfil import Perfil_routes

import os


app = Flask(__name__)
app.host = '0.0.0.0'
app.port = os.getenv('PORT')
app.secret_key = b'\xd4\x8a\xa7\x9f\xf39i\x17|>\xad\xa6R]\xc0W\xc8\xa3M\x852\xa34>'

app.register_blueprint(login_routes)
app.register_blueprint(Mongo_routes)
app.register_blueprint(Perfil_routes)
#podrias hacer routeas y funciones para servidor ejemplos funcon de renderrozar el error 404, mensajes de registro correcto, etc






# ENDPOINT

if __name__ == '__main__':
    #te falta redireccion del error 404,
    app.run(host=app.host, port=app.port, debug=True)
