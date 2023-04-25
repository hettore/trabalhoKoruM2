# Trabalho em grupo para a criação de rotas de uma API básica contendo os métodos GET, POST, PUT E DELETE 

# imports

from flask import Flask, jsonify, request
import repository

# 

app = Flask(__name__)

# 1 retornar todos os produtos
@app.route('/', methods=['GET'])
def retornar_todos():
    print(repository.produtos)
    return repository.produtos


# 2 criar rota para retornar um produto específico por id  
@app.route('/products/<int:id>', methods=['GET'])
def buscar_por_id(id:int):
    for chaves, valores in repository.produtos.items():
       if chaves == id: 
        return jsonify(f'{chaves} = {valores}')
    
    return jsonify({'Mensagem': "Produto não encontrado"})


# 3 criar rota de criação de produto
@app.route('/products', methods=['POST'])
def function_one():
    body = repository.criar_produto()
    return body


# 4 atualizar um produto com o id passado






app.run(debug=True)