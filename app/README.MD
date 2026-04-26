# Sistema de Cadastro de Alunos (Flask)

Projeto simples desenvolvido em **Python + Flask** para gerenciamento de alunos de uma sala de aula.

## Funcionalidades

* Cadastrar alunos
* Listar alunos
* Editar alunos
* Deletar alunos

O sistema utiliza **SQLite** para armazenamento de dados e **SQLAlchemy** como ORM.

## Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML5
* Jinja2

## Estrutura do projeto

```
app/
 ├─ models/
 │   └─ aluno.py
 │
 ├─ routes/
 │   └─ alunos.py
 │
 ├─ templates/
 │   ├─ alunos.html
 │   ├─ cadastrar_aluno.html
 │   └─ editar_aluno.html
 │
 ├─ static/
 │
 ├─ config.py
 └─ main.py

database.db
requirements.txt
README.md
```

## Instalação

Clone o repositório:

```
git clone https://github.com/seuusuario/seuprojeto.git
```

Entre na pasta:

```
cd seuprojeto
```

Crie ambiente virtual:

```
python -m venv venv
```

Ative o ambiente virtual:

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

Instale dependências:

```
pip install -r requirements.txt
```

Execute o projeto:

```
python app/main.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

## Autor

Euzebio Silva
