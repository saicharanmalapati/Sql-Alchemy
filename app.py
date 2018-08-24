from flask import Flask, render_template, request, flash
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
db = SQLAlchemy(app)
app.secret_key = 'development key'


@app.route('/', methods=['GET'])
def index():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/signin', methods=['POST'])
def signin():

    email = request.form["email"]
    username = request.form["username"]
    return render_template('user.html', email=email, username=username)

if __name__ == '__main__':
    app.run()
