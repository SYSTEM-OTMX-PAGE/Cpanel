from flask import render_template

def no_found(error):
    return render_template('SERVIDOR/404.html',title = "Pagina no encontrada"), 404
