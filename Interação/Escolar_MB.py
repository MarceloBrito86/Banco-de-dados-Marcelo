import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

# Função para conectar ao banco de dados
def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="Escolar_MB"
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erro: Acesso negado. Verifique seu nome de usuário e senha.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Erro: Banco de dados não existe.")
        else:
            print(err)

# Função para adicionar um novo aluno
def adicionar_aluno(nome, data_nascimento, endereco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Alunos (nome, data_nascimento, endereco) VALUES (%s, %s, %s)"
    valores = (nome, data_nascimento, endereco)
    cursor.execute(sql, valores)
    conn.commit()
    print("Aluno adicionado com sucesso!")
    cursor.close()
    conn.close()

# Função para adicionar uma nova disciplina
def adicionar_disciplina(nome, professor):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Disciplinas (nome, professor) VALUES (%s, %s)"
    valores = (nome, professor)
    cursor.execute(sql, valores)
    conn.commit()
    print("Disciplina adicionada com sucesso!")
    cursor.close()
    conn.close()

# Função para adicionar uma nova matrícula
def adicionar_matricula(aluno_id, disciplina_id, ano_letivo):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Matriculas (aluno_id, disciplina_id, ano_letivo) VALUES (%s, %s, %s)"
    valores = (aluno_id, disciplina_id, ano_letivo)
    cursor.execute(sql, valores)
    conn.commit()
    print("Matrícula adicionada com sucesso!")
    cursor.close()
    conn.close()

# Função para listar todos os alunos
def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)
    cursor.close()
    conn.close()

# Função para listar todas as disciplinas
def listar_disciplinas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Disciplinas")
    disciplinas = cursor.fetchall()
    for disciplina in disciplinas:
        print(disciplina)
    cursor.close()
    conn.close()

# Função para listar todas as matrículas
def listar_matriculas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Matriculas")
    matriculas = cursor.fetchall()
    for matricula in matriculas:
        print(matricula)
    cursor.close()
    conn.close()

# Função para atualizar informações de um aluno
def atualizar_aluno(id, nome, data_nascimento, endereco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Alunos SET nome = %s, data_nascimento = %s, endereco = %s WHERE id = %s"
    valores = (nome, data_nascimento, endereco, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Informações do aluno atualizadas com sucesso!")
    cursor.close()
    conn.close()

# Função para atualizar informações de uma disciplina
def atualizar_disciplina(id, nome, professor):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Disciplinas SET nome = %s, professor = %s WHERE id = %s"
    valores = (nome, professor, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Informações da disciplina atualizadas com sucesso!")
    cursor.close()
    conn.close()

# Função para atualizar informações de uma matrícula
def atualizar_matricula(id, aluno_id, disciplina_id, ano_letivo):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE Matriculas SET aluno_id = %s, disciplina_id = %s, ano_letivo = %s WHERE id = %s"
    valores = (aluno_id, disciplina_id, ano_letivo, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Informações da matrícula atualizadas com sucesso!")
    cursor.close()
    conn.close()

# Função para excluir um aluno
def excluir_aluno(id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM Alunos WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Aluno excluído com sucesso!")
    cursor.close()
    conn.close()

# Função para excluir uma disciplina
def excluir_disciplina(id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM Disciplinas WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Disciplina excluída com sucesso!")
    cursor.close()
    conn.close()

# Função para excluir uma matrícula
def excluir_matricula(id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM Matriculas WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Matrícula excluída com sucesso!")
    cursor.close()
    conn.close()

# Menu interativo
def menu():
    while True:
        print("\nSistema Escolar")
        print("1. Adicionar Aluno")
        print("2. Adicionar Disciplina")
        print("3. Adicionar Matrícula")
        print("4. Listar Alunos")
        print("5. Listar Disciplinas")
        print("6. Listar Matrículas")
        print("7. Atualizar Aluno")
        print("8. Atualizar Disciplina")
        print("9. Atualizar Matrícula")
        print("10. Excluir Aluno")
        print("11. Excluir Disciplina")
        print("12. Excluir Matrícula")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do aluno: ")
            data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            endereco = input("Endereço do aluno: ")
            adicionar_aluno(nome, data_nascimento, endereco)
        elif escolha == "2":
            nome = input("Nome da disciplina: ")
            professor = input("Nome do professor: ")
            adicionar_disciplina(nome, professor)
        elif escolha == "3":
            listar_alunos()
            aluno_id = input("ID do aluno: ")
            listar_disciplinas()
            disciplina_id = input("ID da disciplina: ")
            ano_letivo = input("Ano letivo: ")
            adicionar_matricula(int(aluno_id), int(disciplina_id), int(ano_letivo))
        elif escolha == "4":
            listar_alunos()
        elif escolha == "5":
            listar_disciplinas()
        elif escolha == "6":
            listar_matriculas()
        elif escolha == "7":
            listar_alunos()
            id = input("ID do aluno a ser atualizado: ")
            nome = input("Novo nome do aluno: ")
            data_nascimento = input("Nova data de nascimento (YYYY-MM-DD): ")
            endereco = input("Novo endereço do aluno: ")
            atualizar_aluno(int(id), nome, data_nascimento, endereco)
        elif escolha == "8":
            listar_disciplinas()
            id = input("ID da disciplina a ser atualizada: ")
            nome = input("Novo nome da disciplina: ")
            professor = input("Novo nome do professor: ")
            atualizar_disciplina(int(id), nome, professor)
        elif escolha == "9":
            listar_matriculas()
            id = input("ID da matrícula a ser atualizada: ")
            listar_alunos()
            aluno_id = input("Novo ID do aluno: ")
            listar_disciplinas()
            disciplina_id = input("Novo ID da disciplina: ")
            ano_letivo = input("Novo ano letivo: ")
            atualizar_matricula(int(id), int(aluno_id), int(disciplina_id), int(ano_letivo))
        elif escolha == "10":
            listar_alunos()
            id = input("ID do aluno a ser excluído: ")
            excluir_aluno(int(id))
        elif escolha == "11":
            listar_disciplinas()
            id = input("ID da disciplina a ser excluída: ")
            excluir_disciplina(int(id))
        elif escolha == "12":
            listar_matriculas()
            id = input("ID da matrícula a ser excluída: ")
            excluir_matricula(int(id))
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()