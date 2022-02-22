# from flask import(Flask, url_for, request, render_template)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'working'

# @app.route('/login', methods=['POST', 'GET'])
# def login(username = None):
#     if request.method == 'POST':
#         return render_template('login.html')
#     elif request.method == 'GET' and not username:
#         return render_template('login.html')
#     elif request.method == 'GET' and username:
#         return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)

#import necessary library
import jinja2
from flask import (Flask, render_template, request, redirect, session)

#configuring application
app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return "Have a nice day!"


#creating route for login
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    print(request.method)
    if request.method == 'GET':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/dashboard')
    return render_template('template/login.html')



#run the app
if __name__ == '__main__':
    app.run(debug=True)