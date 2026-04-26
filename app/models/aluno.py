from database import db

class Aluno(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)

    idade = db.Column(db.Integer)

    serie = db.Column(db.String(50))