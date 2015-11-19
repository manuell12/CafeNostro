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
INSERT INTO `producto` VALUES (1,'Ristretto','',1053.00000,1300.00000,'1',3),(2,'Lungo','',1053.00000,1300.00000,'1',3),(3,'Espresso','',1053.00000,1300.00000,'1',3),(4,'Espresso doble','',1458.00000,1800.00000,'1',3),(5,'Americano','',1093.50000,1350.00000,'1',3),(6,'Macchiato','',1215.00000,1500.00000,'1',3),(7,'Macchiato doble','',1579.50000,1950.00000,'1',3),(8,'Capuccino','',1498.50000,1850.00000,'1',3),(9,'Capuccino grande','',1620.00000,2000.00000,'1',3),(10,'Capuccino miel canela','',1620.00000,2000.00000,'1',3),(11,'Latte macchiato','',1620.00000,2000.00000,'1',3),(12,'Mokaccino','',2065.50000,2550.00000,'1',3),(13,'Café helado','',2308.50000,2850.00000,'1',3),(14,'Chocolate helado','',2308.50000,2850.00000,'1',3),(15,'Nutelatte','',2065.50000,2550.00000,'1',3),(16,'Chocolate sabores','',1660.50000,2050.00000,'1',3),(17,'Chocolate marshmallows','',1782.00000,2200.00000,'1',3),(18,'Té selección','',1125.90000,1390.00000,'1',3),(19,'Tetera té gourmet','',2065.50000,2550.00000,'1',3),(20,'Agua mineral','',1174.50000,1450.00000,'1',4),(21,'Soda italiana','',1215.00000,1500.00000,'1',4),(22,'Bebida','',1215.00000,1500.00000,'1',4),(23,'Jugo natural','',1701.00000,2100.00000,'1',4),(24,'Milk shake','',2065.50000,2550.00000,'1',4),(25,'Copa helado','',2187.00000,2700.00000,'1',2),(26,'Panini queso, jamón, verduras','',2389.50000,2950.00000,'1',1),(27,'Panini queso, jamón, tomate, pesto','',2308.50000,2850.00000,'1',1),(28,'Panini queso, chorizo, morrón','',2187.00000,2700.00000,'1',1),(29,'Panini queso, jamón, dijon','',2146.50000,2650.00000,'1',1),(30,'Panini queso, tomate, orégano','',2146.50000,2650.00000,'1',1),(31,'Descafeinado','',202.50000,250.00000,'1',3),(32,'Café X','Un café que posee una X',1611.90000,1990.00000,'0',3),(33,'helado','Un helado bien frío',0.00000,990.00000,'0',2),(34,'Helado','Helado muy frio',801.90000,990.00000,'0',2),(35,'hlado 2','qwertyuikjhgf',7999.56000,9876.00000,'0',1);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (4,'root','root','root','2a533081',0,1);
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

-- Dump completed on 2015-11-18 22:06:37
