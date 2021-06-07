from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

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
    # return f'Hola {user_name}, tu IP es {user_ip}'
    return render_template('hello.html', user_ip=user_ip, user_name=user_name)