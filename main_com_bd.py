from flask import Flask, jsonify, request, json
import sqlite3
import os

app = Flask(__name__)

caminho = f"{os.path.dirname(__file__)}\\db\\produtos.db"

#Função para gerar um novo id
def gerar_id():
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='produtos")
    next_id = cursor.fetchone()[0]
    return next_id + 1

#Criar um novo produto no banco
#nome, preco, peso, descricao, fornecedor
@app.route('/product', methods=['POST'])
def criar_produto():
    try:
        obj = request.json
        values = (obj['nome'], obj['preco'], obj['peso'], obj['descricao'], obj['fornecedor'])
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_insert = "INSERT INTO produtos (nome_produto, preco_produto, peso_produto, descricao_produto, fornecedor_produto) values (?, ?, ?, ?, ? )"
        cursor.execute(sql_insert, (values))
        produto_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify(obj)
    except Exception as ex:
        print(ex)
        return 0
    
#Retorna todos os produtos
@app.route('/', methods=['GET'])
def retornar_produtos():
    try:
        resultado = []
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos"
        cursor.execute(sql_select)
        produtos = cursor.fetchall()
        conn.close()
        for item in produtos:
            produtos = {
                         'id': item[0],
                         'nome': item[1],
                         'preco': item[2],
                         'peso': item[3],
                         'descricao': item[4],
                         'fornecedor': item[5]
                       }
            resultado.append(produtos)
        return resultado
    except:
        return False 
    
#Retorna um único produto
@app.route('/product/<int:id>', methods=['GET'])
def retornar_produto(id:int):
    try:
        if id == 0:
            return jsonify({'Mensagem': "Produto não encontrado"})
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        sql_select = "SELECT * FROM produtos WHERE id_produto = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, preco, peso, descricao, fornecedor = cursor.fetchone()
        conn.close()
        #prod = id, nome, preco, peso, descricao, fornecedor
        return {
                "id":id,
                "nome": nome,
                "preco": preco,
                "peso": peso,
                "descricao": descricao,
                "fornecedor": fornecedor
                }
    except:
        return False
    
#Atualiza os dados de um produto
def atualizar_produto(id:int, nome, preco, peso, descricao, fornecedor):
    try:
        #Tentar atualizar
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_update = "UPDATE produtos SET nome_produto = ?, preco_produto = ?, peso_produto = ?, descricao_produto = ?, fornecedor_produto = ? WHERE id_produto = ?"
        cursor.execute(sql_update, (nome, preco, peso, descricao, fornecedor, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
@app.route('/product/<int:id>', methods=['PUT'])
def atualizar_produto_id(id):
    produto = retornar_produto(id)
    if produto:
        dados_atualizados = request.json
        dados_atualizados["id"]=id
        atualizar_produto(**dados_atualizados)
        return jsonify(dados_atualizados)

    
#Remove um produto
def remover_produto(id:int):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_delete = "DELETE FROM produtos WHERE id_produto = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    
@app.route('/product/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = retornar_produto(id)
    if produto:
        remover_produto(id)
        return jsonify({"Mensagem": "produto deletado com sucesso"}, produto)
    else:
        return jsonify({"Mensagem": "Produto não encontrado"}), 404

app.run(debug=True)

# nome = "Apple Watch 8"
# preco = 8000.00
# peso = 0.2
# descricao = "Relógio inteligente Apple"
# fornecedor = "Apple"

# id = criar_produto(nome, preco, peso, descricao, fornecedor)
# print(id)
# print(retornar_produto(id))

# id, nome, preco, peso, descricao, fornecedor = retornar_produto(id)
# atualizar_produto(id, "Apple Watch 8 ULTRA", 10000.00, peso, descricao, fornecedor)

# print(retornar_produto(id))
# id, nome, preco, peso, descricao, fornecedor = retornar_produto(id)

# print(retornar_produtos())

# remover_produto(id)

# print(retornar_produtos())