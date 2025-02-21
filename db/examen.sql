CREATE DATABASE flaskexamendwes;
USE flaskexamendwes;

CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255)
);

CREATE TABLE objetos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    foto VARCHAR(255),
    descripcion VARCHAR(100),
    id_user INT UNSIGNED,
    FOREIGN KEY (id_user) REFERENCES users(id);
);