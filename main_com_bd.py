import sqlite3
import os

caminho = f"{os.path.dirname(__file__)}\\db\\produtos.db"

#Função para gerar um novo id
def gerar_id():
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='personagens")
    next_id = cursor.fetchone()[0]
    return next_id + 1

#Criar um novo produto no banco
def criar_produto(nome, preco, peso, descricao, fornecedor):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_insert = "INSERT INTO produtos (nome_produto, preco_produto, peso_produto, descricao_produto, fornecedor_produto) values (?, ?, ?, ?, ? )"
        cursor.execute(sql_insert, (nome, preco, peso, descricao, fornecedor))
        produto_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return produto_id
    except Exception as ex:
        print(ex)
        return 0
    
#Retorna todos os produtos
def retornar_produtos():
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos"
        cursor.execute(sql_select)
        produtos = cursor.fetchall()
        conn.close()
        return produtos
    except:
        return False 
    
#Retorna um único produto
def retornar_produto(id:int):
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", ""
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        sql_select = "SELECT * FROM produtos WHERE id_produto = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, preco, peso, descricao, fornecedor = cursor.fetchone()
        conn.close()
        return id, nome, preco, peso, descricao, fornecedor
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

nome = "Apple Watch 8"
preco = 8000.00
peso = 0.2
descricao = "Relógio inteligente Apple"
fornecedor = "Apple"

id = criar_produto(nome, preco, peso, descricao, fornecedor)
print(id)
print(retornar_produto(id))

id, nome, preco, peso, descricao, fornecedor = retornar_produto(id)
atualizar_produto(id, "Apple Watch 8 ULTRA", 10000.00, peso, descricao, fornecedor)

print(retornar_produto(id))
id, nome, preco, peso, descricao, fornecedor = retornar_produto(id)

print(retornar_produtos())

remover_produto(id)

print(retornar_produtos())