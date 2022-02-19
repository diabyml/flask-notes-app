from flask import render_template,request,session,redirect,url_for
from . import note
from ..helpers import validate_inputs,login_required
from .. import db
from ..models import User,Note
from .. import db

@note.route('/note/add',methods=['POST','GET'])
@login_required
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        res = validate_inputs({title: description, description: description})
        if res['status'] == 'no':
            return render_template('error.html',message='Some fields are empty'),401
        
        # fields are valid
        # store note in db and redirect user to home
            # get current_user and associate it with the newly created note
        user = User.query.filter_by(username=session['current_user']).first()
        note = Note(title=title,description=description,user=user)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('note/add-note.html')

@note.route('/note/edit-note/<note_id>',methods=['POST','GET'])
def edit_note(note_id):
    note = Note.query.filter_by(id=note_id).first()

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        res = validate_inputs({title: description, description: description})
        if res['status'] == 'no':
            return render_template('error.html',message='Some fields are empty'),401
        
        # fields are valid
        note.title = title
        note.description = description
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('note/edit-note.html',note=note)

@note.route('/note/delete/<note_id>')
def delete(note_id):
    note_to_delete = Note.query.filter_by(id=note_id).first()
    db.session.delete(note_to_delete)
    db.session.commit()
    return redirect(url_for('main.index'))

@note.route('/note/<note_id>')
def view(note_id):
    note = Note.query.filter_by(id=note_id).first()
    return render_template('/note/view.html', note=note)