# app.py

import os
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
        post_nome = Produto(nome)
        post_categoria = Produto(categoria)
        post_preco = Produto(preco)
        db.session.add(post_nome, post_categoria, post_preco)
        db.session.commit()
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)

