-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: invernapro
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `cultivo_plantas`
--

DROP TABLE IF EXISTS `cultivo_plantas`;
/*!50001 DROP VIEW IF EXISTS `cultivo_plantas`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cultivo_plantas` AS SELECT 
 1 AS `variedad`,
 1 AS `contLote`,
 1 AS `contPlanta`,
 1 AS `venta`,
 1 AS `merma`,
 1 AS `reproducir`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `lotes`
--

DROP TABLE IF EXISTS `lotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lotes` (
  `cont` int NOT NULL AUTO_INCREMENT,
  `idVar` char(10) DEFAULT NULL,
  `idMetodo` char(6) DEFAULT NULL,
  `fecha` date DEFAULT (curdate()),
  `cantidad` int NOT NULL,
  PRIMARY KEY (`cont`),
  KEY `fk_lotemetodo` (`idMetodo`),
  KEY `fk_variedad` (`idVar`),
  CONSTRAINT `fk_lotemetodo` FOREIGN KEY (`idMetodo`) REFERENCES `metodos` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_variedad` FOREIGN KEY (`idVar`) REFERENCES `variedades` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lotes`
--

LOCK TABLES `lotes` WRITE;
/*!40000 ALTER TABLE `lotes` DISABLE KEYS */;
INSERT INTO `lotes` VALUES (1,'CHLRVTTT30','plti55','2023-11-10',12),(2,'SYNGPX--36','esag88','2023-11-17',6),(3,'SYNGALB-84','esag77','2023-11-18',4),(4,'HWRTZBRN23','plti55','2023-11-24',4),(5,'SNSVLRNT47','hoti60','2023-11-24',5),(6,'SDMLLBM-54','hoti75','2023-11-27',8),(7,'DRCNMSSN11','esag77','2023-11-27',9);
/*!40000 ALTER TABLE `lotes` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `fecha_insert_lote` BEFORE INSERT ON `lotes` FOR EACH ROW begin
    IF new.fecha = NULL THEN
        SET new.fecha = now();
    END IF;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `plantas_from_lote` AFTER INSERT ON `lotes` FOR EACH ROW begin
    declare n int;
    set n = 0;
    while n < new.cantidad do
        set n = n+1;
        INSERT into plantas (contLote,contPlanta) values (new.cont,n);
    end while;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `plantas_update_lote` AFTER UPDATE ON `lotes` FOR EACH ROW begin
    declare old_plantas int;
    declare new_plantas int;
    SET old_plantas = (SELECT COUNT(*) FROM plantas WHERE contLote = new.cont);
    IF old_plantas > new.cantidad THEN
        DELETE FROM plantas WHERE contLote = new.cont AND contPlanta > new.cantidad;
    ELSEIF old_plantas < new.cantidad THEN
        SET new_plantas = old_plantas;
        WHILE new_plantas < new.cantidad DO
            SET new_plantas = new_plantas+1;
            INSERT into plantas (contLote,contPlanta) values (new.cont,new_plantas);
        END WHILE;
    END IF;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `metodos`
--

DROP TABLE IF EXISTS `metodos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metodos` (
  `id` char(6) NOT NULL,
  `organo` char(32) DEFAULT NULL,
  `medio` char(32) DEFAULT NULL,
  `notas` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metodos`
--

LOCK TABLES `metodos` WRITE;
/*!40000 ALTER TABLE `metodos` DISABLE KEYS */;
INSERT INTO `metodos` VALUES ('esag48','Esqueje','Agua','Se debe dejar reposar el corte varios días hasta la formación de costra.\nLuego se sumerge en agua de forma acostumbrada.'),('esag77','Esqueje','Agua','Dejando secar el punto de corte antes de sumergir en agua'),('esag88','Esqueje','Agua','Sumergir unos centimetros en agua por el lado de corte'),('esai42','Esqueje','Aire','Se descubre de corteza en una rama apropiada, raspando.\nSe frota la zona expuesta con enraizante en polvo.\nCuando aparezcan raices, se hace el corte.'),('esai68','Esqueje','Aire','Torcer cuidadosamente la rama hasta que haga contacto con la tierra en la nueva maceta y sujetarla en ese lugar.'),('esca81','Esqueje','Caja',''),('esti43','Esqueje','Tierra','Se deja reposar el esqueje en la tierra, manteniendola húmeda hasta que aparezcan raíces.'),('esti56','Esqueje','Tierra','Enterrar el tallo varios centimetros en la tierra por el lado del corte'),('esti58','Esqueje','Tierra','Añadir hormona de enraizado en la zona del corte antes de enterrar'),('esti84','Esqueje','Tierra','Será necesario sellar el corte en la planta madre con cera para evitar infecciones.'),('hoag37','Hoja','Agua','Colocar la base de la hoja en el agua'),('hoag38','Hoja','Agua','Cortar secciones de hoja y sumergir la parte inferior en agua.\nProcurando que la base de la sección no quede completamente plana contra el fondo del recipiente.'),('hoag45','Hoja','Agua','La base de la hoja debe ser sostenida por encima del agua, en un espacio cerrado.'),('hoca76','Hoja','Caja','Cortar la hoja a travez del nervio central, añadir enraizador en la herida, colocar cara arriba en el sustrato'),('hoti22','Hoja','Tierra','Cortando la hoja a la mitad a lo largo del nervio central.\nInsertar la hoja en la tierra por el lado del corte.'),('hoti60','Hoja','Tierra','Cortar secciones de hoja y enterrar por la parte interior.'),('hoti75','Hoja','Tierra','Dejar reposar la hoja sobre tierra y regar solo cuando la superficie esté completamente seca.'),('plag81','Plantula','Agua','Procurar que solo la base de la hoja, o raíces ya existentes, toquen el agua.'),('plti55','Plantula','Tierra','Colocar firmemente la plántula sobre la tierra y regar frecuentemente hasta la aparición de raices.'),('raag26','Raíz','Agua','Remover el tallo de la sección de raíz, limpiar la tierra, y colocarla en agua hasta que crezcan raíces secundarias nuevas.'),('rati53','Raíz','Tierra','Separar las plantas hijas desde la raíz y colocarlas en macetas nuevas.'),('riti52','Rizoma','Tierra','Procurar cortar el rizoma antes de donde ya tenga crecimiento de raices.'),('taag24','Tallo','Agua','Sumergir el tope de la planta en el agua');
/*!40000 ALTER TABLE `metodos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nombres`
--

DROP TABLE IF EXISTS `nombres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nombres` (
  `nombre` char(128) NOT NULL,
  `idioma` char(64) DEFAULT NULL,
  PRIMARY KEY (`nombre`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nombres`
--

LOCK TABLES `nombres` WRITE;
/*!40000 ALTER TABLE `nombres` DISABLE KEYS */;
INSERT INTO `nombres` VALUES ('Arrowhead','Ingles'),('Batata','Español'),('Bird nest','Inglés'),('Camote','Español'),('Corn plant','Inglés'),('Corona de cristo','Español'),('Espada de san jorge','Español'),('Jellybean plant','Inglés'),('Lemongrass','Inglés'),('Lengua de suegra','Español'),('Listón','Español'),('Meloncito','Español'),('Mono araña','Español'),('Palo de brazil','Español'),('Papiro','Español'),('Paraguas','Español'),('Platanitos','Español'),('Rosarito','Español'),('Sávila','Español'),('Sedo','Español'),('Spider plant','Inglés'),('Stonecrop','Inglés'),('Suculenta','Español'),('Sweet potato vine','Ingles'),('Té de limon','Español'),('Umbrella','Inglés'),('Uva de gato','Español');
/*!40000 ALTER TABLE `nombres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plantas`
--

DROP TABLE IF EXISTS `plantas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plantas` (
  `contLote` int NOT NULL,
  `contPlanta` int NOT NULL,
  `venta` tinyint(1) DEFAULT '0',
  `merma` tinyint(1) DEFAULT '0',
  `reproducir` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`contLote`,`contPlanta`),
  CONSTRAINT `fk_loteP` FOREIGN KEY (`contLote`) REFERENCES `lotes` (`cont`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plantas`
--

LOCK TABLES `plantas` WRITE;
/*!40000 ALTER TABLE `plantas` DISABLE KEYS */;
INSERT INTO `plantas` VALUES (1,1,0,0,1),(1,2,1,0,0),(1,3,1,0,1),(1,4,0,1,0),(1,5,0,1,0),(1,6,1,0,0),(1,7,0,1,0),(1,8,0,1,0),(1,9,1,0,1),(1,10,1,0,1),(1,11,1,0,1),(1,12,1,0,1),(2,1,0,0,0),(2,2,0,1,0),(2,3,0,0,0),(2,4,1,0,1),(2,5,0,0,0),(2,6,0,1,0),(3,1,0,0,0),(3,2,0,0,0),(3,3,1,0,0),(3,4,0,1,0),(4,1,1,0,1),(4,2,0,1,0),(4,3,1,0,0),(4,4,1,0,0),(5,1,1,0,0),(5,2,0,0,0),(5,3,0,1,0),(5,4,1,0,0),(5,5,1,0,0),(6,1,1,0,0),(6,2,1,0,0),(6,3,0,1,0),(6,4,1,0,0),(6,5,1,0,1),(6,6,0,1,0),(6,7,0,1,0),(6,8,0,1,0),(7,1,0,0,1),(7,2,0,1,0),(7,3,1,0,1),(7,4,1,0,1),(7,5,0,1,0),(7,6,0,1,0),(7,7,1,0,0),(7,8,1,0,0),(7,9,1,0,0);
/*!40000 ALTER TABLE `plantas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variedades`
--

DROP TABLE IF EXISTS `variedades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `variedades` (
  `id` char(10) NOT NULL,
  `especie` char(128) NOT NULL,
  `nombre` char(128) NOT NULL,
  `luz` char(3) NOT NULL,
  `riego` float DEFAULT NULL,
  `temporada` char(4) DEFAULT NULL,
  `temperatura` char(6) DEFAULT NULL,
  `ph` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `specvar` (`especie`,`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variedades`
--

LOCK TABLES `variedades` WRITE;
/*!40000 ALTER TABLE `variedades` DISABLE KEYS */;
INSERT INTO `variedades` VALUES ('CHLRVTTT30','Chlorophytum comosum','Vittatum','A08',0.5,'0112','002032',7),('CYPRNNS-88','Cyperus papyrus','Nanus','D08',0.6,'0310','003034',7),('DRCNMSSN11','Dracaena fragrans','Massangeana','A08',0.4,'0711','010029',6.1),('HWRTZBRN23','Haworthia reinwardtii','Zebrina','D05',0.1,'0508','010032',7),('LVRCHNN-37','Aloe vera','Chinensis','D05',0.2,'0411','013027',7),('PMBTTRCL02','Ipomea batatas','Tricolor','D06',0.4,'0408','005032',8),('SDMCCRST68','Sedum clavatum','Cristatum','D06',0,'0410','0-4036',7),('SDMLLBM-54','Sedum album','Album','D05',0,'0211','005030',8),('SNSVHHNG54','Sansevieria trifasciata','Hahnii golden','D05',0,'0410','012030',7),('SNSVLRNT47','Sansevieria trifasciata','Laurentii','D06',0,'0210','012030',7),('SYNGALB-84','Syngonium podophyllum','Albo','A10',0.4,'0408','020027',6),('SYNGPX--36','Syngonium podophyllum','Pixie','A08',0.4,'0409','016024',6);
/*!40000 ALTER TABLE `variedades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variedadmetodos`
--

DROP TABLE IF EXISTS `variedadmetodos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `variedadmetodos` (
  `idVar` char(10) DEFAULT NULL,
  `idMetodo` char(6) DEFAULT NULL,
  KEY `fk_metVariedades` (`idMetodo`),
  KEY `fk_varMetodos` (`idVar`),
  CONSTRAINT `fk_metVariedades` FOREIGN KEY (`idMetodo`) REFERENCES `metodos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_varMetodos` FOREIGN KEY (`idVar`) REFERENCES `variedades` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variedadmetodos`
--

LOCK TABLES `variedadmetodos` WRITE;
/*!40000 ALTER TABLE `variedadmetodos` DISABLE KEYS */;
INSERT INTO `variedadmetodos` VALUES ('LVRCHNN-37','plti55'),('SDMCCRST68','esti56'),('SDMCCRST68','esag88'),('CHLRVTTT30','plti55'),('PMBTTRCL02','esca81'),('CHLRVTTT30','plag81'),('HWRTZBRN23','riti52'),('LVRCHNN-37','riti52'),('PMBTTRCL02','esai68'),('PMBTTRCL02','esag88'),('SDMCCRST68','hoag45'),('SDMCCRST68','hoti75'),('SDMLLBM-54','hoag45'),('SDMLLBM-54','hoti75'),('SDMLLBM-54','esti58'),('SNSVHHNG54','riti52'),('SNSVHHNG54','hoti60'),('SNSVLRNT47','hoag38'),('SNSVLRNT47','hoti60'),('SNSVLRNT47','riti52'),('SYNGALB-84','esca81'),('SYNGALB-84','esag77'),('SYNGPX--36','esca81'),('SYNGPX--36','esag77'),('CYPRNNS-88','taag24'),('CYPRNNS-88','rati53'),('DRCNMSSN11','esag77');
/*!40000 ALTER TABLE `variedadmetodos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variedadnombres`
--

DROP TABLE IF EXISTS `variedadnombres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `variedadnombres` (
  `idVar` char(10) DEFAULT NULL,
  `nombrecomun` char(128) DEFAULT NULL,
  KEY `fk_nomVariedades` (`nombrecomun`),
  KEY `fk_varNombres` (`idVar`),
  CONSTRAINT `fk_nomVariedades` FOREIGN KEY (`nombrecomun`) REFERENCES `nombres` (`nombre`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_varNombres` FOREIGN KEY (`idVar`) REFERENCES `variedades` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variedadnombres`
--

LOCK TABLES `variedadnombres` WRITE;
/*!40000 ALTER TABLE `variedadnombres` DISABLE KEYS */;
INSERT INTO `variedadnombres` VALUES ('SDMLLBM-54','Sedo'),('SDMLLBM-54','Uva de gato'),('LVRCHNN-37','Sávila'),('SDMCCRST68','Sedo'),('SDMCCRST68','Suculenta'),('CHLRVTTT30','Spider plant'),('CHLRVTTT30','Listón'),('CHLRVTTT30','Mono araña'),('PMBTTRCL02','Camote'),('PMBTTRCL02','Sweet potato vine'),('HWRTZBRN23','Suculenta'),('SDMLLBM-54','Suculenta'),('SDMLLBM-54','Platanitos'),('SNSVHHNG54','Suculenta'),('SNSVHHNG54','Bird nest'),('SNSVLRNT47','Espada de san jorge'),('SNSVLRNT47','Lengua de suegra'),('SYNGALB-84','Arrowhead'),('SYNGPX--36','Arrowhead'),('CYPRNNS-88','Umbrella'),('CYPRNNS-88','Paraguas'),('CYPRNNS-88','Papiro'),('PMBTTRCL02','Batata'),('SDMLLBM-54','Jellybean plant'),('SDMLLBM-54','Platanitos'),('DRCNMSSN11','Palo de brazil'),('DRCNMSSN11','Corn plant');
/*!40000 ALTER TABLE `variedadnombres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `ver_lotes`
--

DROP TABLE IF EXISTS `ver_lotes`;
/*!50001 DROP VIEW IF EXISTS `ver_lotes`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ver_lotes` AS SELECT 
 1 AS `# de lote`,
 1 AS `Variedad`,
 1 AS `Método`,
 1 AS `fecha`,
 1 AS `Existencia`,
 1 AS `Pérdidas`,
 1 AS `% exito`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `ver_variedades`
--

DROP TABLE IF EXISTS `ver_variedades`;
/*!50001 DROP VIEW IF EXISTS `ver_variedades`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ver_variedades` AS SELECT 
 1 AS `id`,
 1 AS `especie`,
 1 AS `nombre`,
 1 AS `Cat`,
 1 AS `Horas`,
 1 AS `% agua`,
 1 AS `mes inicio`,
 1 AS `mes fin`,
 1 AS `t min`,
 1 AS `t max`,
 1 AS `ph`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'invernapro'
--

--
-- Final view structure for view `cultivo_plantas`
--

/*!50001 DROP VIEW IF EXISTS `cultivo_plantas`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`invernadmin`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cultivo_plantas` AS select `lotes`.`idVar` AS `variedad`,`plantas`.`contLote` AS `contLote`,`plantas`.`contPlanta` AS `contPlanta`,`plantas`.`venta` AS `venta`,`plantas`.`merma` AS `merma`,`plantas`.`reproducir` AS `reproducir` from (`lotes` join `plantas` on((`plantas`.`contLote` = `lotes`.`cont`))) order by `plantas`.`contLote` desc,`plantas`.`contPlanta` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ver_lotes`
--

/*!50001 DROP VIEW IF EXISTS `ver_lotes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`invernadmin`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ver_lotes` AS select `lotes`.`cont` AS `# de lote`,`lotes`.`idVar` AS `Variedad`,`lotes`.`idMetodo` AS `Método`,`lotes`.`fecha` AS `fecha`,(select count(0) from `plantas` where ((`plantas`.`contLote` = `lotes`.`cont`) and (`plantas`.`merma` = 0))) AS `Existencia`,(select count(0) from `plantas` where ((`plantas`.`contLote` = `lotes`.`cont`) and (`plantas`.`merma` <> 0))) AS `Pérdidas`,round((((select count(0) from `plantas` where ((`plantas`.`contLote` = `lotes`.`cont`) and (`plantas`.`merma` = 0))) * 100) / `lotes`.`cantidad`),0) AS `% exito` from `lotes` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ver_variedades`
--

/*!50001 DROP VIEW IF EXISTS `ver_variedades`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`invernadmin`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ver_variedades` AS select `variedades`.`id` AS `id`,`variedades`.`especie` AS `especie`,`variedades`.`nombre` AS `nombre`,substr(`variedades`.`luz`,1,1) AS `Cat`,cast(substr(`variedades`.`luz`,2) as unsigned) AS `Horas`,round((`variedades`.`riego` * 100),0) AS `% agua`,substr(`variedades`.`temporada`,1,2) AS `mes inicio`,substr(`variedades`.`temporada`,3) AS `mes fin`,trim(leading '0' from substr(`variedades`.`temperatura`,1,3)) AS `t min`,trim(leading '0' from substr(`variedades`.`temperatura`,4)) AS `t max`,`variedades`.`ph` AS `ph` from `variedades` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-27 14:54:35
