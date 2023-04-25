from flask import request, jsonify

#exemplo de dicionario para criação de produto com suas características
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

# função para criar um produto a aprtir de requisição post em json
def criar_produto():
    body = request.json
    produtos[gerar_id()] = body
    return jsonify(produtos)

# função para retornar um produto específico passando um id
# def buscar_por_id(id):
#     for produto in produtos:
#         if id == produtos[id]:
#             print(produtos[id])
            
#             return jsonify(id)
#         return jsonify({'Mensagem': "Produto não encontrado"})

