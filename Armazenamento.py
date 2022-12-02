from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from credenciais import segredos

app = Flask(__name__)
app.secret_key = 'alura'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "{mysql}://{usuario}:{senha}@{servidor}/{database}".format(
        mysql = segredos.get('mysql'),
        usuario = segredos.get('usuario'),
        senha = segredos.get('senha'),
        servidor = segredos.get('servidor'),
        database = segredos.get('database')
    )
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False )
    email = db.Column(db.String(40), nullable=False )
    subject = db.Column(db.String(40), nullable=False )
    message = db.Column(db.String(300), nullable=False )

    def __repr__(self):
        return '<Id %r>' % self.id

class Users(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False )
    email = db.Column(db.String(40), nullable=False, unique=True )
    username = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False )

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/criarContato')
def criarContato():
    nome = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    contato = (nome, email, subject, message)

@app.route('/prices')
def prices_page():
    return render_template('prices.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form[''] == request.form['psw']:
        session['usuario_logado'] = request.form['usuario']
        return redirect('/') #adicionar pagina dashboard
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
