from flask import Flask
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# importar models
from models.aluno import *

# criar banco automaticamente
with app.app_context():
    db.create_all()

# importar rotas
from routes.alunos import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)