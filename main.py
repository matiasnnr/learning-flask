from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Comprar café', 'Solicitud de compra', 'todo 3', 'todo 4']

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
    response.set_cookie('user_ip', user_ip)
    response.set_cookie('user_name', 'Matías')

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    user_name = request.cookies.get('user_name')

    context = {
        'user_ip': user_ip, 
        'user_name': user_name, 
        'todos': todos
    }
    # return f'Hola {user_name}, tu IP es {user_ip}'
    # **context hace que expanda y exponga todas las variables y no sea necesario usar contenxt.user_ip por ejemplo, simplemente llamamos a user_ip
    return render_template('hello.html', **context)