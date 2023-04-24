from flask import request, jsonify

#exemplo de dicionario para criação de produto
produtos = {
      0:{
        "id": "exemplo",
        "nome": "",
        "preco":"" ,
        "peso": "",
        "descricao": "",
        "fornecedor": ""
        }
}

# função para gerar id de cada produto
def gerar_id():
    id = max(produtos.keys()) + 1
    return id

# função para criar um produto a aprtir de requisição post em json
def criar_produto():
    body = request.json
    produtos[gerar_id()] = body
    return jsonify(produtos)