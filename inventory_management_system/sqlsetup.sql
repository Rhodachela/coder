CREATE DATABSE IF NOT EXISTS inventory_management;
USE inventory_management;

CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(200) NOT NULL,
    stock_quantity INT NOT NULL,
    price INT NOT NULL
);