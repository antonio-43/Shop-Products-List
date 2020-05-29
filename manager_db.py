import sqlite3 as sq


def add():
    conn = sq.connect("data.db")
    c = conn.cursor()
    
    prod_name = input("Nome do Produto: ")
    quantidade = int(input("Quantidade: "))

    c.execute("""
    ISERT INTO produtos (name, much) VALUES (
    (?, ?)
    ), (prod_name, quantidade)
    """)

