from atexit import register
from flask import (Flask, render_template, request, redirect, session)

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
    return "<h1>WELCOME</h1>"

@app.route('/register')
def home():
    form = RegistrationForm()
    return render_template('register.html', title = register)


