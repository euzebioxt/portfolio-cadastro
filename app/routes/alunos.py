from main import app, db
from flask import render_template, request, redirect, url_for
from models.aluno import Aluno


# ----------- rota teste / home -----------
@app.route('/')
def home():
    return render_template('index.html')


# ----------- cadastrar aluno -----------
@app.route('/cadastrar-aluno', methods=['GET', 'POST'])
def cadastrar_aluno():

    if request.method == 'POST':

        nome = request.form['nome']
        idade = request.form['idade']
        serie = request.form['serie']

        aluno = Aluno(
            nome=nome,
            idade=idade,
            serie=serie
        )

        db.session.add(aluno)
        db.session.commit()

        return redirect(url_for('listar_alunos'))

    return render_template('cadastrar_aluno.html')


# ----------- listar alunos -----------
@app.route('/alunos')
def listar_alunos():

    alunos = Aluno.query.all()

    return render_template('alunos.html', alunos=alunos)


# ----------- deletar aluno -----------
@app.route('/deletar-aluno/<int:id>')
def deletar_aluno(id):

    aluno = Aluno.query.get(id)

    db.session.delete(aluno)
    db.session.commit()

    return redirect(url_for('listar_alunos'))


# ----------- editar aluno -----------
@app.route('/editar-aluno/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):

    aluno = Aluno.query.get(id)

    if request.method == 'POST':

        aluno.nome = request.form['nome']
        aluno.idade = request.form['idade']
        aluno.serie = request.form['serie']

        db.session.commit()

        return redirect(url_for('listar_alunos'))

    return render_template('editar_aluno.html', aluno=aluno)