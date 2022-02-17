from flask import render_template
from . import main
from ..helpers import login_required

@main.route('/')
@login_required
def index():
    return render_template('index.html')
