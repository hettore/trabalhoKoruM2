from flask import request, jsonify

#exemplo de dicionário para criação de produto com suas características
produtos = {
      0:{
        "id": "exemplo",
        "nome": "exemplo",
        "preco":"00" ,
        "peso": "00",
        "descricao": "Exemplo de um produto",
        "fornecedor": "exemplo"
        }
}

# função para gerar id de cada produto
def gerar_id():
    id = max(produtos.keys()) + 1
    return id

# função para criar um produto a a partir de requisição post em json
def criar_produto():
    body = request.json
    id = gerar_id()
    produtos[id] = {
        'id': id,
        'nome': request.json["nome"],
        'preco': request.json["preco"],
        'peso': request.json["peso"],
        'descricao': request.json["descricao"],
        'fornecedor': request.json["fornecedor"]
    }
    return jsonify(produtos)



