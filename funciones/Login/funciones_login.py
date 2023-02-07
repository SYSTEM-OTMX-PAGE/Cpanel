from database import database as mongoDB
from flask import flash, redirect, session
from werkzeug.security import check_password_hash

def DataBase(tabla):
    BD = mongoDB.ConexionMongo()
    datos = BD[tabla]
    return datos

def login(request):
    if request.method == 'POST':
        try:
            datos = DataBase("admin")
            usuario = datos.find_one({'email':request.form['email']})
            if(usuario is None):
                flash("NO EXISTE EL USUARIO")   
                return redirect('/')
            else:
                if(check_password_hash(usuario["password"],request.form["password"]) == True):
                    session["USER"] = usuario["email"]
                    session["ROL"] = "administrador"
                    flash("BIENVENIDO: "+session["USER"])
                    return redirect('/cpanel')      
                elif(check_password_hash(usuario["password"],request.form["password"]) == False):
                    flash("ERROR EN LA CONTRASEÑA")
                    return redirect('/')    
        except Exception as e:
            flash("ERROR EN EL SERVIDOR: " +str(e))
            return redirect('/')

