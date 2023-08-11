from flask import Flask, jsonify, request, json
import sqlite3
import os

import repository_com_bd

app = Flask(__name__)

#Criar um novo produto no banco
#nome, preco, peso, descricao, fornecedor
@app.route('/product', methods=['POST'])
def criar_produto():
    try:
        produto = repository_com_bd.criando_produto()
        
        return jsonify(produto), 201
    except Exception as ex:
        print(ex)
        return 0
    
#Retorna todos os produtos
@app.route('/', methods=['GET'])
def retornar_produtos():
    try:
        resultado = repository_com_bd.retornando_produtos()
        return resultado, 200
    except:
        return False 
    
#Retorna um único produto
@app.route('/product/<int:id>', methods=['GET'])
def retornar_produto(id:int):
    try:
        produto = repository_com_bd.retornando_produto(id)
        return produto, 200
    except:
        return jsonify({'Mensagem': "Produto não encontrado"}), 404
    
#Atualiza os dados de um produto
@app.route('/product/<int:id>', methods=['PUT'])
def atualizar_produto_id(id):
    try:
        produto = repository_com_bd.retornando_produto(id)
        if produto['id'] == id:
            dados_atualizados = request.json
            dados_atualizados["id"]=id
            repository_com_bd.atualizar_produto(**dados_atualizados)
            return jsonify(dados_atualizados), 200
    except Exception:
        return jsonify({'Mensagem': "Produto não encontrado"}), 404

#Deletando um produto
@app.route('/product/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        produto = repository_com_bd.retornando_produto(id)
        if produto:
            repository_com_bd.remover_produto(id)
            return jsonify({"Mensagem": "produto deletado com sucesso"}, produto)
    except Exception:
        return jsonify({"Mensagem": "Produto não encontrado"}), 404

# Instruções de como criar o banco e suas tabelas
# if __name__ == '__main__':
#     # Create the ‘products’ table if it doesn’t exist
#     conn.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, peso REAL, descricao TEXT, fornecedor TEXT)')


app.run(debug=True)