# models.py


from app import db


class Produto(db.Model):

    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    preco = db.Column(db.String, nullable=False)

    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
