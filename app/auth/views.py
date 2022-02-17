from flask import render_template,request,session, url_for,\
    redirect
from werkzeug.security import generate_password_hash,check_password_hash
from . import auth
from ..helpers import validate_inputs,is_logged_in
from .. import db
from ..models import User

@auth.route('/login',methods=['POST','GET'])
@is_logged_in
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('password')
        res = validate_inputs({'username': username, 'password': pwd})
        if res['status'] == 'no':
            return render_template('error.html',message='Some fields are empty !'),401
    
        # all fields are provided
        # check if username exists in db
        # if true: check if user hash match the hashed version of password provided
            # if true store user ij session and redirect him to home
        
        user = User.query.filter_by(username=username).first()

        if user:
            if  check_password_hash(user.hash,pwd):
                session['current_user'] = user.username
                return redirect(url_for('main.index'))
            else:
                return render_template('error.html',message='Password is incorrect!')
        else:
            return render_template('error.html',message='Username does not exists!')

    return render_template('auth/login.html')

@auth.route('/register',methods=['POST','GET'])
@is_logged_in
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('password')
        res = validate_inputs({'username': username, 'password': pwd})
        if res['status'] == 'no':
            return render_template('error.html',message='Some fields are empty !'),401
        
        # all fields are valid
        # store user in database
            # check if username already exists in databse
            # if not create new user in db
            # else redirect user to error page with message='Username already taken'
        # store user in session for later visit

        is_username_taken = User.query.filter_by(username=username).first()
        if not is_username_taken:
            user = User(username=username,hash=generate_password_hash(pwd))
            db.session.add(user)
            db.session.commit()
            session['current_user'] = user.username
            return redirect(url_for('main.index'))
        else:
            return render_template('error.html',message='Username is already taken!')

        
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))