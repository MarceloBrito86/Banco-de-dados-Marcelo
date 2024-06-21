CREATE DATABASE IF NOT EXISTS Ecommerce_MB;
USE Ecommerce_MB;

CREATE TABLE IF NOT EXISTS Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2),
    estoque INT
);

CREATE TABLE IF NOT EXISTS Pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    data_pedido DATE,
    status VARCHAR(50),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ItensPedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    preco_unitario DECIMAL(10, 2),
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES Produtos(id) ON DELETE CASCADE
);

INSERT INTO Clientes (nome, email, telefone, endereco) VALUES
('Alice Silva', 'alice.silva@example.com', '123456789', 'Rua A, 123'),
('Bruno Lima', 'bruno.lima@example.com', '987654321', 'Rua B, 456'),
('Carla Souza', 'carla.souza@example.com', '456789123', 'Rua C, 789'),
('Diego Ferreira', 'diego.ferreira@example.com', '789123456', 'Rua D, 1011'),
('Elena Costa', 'elena.costa@example.com', '321654987', 'Rua E, 1213');

INSERT INTO Produtos (nome, descricao, preco, estoque) VALUES
('Notebook', 'Notebook Dell Inspiron', 3500.00, 50),
('Smartphone', 'Smartphone Samsung Galaxy', 2500.00, 100),
('Tablet', 'Tablet Apple iPad', 3000.00, 30),
('Monitor', 'Monitor LG 24 polegadas', 800.00, 20),
('Teclado', 'Teclado Mecânico Gamer', 150.00, 150);

INSERT INTO Pedidos (cliente_id, data_pedido, status) VALUES
(1, '2024-06-01', 'Pendente'),
(2, '2024-06-02', 'Enviado'),
(3, '2024-06-03', 'Entregue'),
(4, '2024-06-04', 'Cancelado'),
(5, '2024-06-05', 'Pendente');

INSERT INTO ItensPedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES
(1, 1, 1, 3500.00),
(1, 2, 2, 2500.00),
(2, 3, 1, 3000.00),
(3, 4, 1, 800.00),
(3, 5, 1, 150.00),
(4, 1, 1, 3500.00),
(5, 2, 1, 2500.00),
(5, 5, 5, 150.00);

SELECT * FROM Clientes;
SELECT * FROM Produtos;
SELECT * FROM Pedidos;
SELECT * FROM ItensPedido;