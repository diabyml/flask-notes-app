from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html',message='Page not found'),404


@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('error.html',message='Internal Server Error'),500