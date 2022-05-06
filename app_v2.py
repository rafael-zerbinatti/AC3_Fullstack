# app.py


from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        preco = request.form['preco']
        produto = Produto(nome, categoria, preco)
        db.session.add(produto)
        db.session.commit()
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)


if __name__ == '__main__':
    app.run()
