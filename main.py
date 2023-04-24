# Trabalho em grupo para a criação de rotas de uma API básica contendo os métodos GET, POST, PUT E DELETE 

# imports

from flask import Flask, jsonify, request
import repository

# 

app = Flask(__name__)

# criar rota de criação de produto
@app.route('/products', methods=['POST'])
def function_one():
    body = repository.criar_produto()
    return body

    





app.run(debug=True)