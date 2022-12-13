-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: AmbulanceAlertingSystem
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hospital`
--

DROP TABLE IF EXISTS `hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital` (
  `h_id` int NOT NULL AUTO_INCREMENT,
  `h_discord_name` varchar(100) NOT NULL,
  `hospital_name` varchar(100) NOT NULL,
  `accept_patient` int NOT NULL,
  `location` varchar(200) NOT NULL,
  PRIMARY KEY (`h_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital`
--

LOCK TABLES `hospital` WRITE;
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` VALUES (1,'dfaf','EWRds',0,'ewrfafew'),(2,'samuela#1234','yyy hospital',0,'tambaram'),(3,'saem#1234','yxyx Hospital',1,'thiruvanmuir');
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trafficsignal`
--

DROP TABLE IF EXISTS `trafficsignal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trafficsignal` (
  `sgnal_id` int NOT NULL AUTO_INCREMENT,
  `f_rom` varchar(255) NOT NULL,
  `t_o` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `name` varchar(60) NOT NULL,
  `s_s_status` bit(1) NOT NULL,
  `discord_name` varchar(100) NOT NULL,
  PRIMARY KEY (`sgnal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trafficsignal`
--

LOCK TABLES `trafficsignal` WRITE;
/*!40000 ALTER TABLE `trafficsignal` DISABLE KEYS */;
INSERT INTO `trafficsignal` VALUES (1,'tambaram','thiruvanmuir','thambaram','sam',_binary '\0','vinotham#123'),(2,'thiruvanmuir','t nagar','thambaram','sam',_binary '\0','vinotham#123'),(3,'kandhanchavady ','tidle park','guindy','Kumar',_binary '\0','kumar#2314'),(4,'t nagar','vellachery','guindy','Kumar',_binary '\0','kumar#2314'),(5,'Loc1','Loc2','Viruthunagar','Huru',_binary '\0','Huru#1234'),(6,'Loc3','Loc4','Viruthunagar','Huru',_binary '\0','Huru#1234');
/*!40000 ALTER TABLE `trafficsignal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `proffession` varchar(3) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_id` (`email_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'K:4r','oij4q3jr@aewifj.32984','hpt','hjasdfjklladskjf'),(2,'sam','sam@gamil.com','trp','sam1234'),(3,'adhi','adhi@gmail.com','amd','adhi1234'),(4,'same','same@same.in','hpt','same1234'),(6,'hello','hello@1234','hpt','hello1234'),(7,'value','value@gmail.com','hpt','value1234'),(8,'vanakam','vanakam@12.21','hpt','hai'),(9,'Samuela','samuela@gmail.com','hpt','samuela1234'),(10,'Saem','saem@gmail.com','hpt','saem1234'),(11,'Kumar','kumar@gmail.com','trp','kumar1234'),(12,'anu','anu@gmail.com','amd','anu1234'),(13,'Huru','huru@gmail.com','trp','huru1234');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-13 15:55:08
