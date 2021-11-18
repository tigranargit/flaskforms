from application import app 
from application.forms import DemoForm
from flask import render_template, request

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])

def home():
    message = ''
    form = DemoForm()
    if request.method == 'POST':
        firstname = form.first_name.data
        lastname = form.last_name.data
        if len(firstname) == 0 or len(lastname) == 0:
            message = "Please enter a first name and a last name"
        else:
            message = f'Thanks for registering, {firstname} {lastname}'
    return render_template('home.html', message = message, form = form)
