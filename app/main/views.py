from flask import session
from flask import render_template
from . import main
from ..helpers import login_required
from ..models import User,Note
from sqlalchemy import desc

@main.route('/')
@login_required
def index():
    # load nores here
    user = User.query.filter_by(username=session['current_user']).first()
    notes = user.notes.order_by(desc(Note.time_created)).all()
    return render_template('index.html',notes=notes)

