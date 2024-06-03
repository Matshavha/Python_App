from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from users.routes import users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def hello_world():
    return render_template('index.html', name='World')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f'Hello, {name}!'

app.register_blueprint(users)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
