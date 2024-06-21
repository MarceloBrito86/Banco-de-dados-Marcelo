import mysql.connector
from datetime import datetime

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="he182555@",
        database="CRM_MB"
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

def adicionar_interacao(cliente_id, data_interacao, tipo, descricao):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Interacoes (cliente_id, data_interacao, tipo, descricao) VALUES (%s, %s, %s, %s)"
    valores = (cliente_id, data_interacao, tipo, descricao)
    cursor.execute(sql, valores)
    conn.commit()
    print("Interação adicionada com sucesso!")
    cursor.close()
    conn.close()

def adicionar_oportunidade(cliente_id, descricao, valor, status, data_criacao):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Oportunidades (cliente_id, descricao, valor, status, data_criacao) VALUES (%s, %s, %s, %s, %s)"
    valores = (cliente_id, descricao, valor, status, data_criacao)
    cursor.execute(sql, valores)
    conn.commit()
    print("Oportunidade adicionada com sucesso!")
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

def listar_interacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Interacoes")
    interacoes = cursor.fetchall()
    for interacao in interacoes:
        print(interacao)
    cursor.close()
    conn.close()

def listar_oportunidades():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Oportunidades")
    oportunidades = cursor.fetchall()
    for oportunidade in oportunidades:
        print(oportunidade)
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

def atualizar_interacao(id, cliente_id, data_interacao, tipo, descricao):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Interacoes SET cliente_id = %s, data_interacao = %s, tipo = %s, descricao = %s WHERE id = %s"
    valores = (cliente_id, data_interacao, tipo, descricao, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Interação atualizada com sucesso!")
    cursor.close()
    conn.close()

def atualizar_oportunidade(id, cliente_id, descricao, valor, status, data_criacao):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Oportunidades SET cliente_id = %s, descricao = %s, valor = %s, status = %s, data_criacao = %s WHERE id = %s"
    valores = (cliente_id, descricao, valor, status, data_criacao, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Oportunidade atualizada com sucesso!")
    cursor.close()
    conn.close()

def menu():
    while True:
        print("\nSistema de CRM")
        print("1. Adicionar Cliente")
        print("2. Adicionar Interação")
        print("3. Adicionar Oportunidade")
        print("4. Listar Clientes")
        print("5. Listar Interações")
        print("6. Listar Oportunidades")
        print("7. Atualizar Cliente")
        print("8. Atualizar Interação")
        print("9. Atualizar Oportunidade")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("Telefone do cliente: ")
            endereco = input("Endereço do cliente: ")
            adicionar_cliente(nome, email, telefone, endereco)
        elif escolha == "2":
            cliente_id = input("ID do cliente: ")
            data_interacao = input("Data da interação (YYYY-MM-DD): ")
            tipo = input("Tipo de interação: ")
            descricao = input("Descrição da interação: ")
            adicionar_interacao(int(cliente_id), data_interacao, tipo, descricao)
        elif escolha == "3":
            cliente_id = input("ID do cliente: ")
            descricao = input("Descrição da oportunidade: ")
            valor = input("Valor da oportunidade: ")
            status = input("Status da oportunidade: ")
            data_criacao = input("Data de criação (YYYY-MM-DD): ")
            adicionar_oportunidade(int(cliente_id), descricao, float(valor), status, data_criacao)
        elif escolha == "4":
            listar_clientes()
        elif escolha == "5":
            listar_interacoes()
        elif escolha == "6":
            listar_oportunidades()
        elif escolha == "7":
            id = input("ID do cliente a ser atualizado: ")
            nome = input("Novo nome do cliente: ")
            email = input("Novo email do cliente: ")
            telefone = input("Novo telefone do cliente: ")
            endereco = input("Novo endereço do cliente: ")
            atualizar_cliente(int(id), nome, email, telefone, endereco)
        elif escolha == "8":
            id = input("ID da interação a ser atualizada: ")
            cliente_id = input("Novo ID do cliente: ")
            data_interacao = input("Nova data da interação (YYYY-MM-DD): ")
            tipo = input("Novo tipo de interação: ")
            descricao = input("Nova descrição da interação: ")
            atualizar_interacao(int(id), int(cliente_id), data_interacao, tipo, descricao)
        elif escolha == "9":
            id = input("ID da oportunidade a ser atualizada: ")
            cliente_id = input("Novo ID do cliente: ")
            descricao = input("Nova descrição da oportunidade: ")
            valor = input("Novo valor da oportunidade: ")
            status = input("Novo status da oportunidade: ")
            data_criacao = input("Nova data de criação (YYYY-MM-DD): ")
            atualizar_oportunidade(int(id), int(cliente_id), descricao, float(valor), status, data_criacao)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()