from flask import render_template

def home():
    titulo = 'SYSTEM PANEL'
    return render_template('/CPANEL/home.html',titulo=titulo)