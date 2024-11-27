CREATE DATABASE IF NOT EXISTS app_crud_juego;
USE app_crud_juego;

CREATE TABLE IF NOT EXISTS `juegos` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `nombre` VARCHAR(255) NOT NULL,
    `descripcion` TEXT,
    `precio` DECIMAL(9,2)
);
