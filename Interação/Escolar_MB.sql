CREATE DATABASE IF NOT EXISTS Escolar_MB;
USE Escolar_MB;

CREATE TABLE IF NOT EXISTS Alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    endereco VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Disciplinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    professor VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    disciplina_id INT,
    ano_letivo YEAR,
    FOREIGN KEY (aluno_id) REFERENCES Alunos(id) ON DELETE CASCADE,
    FOREIGN KEY (disciplina_id) REFERENCES Disciplinas(id) ON DELETE CASCADE
);

INSERT INTO Alunos (nome, data_nascimento, endereco) VALUES
('João Silva', '2005-03-15', 'Rua A, 123'),
('Maria Souza', '2006-07-20', 'Av. B, 456'),
('Carlos Oliveira', '2004-01-10', 'Praça C, 789');

INSERT INTO Disciplinas (nome, professor) VALUES
('Matemática', 'Prof. Ana Lima'),
('Português', 'Prof. José Santos'),
('Ciências', 'Prof. Marina Costa');

INSERT INTO Matriculas (aluno_id, disciplina_id, ano_letivo) VALUES
(1, 1, 2024),
(1, 2, 2024),
(2, 1, 2024),
(3, 3, 2024);

SELECT * FROM ALunos;
SELECT * FROM Disciplinas;
SELECT * FROM Matriculas;