from flask import Flask, render_template, request, redirect, url_for, session, flash
from services.service import login as login_service


app = Flask(__name__)
app.secret_key  = 'super secret key'


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    res = login_service(username, password)
    if res.status_code == 200:
        return redirect(url_for('home'))
    else:
        flash('Usuario o contraseña incorrectos')
        return redirect(url_for('login'))
    
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)


