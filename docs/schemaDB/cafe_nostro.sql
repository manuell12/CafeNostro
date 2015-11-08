-- MySQL Workbench Synchronization
-- Generated: 2015-11-04 20:32
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Esteban

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `cafe_nostro` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`usuario` (
  `idUsuario` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `nombre` VARCHAR(45) NOT NULL COMMENT '',
  `apellido` VARCHAR(45) NOT NULL COMMENT '',
  `rut` VARCHAR(15) NOT NULL COMMENT '',
  `clave` VARCHAR(45) NOT NULL COMMENT '',
  `tipo` INT(11) NOT NULL COMMENT '',
  `status` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`idUsuario`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`venta` (
  `idVenta` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `fecha` DATE NOT NULL COMMENT '',
  `num_documento` INT(11) NOT NULL COMMENT '',
  `tipo` VARCHAR(20) NOT NULL COMMENT '',
  `total_pago` DECIMAL(10,5) NOT NULL COMMENT '',
  `idUsuario` INT(11) NOT NULL COMMENT '',
  `idPedido` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`idVenta`)  COMMENT '',
  INDEX `fk_venta_usuario_idx` (`idUsuario` ASC)  COMMENT '',
  INDEX `fk_venta_pedido1_idx` (`idPedido` ASC)  COMMENT '',
  CONSTRAINT `fk_venta_usuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `cafe_nostro`.`usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venta_pedido1`
    FOREIGN KEY (`idPedido`)
    REFERENCES `cafe_nostro`.`pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`pago` (
  `idPago` INT(11) NOT NULL COMMENT '',
  `pago_total` DECIMAL(10,5) NOT NULL COMMENT '',
  `efectivo` DECIMAL(10,5) NULL DEFAULT NULL COMMENT '',
  `tarjeta` DECIMAL(10,5) NULL DEFAULT NULL COMMENT '',
  `propina` DECIMAL(10,5) NULL DEFAULT NULL COMMENT '',
  `idVenta` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`idPago`)  COMMENT '',
  INDEX `fk_pago_venta1_idx` (`idVenta` ASC)  COMMENT '',
  CONSTRAINT `fk_pago_venta1`
    FOREIGN KEY (`idVenta`)
    REFERENCES `cafe_nostro`.`venta` (`idVenta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`pedido` (
  `idPedido` INT(11) NOT NULL COMMENT '',
  `mesa` VARCHAR(45) NOT NULL COMMENT '',
  `en_curso` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`idPedido`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`venta_has_producto` (
  `idPedido` INT(11) NOT NULL COMMENT '',
  `idProducto` INT(11) NOT NULL COMMENT '',
  `cantidad` INT(11) NOT NULL COMMENT '',
  `precio_venta` DECIMAL(10,5) NOT NULL COMMENT '',
  `porcentaje_descuento` INT(11) NULL DEFAULT NULL COMMENT '',
  INDEX `fk_venta_has_producto_producto1_idx` (`idProducto` ASC)  COMMENT '',
  INDEX `fk_venta_has_producto_pedido1_idx` (`idPedido` ASC)  COMMENT '',
  CONSTRAINT `fk_venta_has_producto_producto1`
    FOREIGN KEY (`idProducto`)
    REFERENCES `cafe_nostro`.`producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venta_has_producto_pedido1`
    FOREIGN KEY (`idPedido`)
    REFERENCES `cafe_nostro`.`pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`producto` (
  `idProducto` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `nombre` VARCHAR(45) NOT NULL COMMENT '',
  `descripcion` TEXT NOT NULL COMMENT '',
  `tipo` VARCHAR(45) NULL DEFAULT NULL COMMENT '',
  `precio_neto` DECIMAL(10,5) NOT NULL COMMENT '',
  `status` VARCHAR(1) NULL DEFAULT NULL COMMENT '',
  `idCategoria` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`idProducto`)  COMMENT '',
  INDEX `fk_producto_categoria1_idx` (`idCategoria` ASC)  COMMENT '',
  CONSTRAINT `fk_producto_categoria1`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `cafe_nostro`.`categoria` (`idCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`categoria` (
  `idCategoria` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `nombre` VARCHAR(45) NOT NULL COMMENT '',
  `descripcion` TEXT NOT NULL COMMENT '',
  `preparada_en` VARCHAR(45) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`idCategoria`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `cafe_nostro`.`empresa` (
  `idEmpresa` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `rut` VARCHAR(45) NOT NULL COMMENT '',
  `nombre` VARCHAR(45) NOT NULL COMMENT '',
  `direccion` VARCHAR(45) NOT NULL COMMENT '',
  `ciudad` VARCHAR(45) NOT NULL COMMENT '',
  `giro` VARCHAR(45) NOT NULL COMMENT '',
  `fono` VARCHAR(45) NOT NULL COMMENT '',
  `email` VARCHAR(45) NOT NULL COMMENT '',
  `num_mesas` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`idEmpresa`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
