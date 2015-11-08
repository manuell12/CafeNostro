-- MySQL dump 10.13  Distrib 5.6.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cafe_nostro
-- ------------------------------------------------------
-- Server version	5.6.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Comida','','Cocina'),(2,'Helado','Selección de helados artesanales de distintos sabores.','Heladeria'),(3,'Café','Distintos tipos de café hecho por baristas profesionales.','Barra'),(4,'Bebestibles','Conjunto de bebidas y/o jugos para acompañar.','Barra');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `pago`
--

LOCK TABLES `pago` WRITE;
/*!40000 ALTER TABLE `pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Ristretto','','Café',1300.00000,'0',3),(2,'Lungo','','Café',1300.00000,'0',3),(3,'Espresso','','Café',1300.00000,'0',3),(4,'Espresso doble','','Café',1800.00000,'0',3),(5,'Americano','','Café',1350.00000,'0',3),(6,'Macchiato','','Café',1500.00000,'0',3),(7,'Macchiato doble','','Café',1950.00000,'0',3),(8,'Capuccino','','Café',1850.00000,'0',3),(9,'Capuccino grande','','Café',2000.00000,'0',3),(10,'Capuccino miel canela','','Café',2000.00000,'0',3),(11,'Latte macchiato','','Café',2000.00000,'0',3),(12,'Mokaccino','','Café',2550.00000,'0',3),(13,'Café helado','','Café',2850.00000,'0',3),(14,'Chocolate helado','','Café',2850.00000,'0',3),(15,'Nutelatte','','Café',2550.00000,'0',3),(16,'Chocolate sabores','','Café',2050.00000,'0',3),(17,'Chocolate marshmallows','','Café',2200.00000,'0',3),(18,'Té selección','','Café',1390.00000,'0',3),(19,'Tetera té gourmet','','Café',2550.00000,'0',3),(20,'Agua mineral','','Bebida',1450.00000,'0',4),(21,'Soda italiana','','Bebida',1500.00000,'0',4),(22,'Bebida','','Bebida',1500.00000,'0',4),(23,'Jugo natural','','Bebida',2100.00000,'0',4),(24,'Milk shake','','Bebida',2550.00000,'0',4),(25,'Copa helado','','Helado',2700.00000,'0',2),(26,'Panini queso, jamón, verduras','','Comida',2950.00000,'0',1),(27,'Panini queso, jamón, tomate, pesto','','Comida',2850.00000,'0',1),(28,'Panini queso, chorizo, morrón','','Comida',2700.00000,'0',1),(29,'Panini queso, jamón, dijon','','Comida',2650.00000,'0',1),(30,'Panini queso, tomate, orégano','','Comida',2650.00000,'0',1),(31,'Descafeinado','','Café',250.00000,'0',3);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (4,'root','root','root','2a533081',0,0);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `venta_has_producto`
--

LOCK TABLES `venta_has_producto` WRITE;
/*!40000 ALTER TABLE `venta_has_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta_has_producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-08 15:52:37
