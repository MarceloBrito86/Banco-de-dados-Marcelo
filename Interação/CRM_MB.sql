CREATE DATABASE IF NOT EXISTS CRM_MB;
USE CRM_MB;

CREATE TABLE IF NOT EXISTS Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Interacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    data_interacao DATE,
    tipo VARCHAR(50),
    descricao TEXT,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Oportunidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    descricao TEXT,
    valor DECIMAL(10, 2),
    status VARCHAR(50),
    data_criacao DATE,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id) ON DELETE CASCADE
);

INSERT INTO Clientes (nome, email, telefone, endereco) VALUES
('Alice Silva', 'alice.silva@example.com', '123456789', 'Rua A, 123'),
('Bruno Lima', 'bruno.lima@example.com', '987654321', 'Rua B, 456'),
('Carla Souza', 'carla.souza@example.com', '456789123', 'Rua C, 789');

INSERT INTO Interacoes (cliente_id, data_interacao, tipo, descricao) VALUES
(1, '2024-06-01', 'Email', 'Discussão sobre novo produto'),
(2, '2024-06-02', 'Chamada', 'Suporte técnico'),
(3, '2024-06-03', 'Reunião', 'Apresentação de proposta');

INSERT INTO Oportunidades (cliente_id, descricao, valor, status, data_criacao) VALUES
(1, 'Venda de software', 5000.00, 'Em negociação', '2024-06-05'),
(2, 'Contrato de manutenção', 2000.00, 'Fechado', '2024-06-06'),
(3, 'Projeto de consultoria', 15000.00, 'Proposta enviada', '2024-06-07');

SELECT * FROM Clientes;
SELECT * FROM Interacoes;
SELECT * FROM Oportunidades;