CREATE DATABASE IF NOT EXISTS Biblioteca;
USE Biblioteca;

CREATE TABLE IF NOT EXISTS Autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor_id INT,
    ano_publicacao INT,
    FOREIGN KEY (autor_id) REFERENCES Autores(id) ON DELETE CASCADE
);

INSERT INTO Autores (nome, nacionalidade) VALUES
('J.K. Rowling', 'Britânica'),
('George R.R. Martin', 'Americana'),
('J.R.R. Tolkien', 'Britânica'),
('Agatha Christie', 'Britânica'),
('Isaac Asimov', 'Russa');

INSERT INTO Livros (titulo, autor_id, ano_publicacao) VALUES
('Harry Potter e a Pedra Filosofal', 1, 1997),
('Harry Potter e a Câmara Secreta', 1, 1998),
('A Guerra dos Tronos', 2, 1996),
('A Fúria dos Reis', 2, 1998),
('O Senhor dos Anéis: A Sociedade do Anel', 3, 1954),
('O Senhor dos Anéis: As Duas Torres', 3, 1954),
('Assassinato no Expresso do Oriente', 4, 1934),
('O Misterioso Caso de Styles', 4, 1920),
('Eu, Robô', 5, 1950),
('Fundação', 5, 1951);

SELECT * FROM Autores;
SELECT * FROM Livros;