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

def filtrar_produtos_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM PRODUTOS
        WHERE nome LIKE ?
    """,
    (f"%{nome}%",))

    produto = cursor.fetchall()

    conexao.close()

    return produto

def filtrar_produtos_por_id(id):
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

def apagar_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM produtos WHERE id = ?    
    """,
    (id,))

    conexao.commit()
    conexao.close()

def atualizar_quantidade(id, quantidade_nova):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET quantidade = ?
    WHERE id = ?
                   """,
    (quantidade_nova, id))

    conexao.commit()
    conexao.close()
    