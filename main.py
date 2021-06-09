from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar café', 'Solicitud de compra', 'todo 3', 'todo 4']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('hello'))
    # response.set_cookie('user_ip', user_ip)
    # response.set_cookie('user_name', 'Matías')
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    # user_name = request.cookies.get('user_name')
    username = session.get('username')
    login_form = LoginForm()

    context = {
        'user_ip': user_ip, 
        'username': username, 
        'todos': todos,
        'login_form': login_form
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con éxito')

        return redirect(url_for('index'))
    # return f'Hola {user_name}, tu IP es {user_ip}'
    # **context hace que expanda y exponga todas las variables y no sea necesario usar contenxt.user_ip por ejemplo, simplemente llamamos a user_ip
    return render_template('hello.html', **context)