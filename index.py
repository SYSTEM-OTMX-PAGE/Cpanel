from flask import Flask
import funciones.Cpanel.funciones_Cpanel as Panel
import funciones.Login.funciones_login as Login
import funciones.BaseDatos.funciones_BD as DataBase
import os

app = Flask(__name__)
app.host = '0.0.0.0'
app.port = os.getenv('PORT')


#FUNCION HOMEPAGE
@app.route('/HOME')
def homePage():
    return Panel.home() 

#FUNCIONES DE BD
@app.route('/BASE-DATOS')
def BaseDatos():
    return DataBase.BD()

#FUNCIONES DE LOGIN
@app.route('/')
@app.route('/INICIAR-SESION')
def iniciarSesion():
    return Login.IniciarSesion()         


#ENDPOINT

if __name__ == '__main__':
    app.run(host=app.host, port=app.port, debug=True)    