import sqlite3
from banco.conexao import conectar

def inserir_no_banco(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (?, ?, ?)
        """,
        (nome, preco, quantidade))
    
    conexao.commit()
    conexao.close()

def lista_de_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    conexao.close()

    return produtos

def filtrar_produtos(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM PRODUTOS
        WHERE id = ?
    """,
    (id,))

    produto = cursor.fetchone()

    conexao.close()

    return produto
