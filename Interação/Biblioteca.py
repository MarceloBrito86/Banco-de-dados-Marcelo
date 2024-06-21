import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="he182555@",
        database="Biblioteca"
    )

def adicionar_autor(nome, nacionalidade):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Autores (nome, nacionalidade) VALUES (%s, %s)"
    valores = (nome, nacionalidade)
    cursor.execute(sql, valores)
    conn.commit()
    print("Autor adicionado com sucesso!")
    cursor.close()
    conn.close()

def adicionar_livro(titulo, autor_id, ano_publicacao):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Livros (titulo, autor_id, ano_publicacao) VALUES (%s, %s, %s)"
    valores = (titulo, autor_id, ano_publicacao)
    cursor.execute(sql, valores)
    conn.commit()
    print("Livro adicionado com sucesso!")
    cursor.close()
    conn.close()

def listar_autores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Autores")
    autores = cursor.fetchall()
    for autor in autores:
        print(autor)
    cursor.close()
    conn.close()

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Livros")
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)
    cursor.close()
    conn.close()

def atualizar_autor(id, nome, nacionalidade):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Autores SET nome = %s, nacionalidade = %s WHERE id = %s"
    valores = (nome, nacionalidade, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Autor atualizado com sucesso!")
    cursor.close()
    conn.close()

def atualizar_livro(id, titulo, autor_id, ano_publicacao):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Livros SET titulo = %s, autor_id = %s, ano_publicacao = %s WHERE id = %s"
    valores = (titulo, autor_id, ano_publicacao, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Livro atualizado com sucesso!")
    cursor.close()
    conn.close()

def menu():
    while True:
        print("\nSistema de Biblioteca")
        print("1. Adicionar Autor")
        print("2. Adicionar Livro")
        print("3. Listar Autores")
        print("4. Listar Livros")
        print("5. Atualizar Autor")
        print("6. Atualizar Livro")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            adicionar_autor(nome, nacionalidade)
        elif escolha == "2":
            titulo = input("Título do livro: ")
            autor_id = input("ID do autor: ")
            ano_publicacao = input("Ano de publicação: ")
            adicionar_livro(titulo, int(autor_id), int(ano_publicacao))
        elif escolha == "3":
            listar_autores()
        elif escolha == "4":
            listar_livros()
        elif escolha == "5":
            id = input("ID do autor a ser atualizado: ")
            nome = input("Novo nome do autor: ")
            nacionalidade = input("Nova nacionalidade do autor: ")
            atualizar_autor(int(id), nome, nacionalidade)
        elif escolha == "6":
            id = input("ID do livro a ser atualizado: ")
            titulo = input("Novo título do livro: ")
            autor_id = input("Novo ID do autor: ")
            ano_publicacao = input("Novo ano de publicação: ")
            atualizar_livro(int(id), titulo, int(autor_id), int(ano_publicacao))
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()