-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-12-2015 a las 00:18:23
-- Versión del servidor: 5.6.21
-- Versión de PHP: 5.5.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `cafe_nostro`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE IF NOT EXISTS `categoria` (
`idCategoria` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` text NOT NULL,
  `preparada_en` varchar(45) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idCategoria`, `nombre`, `descripcion`, `preparada_en`) VALUES
(1, 'Comida', '', 'Cocina'),
(2, 'Helado', 'Selección de helados artesanales de distintos sabores.', 'Heladeria'),
(3, 'Bebidas calientes', 'Distintos tipos de café hecho por baristas profesionales.', 'Barra'),
(4, 'Bebidas frías', 'Conjunto de bebidas y/o jugos para acompañar.', 'Barra'),
(5, 'Repostería', '', 'Vitrina'),
(6, 'Otros', 'Otros', 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE IF NOT EXISTS `empresa` (
`idEmpresa` int(11) NOT NULL,
  `rut` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `giro` varchar(45) NOT NULL,
  `fono` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `num_mesas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago`
--

CREATE TABLE IF NOT EXISTS `pago` (
  `idPago` int(11) NOT NULL,
  `pago_total` decimal(10,5) NOT NULL,
  `efectivo` decimal(10,5) DEFAULT NULL,
  `tarjeta` decimal(10,5) DEFAULT NULL,
  `propina` decimal(10,5) DEFAULT NULL,
  `idVenta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------


--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE IF NOT EXISTS `pedido` (
  `idPedido` int(11) NOT NULL,
  `mesa` varchar(45) NOT NULL,
  `en_curso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------


--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE IF NOT EXISTS `producto` (
`idProducto` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` text NOT NULL,
  `precio_neto` decimal(10,5) NOT NULL,
  `precio_bruto` decimal(10,5) NOT NULL,
  `status` varchar(1) DEFAULT NULL,
  `idCategoria` int(11) NOT NULL,
  `codigo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`idProducto`, `nombre`, `descripcion`, `precio_neto`, `precio_bruto`, `status`, `idCategoria`, `codigo`) VALUES
(1, 'Ristretto', '', '1053.00000', '1300.00000', '1', 3, 'CAF0'),
(2, 'Lungo', '', '1053.00000', '1300.00000', '1', 3, 'CAF1'),
(3, 'Espresso', '', '1053.00000', '1300.00000', '1', 3, NULL),
(4, 'Espresso doble', '', '1458.00000', '1800.00000', '1', 3, NULL),
(5, 'Americano', '', '1093.50000', '1350.00000', '1', 3, NULL),
(6, 'Macchiato', '', '1215.00000', '1500.00000', '1', 3, NULL),
(7, 'Macchiato doble', '', '1579.50000', '1950.00000', '1', 3, NULL),
(8, 'Capuccino', '', '1498.50000', '1850.00000', '1', 3, NULL),
(9, 'Capuccino grande', '', '1620.00000', '2000.00000', '1', 3, NULL),
(10, 'Capuccino miel canela', '', '1620.00000', '2000.00000', '1', 3, NULL),
(11, 'Latte macchiato', '', '1620.00000', '2000.00000', '1', 3, NULL),
(12, 'Mokaccino', '', '2065.50000', '2550.00000', '1', 3, NULL),
(13, 'Café helado', '', '2308.50000', '2850.00000', '1', 3, NULL),
(14, 'Chocolate helado', '', '2308.50000', '2850.00000', '1', 3, NULL),
(15, 'Nutelatte', '', '2065.50000', '2550.00000', '1', 3, NULL),
(16, 'Chocolate sabores', '', '1660.50000', '2050.00000', '1', 3, NULL),
(17, 'Chocolate marshmallows', '', '1782.00000', '2200.00000', '1', 3, NULL),
(18, 'Té selección', '', '1125.90000', '1390.00000', '1', 3, NULL),
(19, 'Tetera té gourmet', '', '2065.50000', '2550.00000', '1', 3, NULL),
(20, 'Agua mineral', '', '1174.50000', '1450.00000', '1', 4, NULL),
(21, 'Soda italiana', '', '1215.00000', '1500.00000', '1', 4, NULL),
(22, 'Bebida', '', '1215.00000', '1500.00000', '1', 4, NULL),
(23, 'Jugo natural', '', '1701.00000', '2100.00000', '1', 4, NULL),
(24, 'Milk shake', '', '2065.50000', '2550.00000', '1', 4, NULL),
(25, 'Copa helado', '', '2187.00000', '2700.00000', '1', 2, NULL),
(26, 'Panini queso, jamón, verduras', '', '2389.50000', '2950.00000', '1', 1, NULL),
(27, 'Panini queso, jamón, tomate, pesto', '', '2308.50000', '2850.00000', '1', 1, NULL),
(28, 'Panini queso, chorizo, morrón', '', '2187.00000', '2700.00000', '1', 1, NULL),
(29, 'Panini queso, jamón, dijon', '', '2146.50000', '2650.00000', '1', 1, NULL),
(30, 'Panini queso, tomate, orégano', '', '2146.50000', '2650.00000', '1', 1, NULL),
(31, 'Descafeinado', '', '202.50000', '250.00000', '1', 3, NULL),
(32, 'Café X', 'Un café que posee una X', '1611.90000', '1990.00000', '0', 3, NULL),
(33, 'helado', 'Un helado bien frío', '0.00000', '990.00000', '0', 2, NULL),
(34, 'Helado', 'Helado muy frio', '801.90000', '990.00000', '0', 2, NULL),
(35, 'helado2', '', '1620.00000', '2000.00000', '1', 2, 'HEL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
`idUsuario` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `rut` varchar(15) NOT NULL,
  `clave` varchar(45) NOT NULL,
  `tipo` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `nombre`, `apellido`, `rut`, `clave`, `tipo`, `status`) VALUES
(4, 'root', 'root', 'root', '2a533081', 0, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE IF NOT EXISTS `venta` (
`idVenta` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `num_documento` int(11) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `total_pago` decimal(10,5) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `idPedido` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta_has_producto`
--

CREATE TABLE IF NOT EXISTS `venta_has_producto` (
  `idPedido` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_venta` decimal(10,5) NOT NULL,
  `porcentaje_descuento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
 ADD PRIMARY KEY (`idCategoria`);

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
 ADD PRIMARY KEY (`idEmpresa`);

--
-- Indices de la tabla `pago`
--
ALTER TABLE `pago`
 ADD PRIMARY KEY (`idPago`), ADD KEY `fk_pago_venta1_idx` (`idVenta`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
 ADD PRIMARY KEY (`idPedido`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
 ADD PRIMARY KEY (`idProducto`), ADD KEY `fk_producto_categoria1_idx` (`idCategoria`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
 ADD PRIMARY KEY (`idUsuario`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
 ADD PRIMARY KEY (`idVenta`), ADD KEY `fk_venta_usuario_idx` (`idUsuario`), ADD KEY `fk_venta_pedido1_idx` (`idPedido`);

--
-- Indices de la tabla `venta_has_producto`
--
ALTER TABLE `venta_has_producto`
 ADD KEY `fk_venta_has_producto_producto1_idx` (`idProducto`), ADD KEY `fk_venta_has_producto_pedido1_idx` (`idPedido`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
MODIFY `idCategoria` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `empresa`
--
ALTER TABLE `empresa`
MODIFY `idEmpresa` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=36;
--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
MODIFY `idVenta` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pago`
--
ALTER TABLE `pago`
ADD CONSTRAINT `fk_pago_venta1` FOREIGN KEY (`idVenta`) REFERENCES `venta` (`idVenta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
ADD CONSTRAINT `fk_producto_categoria1` FOREIGN KEY (`idCategoria`) REFERENCES `categoria` (`idCategoria`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
ADD CONSTRAINT `fk_venta_pedido1` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`idPedido`) ON DELETE NO ACTION ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_venta_usuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `venta_has_producto`
--
ALTER TABLE `venta_has_producto`
ADD CONSTRAINT `fk_venta_has_producto_pedido1` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`idPedido`) ON DELETE NO ACTION ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_venta_has_producto_producto1` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
