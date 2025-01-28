from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    data_nascimento = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(200), nullable=True)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    sexo = db.Column(db.String(5), nullable=True)
