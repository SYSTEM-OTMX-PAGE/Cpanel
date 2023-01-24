from flask import render_template, session, flash, request, redirect

def IniciarSesion():
    titulo = 'Login Cpanel'
    return render_template('/index.html', titulo=titulo)