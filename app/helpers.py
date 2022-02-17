from flask import session,redirect,url_for
from functools import wraps

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('current_user'):
            return redirect(url_for('auth.login'))
        
        return fn(*args, **kwargs)

    return wrapper

def is_logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if session.get('current_user'):
            return redirect(url_for('main.index'))
        else:
            return fn(*args, **kwargs)
    return wrapper

def validate_inputs(inputs):
    status = 'ok'
    empty_fields = []
    for input in inputs:
        if not inputs[input].strip():
            status = 'no'
            empty_fields.append(input.capitalize())
            
    return dict(status=status,empty_fields=empty_fields)


