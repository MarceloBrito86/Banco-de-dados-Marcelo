import mysql.connector
from datetime import datetime

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="he182555@",
        database="Ecommerce_MB"
    )

def adicionar_cliente(nome, email, telefone, endereco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)"
    valores = (nome, email, telefone, endereco)
    cursor.execute(sql, valores)
    conn.commit()
    print("Cliente adicionado com sucesso!")
    cursor.close()
    conn.close()

def adicionar_produto(nome, descricao, preco, estoque):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)"
    valores = (nome, descricao, preco, estoque)
    cursor.execute(sql, valores)
    conn.commit()
    print("Produto adicionado com sucesso!")
    cursor.close()
    conn.close()

def adicionar_pedido(cliente_id, data_pedido, status):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Pedidos (cliente_id, data_pedido, status) VALUES (%s, %s, %s)"
    valores = (cliente_id, data_pedido, status)
    cursor.execute(sql, valores)
    conn.commit()
    print("Pedido adicionado com sucesso!")
    cursor.close()
    conn.close()

def adicionar_item_pedido(pedido_id, produto_id, quantidade, preco_unitario):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO ItensPedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
    valores = (pedido_id, produto_id, quantidade, preco_unitario)
    cursor.execute(sql, valores)
    conn.commit()
    print("Item do pedido adicionado com sucesso!")
    cursor.close()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    cursor.close()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
    cursor.close()
    conn.close()

def listar_pedidos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedidos")
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        print(pedido)
    cursor.close()
    conn.close()

def listar_itens_pedido():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ItensPedido")
    itens = cursor.fetchall()
    for item in itens:
        print(item)
    cursor.close()
    conn.close()

def atualizar_cliente(id, nome, email, telefone, endereco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Clientes SET nome = %s, email = %s, telefone = %s, endereco = %s WHERE id = %s"
    valores = (nome, email, telefone, endereco, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Cliente atualizado com sucesso!")
    cursor.close()
    conn.close()

def atualizar_produto(id, nome, descricao, preco, estoque):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Produtos SET nome = %s, descricao = %s, preco = %s, estoque = %s WHERE id = %s"
    valores = (nome, descricao, preco, estoque, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Produto atualizado com sucesso!")
    cursor.close()
    conn.close()

def atualizar_pedido(id, cliente_id, data_pedido, status):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Pedidos SET cliente_id = %s, data_pedido = %s, status = %s WHERE id = %s"
    valores = (cliente_id, data_pedido, status, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Pedido atualizado com sucesso!")
    cursor.close()
    conn.close()

def atualizar_item_pedido(id, pedido_id, produto_id, quantidade, preco_unitario):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE ItensPedido SET pedido_id = %s, produto_id = %s, quantidade = %s, preco_unitario = %s WHERE id = %s"
    valores = (pedido_id, produto_id, quantidade, preco_unitario, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Item do pedido atualizado com sucesso!")
    cursor.close()
    conn.close()

def menu():
    while True:
        print("\nSistema de E-commerce")
        print("1. Adicionar Cliente")
        print("2. Adicionar Produto")
        print("3. Adicionar Pedido")
        print("4. Adicionar Item do Pedido")
        print("5. Listar Clientes")
        print("6. Listar Produtos")
        print("7. Listar Pedidos")
        print("8. Listar Itens do Pedido")
        print("9. Atualizar Cliente")
        print("10. Atualizar Produto")
        print("11. Atualizar Pedido")
        print("12. Atualizar Item do Pedido")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("Telefone do cliente: ")
            endereco = input("Endereço do cliente: ")
            adicionar_cliente(nome, email, telefone, endereco)
        elif escolha == "2":
            nome = input("Nome do produto: ")
            descricao = input("Descrição do produto: ")
            preco = input("Preço do produto: ")
            estoque = input("Estoque do produto: ")
            adicionar_produto(nome, descricao, float(preco), int(estoque))
        elif escolha == "3":
            cliente_id = input("ID do cliente: ")
            data_pedido = input("Data do pedido (YYYY-MM-DD): ")
            status = input("Status do pedido: ")
            adicionar_pedido(int(cliente_id), data_pedido, status)
        elif escolha == "4":
            pedido_id = input("ID do pedido: ")
            produto_id = input("ID do produto: ")
            quantidade = input("Quantidade: ")
            preco_unitario = input("Preço unitário: ")
            adicionar_item_pedido(int(pedido_id), int(produto_id), int(quantidade), float(preco_unitario))
        elif escolha == "5":
            listar_clientes()
        elif escolha == "6":
            listar_produtos()
        elif escolha == "7":
            listar_pedidos()
        elif escolha == "8":
            listar_itens_pedido()
        elif escolha == "9":
            id = input("ID do cliente a ser atualizado: ")
            nome = input("Novo nome do cliente: ")
            email = input("Novo email do cliente: ")
            telefone = input("Novo telefone do cliente: ")
            endereco = input("Novo endereço do cliente: ")
            atualizar_cliente(int(id), nome, email, telefone, endereco)
        elif escolha == "10":
            id = input("ID do produto a ser atualizado: ")
            nome = input("Novo nome do produto: ")
            descricao = input("Nova descrição do produto: ")
            preco = input("Novo preço do produto: ")
            estoque = input("Novo estoque do produto: ")
            atualizar_produto(int(id), nome, descricao, float(preco), int(estoque))
        elif escolha == "11":
            id = input("ID do pedido a ser atualizado: ")
            cliente_id = input("Novo ID do cliente: ")
            data_pedido = input("Nova data do pedido (YYYY-MM-DD): ")
            status = input("Novo status do pedido: ")
            atualizar_pedido(int(id), int(cliente_id), data_pedido, status)
        elif escolha == "12":
            id = input("ID do item do pedido a ser atualizado: ")
            pedido_id = input("Novo ID do pedido: ")
            produto_id = input("Novo ID do produto: ")
            quantidade = input("Nova quantidade: ")
            preco_unitario = input("Novo preço unitário: ")
            atualizar_item_pedido(int(id), int(pedido_id), int(produto_id), int(quantidade), float(preco_unitario))
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()