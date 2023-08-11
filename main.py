# Trabalho em grupo para a criação de rotas de uma API básica contendo os métodos GET, POST, PUT E DELETE 

# imports

from flask import Flask, jsonify, request
import repository

#

app = Flask(__name__)

# 1 retornar todos os produtos
@app.route('/', methods=['GET'])
def retornar_todos():
    print(repository.produtos[0])
    return repository.produtos


# 2 criar rota para retornar um produto específico por id  
@app.route('/product/<int:id>', methods=['GET'])
def buscar_por_id(id:int):
    for chave, valor in repository.produtos.items():
       if chave == id: 
        body = repository.produtos[id]
        #return jsonify(f'{chave} = {valores}')
        return jsonify(body)
    
    return jsonify({'Mensagem': "Produto não encontrado"})


# 3 criar rota de criação de produto
@app.route('/product', methods=['POST'])
def function_one():
    body = repository.criar_produto()
    return body


# 4 atualizar ou excluir um produto passando um id
@app.route('/product/<int:id>', methods=['PUT', 'DELETE'])
def atualiza_por_id(id:int):
    if request.method == "PUT":
        for chaves, valores in repository.produtos.items():
            if id == 0:
                return jsonify({'Mensagem': 'Produto de exemplo, não pode ser alterado!'})
            if chaves == id: 
                repository.produtos[id] = {
                                            'id': id,
                                            'nome': request.json["nome"],
                                            'preco': request.json["preco"],
                                            'peso': request.json["peso"],
                                            'descricao': request.json["descricao"],
                                            'fornecedor': request.json["fornecedor"]
                                          }
                return jsonify(repository.produtos[id])
        
        return jsonify({'Mensagem': "Produto não encontrado"})
    else:
        for chaves, valores in repository.produtos.items():
            if id == 0:
                return jsonify({'Mensagem': "Produto de exemplo, não pode ser apagado!"})
            elif chaves == id: 
                body = repository.produtos[id]
                repository.produtos.pop(chaves) 
                return jsonify("produto apagado", body) 
        return jsonify({'Mensagem': "Produto não encontrado"})

app.run(debug=True)