-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: AgendaEscolar
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.21.10.2

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
-- Table structure for table `Agendas`
--

DROP TABLE IF EXISTS `Agendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Agendas` (
  `Agenda_id` int NOT NULL AUTO_INCREMENT,
  `Data` date NOT NULL,
  `Matricula_id` int NOT NULL,
  `TurmaProfessor_id` int NOT NULL,
  PRIMARY KEY (`Agenda_id`),
  KEY `Agendas_Matricula_id_08edfb5c_fk_Matriculas_Matricula_id` (`Matricula_id`),
  KEY `Agendas_TurmaProfessor_id_0136b3c9_fk_TurmasPro` (`TurmaProfessor_id`),
  CONSTRAINT `Agendas_Matricula_id_08edfb5c_fk_Matriculas_Matricula_id` FOREIGN KEY (`Matricula_id`) REFERENCES `Matriculas` (`Matricula_id`),
  CONSTRAINT `Agendas_TurmaProfessor_id_0136b3c9_fk_TurmasPro` FOREIGN KEY (`TurmaProfessor_id`) REFERENCES `TurmasProfessores` (`TurmaProfessor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Agendas`
--

LOCK TABLES `Agendas` WRITE;
/*!40000 ALTER TABLE `Agendas` DISABLE KEYS */;
/*!40000 ALTER TABLE `Agendas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AgendasAlimentos`
--

DROP TABLE IF EXISTS `AgendasAlimentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AgendasAlimentos` (
  `AgendaAlimento_id` int NOT NULL AUTO_INCREMENT,
  `DiaHoraRegistro` datetime(6) NOT NULL,
  `Aceite` varchar(1) NOT NULL,
  `Hora` time(6) NOT NULL,
  `Agenda_id` int NOT NULL,
  `Alimento_id` int NOT NULL,
  PRIMARY KEY (`AgendaAlimento_id`),
  KEY `AgendasAlimentos_Agenda_id_4f566d68_fk_Agendas_Agenda_id` (`Agenda_id`),
  KEY `AgendasAlimentos_Alimento_id_53922b70_fk_Alimentos_Alimento_id` (`Alimento_id`),
  CONSTRAINT `AgendasAlimentos_Agenda_id_4f566d68_fk_Agendas_Agenda_id` FOREIGN KEY (`Agenda_id`) REFERENCES `Agendas` (`Agenda_id`),
  CONSTRAINT `AgendasAlimentos_Alimento_id_53922b70_fk_Alimentos_Alimento_id` FOREIGN KEY (`Alimento_id`) REFERENCES `Alimentos` (`Alimento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AgendasAlimentos`
--

LOCK TABLES `AgendasAlimentos` WRITE;
/*!40000 ALTER TABLE `AgendasAlimentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `AgendasAlimentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AgendasBanhos`
--

DROP TABLE IF EXISTS `AgendasBanhos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AgendasBanhos` (
  `AgendaBanho_id` int NOT NULL AUTO_INCREMENT,
  `DiaHoraRegistro` datetime(6) NOT NULL,
  `Hora` time(6) NOT NULL,
  `Agenda_id` int NOT NULL,
  PRIMARY KEY (`AgendaBanho_id`),
  KEY `AgendasBanhos_Agenda_id_7b5f4ba3_fk_Agendas_Agenda_id` (`Agenda_id`),
  CONSTRAINT `AgendasBanhos_Agenda_id_7b5f4ba3_fk_Agendas_Agenda_id` FOREIGN KEY (`Agenda_id`) REFERENCES `Agendas` (`Agenda_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AgendasBanhos`
--

LOCK TABLES `AgendasBanhos` WRITE;
/*!40000 ALTER TABLE `AgendasBanhos` DISABLE KEYS */;
/*!40000 ALTER TABLE `AgendasBanhos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AgendasFisiologias`
--

DROP TABLE IF EXISTS `AgendasFisiologias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AgendasFisiologias` (
  `AgendaAlimento_id` int NOT NULL AUTO_INCREMENT,
  `DiaHoraRegistro` datetime(6) NOT NULL,
  `Fisiologia` varchar(1) NOT NULL,
  `Hora` time(6) NOT NULL,
  `Agenda_id` int NOT NULL,
  PRIMARY KEY (`AgendaAlimento_id`),
  KEY `AgendasFisiologias_Agenda_id_36ef74f3_fk_Agendas_Agenda_id` (`Agenda_id`),
  CONSTRAINT `AgendasFisiologias_Agenda_id_36ef74f3_fk_Agendas_Agenda_id` FOREIGN KEY (`Agenda_id`) REFERENCES `Agendas` (`Agenda_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AgendasFisiologias`
--

LOCK TABLES `AgendasFisiologias` WRITE;
/*!40000 ALTER TABLE `AgendasFisiologias` DISABLE KEYS */;
/*!40000 ALTER TABLE `AgendasFisiologias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AgendasItens`
--

DROP TABLE IF EXISTS `AgendasItens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AgendasItens` (
  `AgendaAlimento_id` int NOT NULL AUTO_INCREMENT,
  `DiaHoraRegistro` datetime(6) NOT NULL,
  `Agenda_id` int NOT NULL,
  `Item_id` int NOT NULL,
  PRIMARY KEY (`AgendaAlimento_id`),
  KEY `AgendasItens_Agenda_id_268cf94e_fk_Agendas_Agenda_id` (`Agenda_id`),
  KEY `AgendasItens_Item_id_93bdbc62_fk_Itens_Item_id` (`Item_id`),
  CONSTRAINT `AgendasItens_Agenda_id_268cf94e_fk_Agendas_Agenda_id` FOREIGN KEY (`Agenda_id`) REFERENCES `Agendas` (`Agenda_id`),
  CONSTRAINT `AgendasItens_Item_id_93bdbc62_fk_Itens_Item_id` FOREIGN KEY (`Item_id`) REFERENCES `Itens` (`Item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AgendasItens`
--

LOCK TABLES `AgendasItens` WRITE;
/*!40000 ALTER TABLE `AgendasItens` DISABLE KEYS */;
/*!40000 ALTER TABLE `AgendasItens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AgendasMedicamentos`
--

DROP TABLE IF EXISTS `AgendasMedicamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AgendasMedicamentos` (
  `AgendaMedicamento_id` int NOT NULL AUTO_INCREMENT,
  `DiaHoraRegistro` datetime(6) NOT NULL,
  `Hora` time(6) NOT NULL,
  `PosologiaAdministrada` varchar(50) NOT NULL,
  `Agenda_id` int NOT NULL,
  `Prescricao_id` int NOT NULL,
  PRIMARY KEY (`AgendaMedicamento_id`),
  KEY `AgendasMedicamentos_Agenda_id_7c44d34b_fk_Agendas_Agenda_id` (`Agenda_id`),
  KEY `AgendasMedicamentos_Prescricao_id_7957f628_fk_Prescrico` (`Prescricao_id`),
  CONSTRAINT `AgendasMedicamentos_Agenda_id_7c44d34b_fk_Agendas_Agenda_id` FOREIGN KEY (`Agenda_id`) REFERENCES `Agendas` (`Agenda_id`),
  CONSTRAINT `AgendasMedicamentos_Prescricao_id_7957f628_fk_Prescrico` FOREIGN KEY (`Prescricao_id`) REFERENCES `Prescricoes` (`Prescricao_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AgendasMedicamentos`
--

LOCK TABLES `AgendasMedicamentos` WRITE;
/*!40000 ALTER TABLE `AgendasMedicamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `AgendasMedicamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AgendasRecados`
--

DROP TABLE IF EXISTS `AgendasRecados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AgendasRecados` (
  `AgendaRecado_id` int NOT NULL AUTO_INCREMENT,
  `DiaHoraRegistro` datetime(6) NOT NULL,
  `Recado` longtext NOT NULL,
  `Agenda_id` int NOT NULL,
  PRIMARY KEY (`AgendaRecado_id`),
  KEY `AgendasRecados_Agenda_id_e6b82770_fk_Agendas_Agenda_id` (`Agenda_id`),
  CONSTRAINT `AgendasRecados_Agenda_id_e6b82770_fk_Agendas_Agenda_id` FOREIGN KEY (`Agenda_id`) REFERENCES `Agendas` (`Agenda_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AgendasRecados`
--

LOCK TABLES `AgendasRecados` WRITE;
/*!40000 ALTER TABLE `AgendasRecados` DISABLE KEYS */;
/*!40000 ALTER TABLE `AgendasRecados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AgendasSonos`
--

DROP TABLE IF EXISTS `AgendasSonos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AgendasSonos` (
  `AgendaSono_id` int NOT NULL AUTO_INCREMENT,
  `DiaHoraRegistro` datetime(6) NOT NULL,
  `Inicio` time(6) NOT NULL,
  `Fim` time(6) NOT NULL,
  `Agenda_id` int NOT NULL,
  PRIMARY KEY (`AgendaSono_id`),
  KEY `AgendasSonos_Agenda_id_97675da5_fk_Agendas_Agenda_id` (`Agenda_id`),
  CONSTRAINT `AgendasSonos_Agenda_id_97675da5_fk_Agendas_Agenda_id` FOREIGN KEY (`Agenda_id`) REFERENCES `Agendas` (`Agenda_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AgendasSonos`
--

LOCK TABLES `AgendasSonos` WRITE;
/*!40000 ALTER TABLE `AgendasSonos` DISABLE KEYS */;
/*!40000 ALTER TABLE `AgendasSonos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Alimentos`
--

DROP TABLE IF EXISTS `Alimentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Alimentos` (
  `Alimento_id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) NOT NULL,
  `Descricao` varchar(150) NOT NULL,
  PRIMARY KEY (`Alimento_id`),
  UNIQUE KEY `Nome` (`Nome`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Alimentos`
--

LOCK TABLES `Alimentos` WRITE;
/*!40000 ALTER TABLE `Alimentos` DISABLE KEYS */;
INSERT INTO `Alimentos` VALUES (1,'Banana','Banana');
/*!40000 ALTER TABLE `Alimentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Alunos`
--

DROP TABLE IF EXISTS `Alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Alunos` (
  `Aluno_id` int NOT NULL AUTO_INCREMENT,
  `Pessoa_id` int NOT NULL,
  PRIMARY KEY (`Aluno_id`),
  UNIQUE KEY `Pessoa_id` (`Pessoa_id`),
  KEY `Alunos_Pessoa_id_f0269ff9_fk_Pessoas_Pessoa_id` (`Pessoa_id`),
  CONSTRAINT `Alunos_Pessoa_id_f0269ff9_fk_Pessoas_Pessoa_id` FOREIGN KEY (`Pessoa_id`) REFERENCES `Pessoas` (`Pessoa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Alunos`
--

LOCK TABLES `Alunos` WRITE;
/*!40000 ALTER TABLE `Alunos` DISABLE KEYS */;
INSERT INTO `Alunos` VALUES (1,1),(2,5),(3,8);
/*!40000 ALTER TABLE `Alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Itens`
--

DROP TABLE IF EXISTS `Itens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Itens` (
  `Item_id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) NOT NULL,
  `Descricao` varchar(150) NOT NULL,
  PRIMARY KEY (`Item_id`),
  UNIQUE KEY `Nome` (`Nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Itens`
--

LOCK TABLES `Itens` WRITE;
/*!40000 ALTER TABLE `Itens` DISABLE KEYS */;
/*!40000 ALTER TABLE `Itens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Matriculas`
--

DROP TABLE IF EXISTS `Matriculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Matriculas` (
  `Matricula_id` int NOT NULL AUTO_INCREMENT,
  `Aluno_id` int NOT NULL,
  `Turma_id` int NOT NULL,
  PRIMARY KEY (`Matricula_id`),
  KEY `Matriculas_Aluno_id_7bef2b1a_fk_Alunos_Aluno_id` (`Aluno_id`),
  KEY `Matriculas_Turma_id_d0e106e9_fk_Turmas_TurmaId` (`Turma_id`),
  CONSTRAINT `Matriculas_Aluno_id_7bef2b1a_fk_Alunos_Aluno_id` FOREIGN KEY (`Aluno_id`) REFERENCES `Alunos` (`Aluno_id`),
  CONSTRAINT `Matriculas_Turma_id_d0e106e9_fk_Turmas_TurmaId` FOREIGN KEY (`Turma_id`) REFERENCES `Turmas` (`TurmaId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Matriculas`
--

LOCK TABLES `Matriculas` WRITE;
/*!40000 ALTER TABLE `Matriculas` DISABLE KEYS */;
INSERT INTO `Matriculas` VALUES (1,1,1),(2,2,1);
/*!40000 ALTER TABLE `Matriculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medicamentos`
--

DROP TABLE IF EXISTS `Medicamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medicamentos` (
  `Medicamento_id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) NOT NULL,
  `Descricao` varchar(150) NOT NULL,
  PRIMARY KEY (`Medicamento_id`),
  UNIQUE KEY `Nome` (`Nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medicamentos`
--

LOCK TABLES `Medicamentos` WRITE;
/*!40000 ALTER TABLE `Medicamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `Medicamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MensalidadesMatriculas`
--

DROP TABLE IF EXISTS `MensalidadesMatriculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MensalidadesMatriculas` (
  `MensalidadeMatricula_id` int NOT NULL,
  `Matricula_id` int NOT NULL,
  `Mes` datetime NOT NULL,
  PRIMARY KEY (`MensalidadeMatricula_id`),
  KEY `Ref1228` (`Matricula_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MensalidadesMatriculas`
--

LOCK TABLES `MensalidadesMatriculas` WRITE;
/*!40000 ALTER TABLE `MensalidadesMatriculas` DISABLE KEYS */;
/*!40000 ALTER TABLE `MensalidadesMatriculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pessoas`
--

DROP TABLE IF EXISTS `Pessoas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pessoas` (
  `Pessoa_id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) DEFAULT NULL,
  `Apelido` varchar(50) DEFAULT NULL,
  `DataNascimento` date DEFAULT NULL,
  `CPF` varchar(14) DEFAULT NULL,
  `RG` varchar(11) DEFAULT NULL,
  `Usuario_id` int NOT NULL,
  `Telefone` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`Pessoa_id`),
  UNIQUE KEY `Pessoas_Usuario_id_6bdf1e2c_uniq` (`Usuario_id`),
  UNIQUE KEY `Nome` (`Nome`),
  CONSTRAINT `Pessoas_Usuario_id_6bdf1e2c_fk_auth_user_id` FOREIGN KEY (`Usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pessoas`
--

LOCK TABLES `Pessoas` WRITE;
/*!40000 ALTER TABLE `Pessoas` DISABLE KEYS */;
INSERT INTO `Pessoas` VALUES (1,'Pedro Antonio Mano','Pê','2022-06-06','12310307807','18',2,'11'),(2,'Marco Antonio Mano','Chucrute','2004-05-29','12310307807','12',3,'11'),(3,NULL,NULL,NULL,NULL,NULL,4,NULL),(4,NULL,NULL,NULL,NULL,NULL,5,NULL),(5,'Alexandre Pimentel','Alex','1975-01-01','12310307807','15151',6,'50505050'),(6,'Luis Sotovia','Luis','1960-01-18','36050184836','123452332',7,'(19)991766912'),(7,'Marcelo Batista','Marcelo','1972-09-04','14018811810','21630543',8,'11999348819'),(8,'Geovanio Lima','geovanio','1975-07-25','15463673810','254130276',9,'19 997320144'),(9,'Antonio Carlos Mano','Mano','1968-10-15','12310307807','123456',10,'123456');
/*!40000 ALTER TABLE `Pessoas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prescricoes`
--

DROP TABLE IF EXISTS `Prescricoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Prescricoes` (
  `Prescricao_id` int NOT NULL AUTO_INCREMENT,
  `DataInicial` date NOT NULL,
  `DataFinal` date NOT NULL,
  `Posologia` longtext NOT NULL,
  `Horarios` longtext NOT NULL,
  `Aluno_id` int NOT NULL,
  `Medicamento_id` int NOT NULL,
  PRIMARY KEY (`Prescricao_id`),
  KEY `Prescricoes_Medicamento_id_c2be92d3_fk_Medicamen` (`Medicamento_id`),
  KEY `Prescricoes_Aluno_id_af30f4ad_fk_Alunos_Aluno_id` (`Aluno_id`),
  CONSTRAINT `Prescricoes_Aluno_id_af30f4ad_fk_Alunos_Aluno_id` FOREIGN KEY (`Aluno_id`) REFERENCES `Alunos` (`Aluno_id`),
  CONSTRAINT `Prescricoes_Medicamento_id_c2be92d3_fk_Medicamen` FOREIGN KEY (`Medicamento_id`) REFERENCES `Medicamentos` (`Medicamento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prescricoes`
--

LOCK TABLES `Prescricoes` WRITE;
/*!40000 ALTER TABLE `Prescricoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `Prescricoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Professores`
--

DROP TABLE IF EXISTS `Professores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Professores` (
  `Professor_id` int NOT NULL AUTO_INCREMENT,
  `Pessoa_id` int NOT NULL,
  PRIMARY KEY (`Professor_id`),
  UNIQUE KEY `Pessoa_id` (`Pessoa_id`),
  KEY `Professores_Pessoa_id_e1c3b8a3_fk_Pessoas_Pessoa_id` (`Pessoa_id`),
  CONSTRAINT `Professores_Pessoa_id_e1c3b8a3_fk_Pessoas_Pessoa_id` FOREIGN KEY (`Pessoa_id`) REFERENCES `Pessoas` (`Pessoa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Professores`
--

LOCK TABLES `Professores` WRITE;
/*!40000 ALTER TABLE `Professores` DISABLE KEYS */;
INSERT INTO `Professores` VALUES (1,2);
/*!40000 ALTER TABLE `Professores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Responsaveis`
--

DROP TABLE IF EXISTS `Responsaveis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Responsaveis` (
  `Responsavel_id` int NOT NULL AUTO_INCREMENT,
  `Pessoa_id` int NOT NULL,
  PRIMARY KEY (`Responsavel_id`),
  UNIQUE KEY `Pessoa_id` (`Pessoa_id`),
  KEY `Responsaveis_Pessoa_id_c8c54a45_fk_Pessoas_Pessoa_id` (`Pessoa_id`),
  CONSTRAINT `Responsaveis_Pessoa_id_c8c54a45_fk_Pessoas_Pessoa_id` FOREIGN KEY (`Pessoa_id`) REFERENCES `Pessoas` (`Pessoa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Responsaveis`
--

LOCK TABLES `Responsaveis` WRITE;
/*!40000 ALTER TABLE `Responsaveis` DISABLE KEYS */;
INSERT INTO `Responsaveis` VALUES (3,8),(1,9);
/*!40000 ALTER TABLE `Responsaveis` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`AEadmin`@`%`*/ /*!50003 TRIGGER `insResp` AFTER INSERT ON `Responsaveis` FOR EACH ROW BEGIN 
  set @tt_json = ( select  json_object ( 'cpf', Pessoas.cpf, 'nome', Pessoas.nome ) from  Pessoas where Pessoas.Pessoa_Id = new.Pessoa_Id limit 1 );
  set @tt_resu = ( select http_post ( 'http://192.168.1.136:3000/sacado', @tt_json ) );
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ResponsaveisAlunos`
--

DROP TABLE IF EXISTS `ResponsaveisAlunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ResponsaveisAlunos` (
  `ResponsavelAluno_id` int NOT NULL AUTO_INCREMENT,
  `Aluno_id` int NOT NULL,
  `Responsavel_id` int NOT NULL,
  PRIMARY KEY (`ResponsavelAluno_id`),
  KEY `ResponsaveisAlunos_Aluno_id_dcdf6898_fk_Alunos_Aluno_id` (`Aluno_id`),
  KEY `ResponsaveisAlunos_Responsavel_id_15fb47d9_fk_Responsav` (`Responsavel_id`),
  CONSTRAINT `ResponsaveisAlunos_Aluno_id_dcdf6898_fk_Alunos_Aluno_id` FOREIGN KEY (`Aluno_id`) REFERENCES `Alunos` (`Aluno_id`),
  CONSTRAINT `ResponsaveisAlunos_Responsavel_id_15fb47d9_fk_Responsav` FOREIGN KEY (`Responsavel_id`) REFERENCES `Responsaveis` (`Responsavel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ResponsaveisAlunos`
--

LOCK TABLES `ResponsaveisAlunos` WRITE;
/*!40000 ALTER TABLE `ResponsaveisAlunos` DISABLE KEYS */;
INSERT INTO `ResponsaveisAlunos` VALUES (1,1,1),(2,2,1);
/*!40000 ALTER TABLE `ResponsaveisAlunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ResponsaveisMensalidades`
--

DROP TABLE IF EXISTS `ResponsaveisMensalidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ResponsaveisMensalidades` (
  `ResponsavelMensalidade_id` int NOT NULL AUTO_INCREMENT,
  `Matricula_id` int NOT NULL,
  `ResponsavelAluno_id` int NOT NULL,
  PRIMARY KEY (`ResponsavelMensalidade_id`),
  KEY `ResponsaveisMensalid_Matricula_id_fa981159_fk_Matricula` (`Matricula_id`),
  KEY `ResponsaveisMensalid_ResponsavelAluno_id_5181bfd9_fk_Responsav` (`ResponsavelAluno_id`),
  CONSTRAINT `ResponsaveisMensalid_Matricula_id_fa981159_fk_Matricula` FOREIGN KEY (`Matricula_id`) REFERENCES `Matriculas` (`Matricula_id`),
  CONSTRAINT `ResponsaveisMensalid_ResponsavelAluno_id_5181bfd9_fk_Responsav` FOREIGN KEY (`ResponsavelAluno_id`) REFERENCES `ResponsaveisAlunos` (`ResponsavelAluno_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ResponsaveisMensalidades`
--

LOCK TABLES `ResponsaveisMensalidades` WRITE;
/*!40000 ALTER TABLE `ResponsaveisMensalidades` DISABLE KEYS */;
INSERT INTO `ResponsaveisMensalidades` VALUES (4,1,1),(7,2,1);
/*!40000 ALTER TABLE `ResponsaveisMensalidades` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`AEadmin`@`%`*/ /*!50003 TRIGGER `ResponsaveisMensalidades_After_Insert` AFTER INSERT ON `ResponsaveisMensalidades` FOR EACH ROW BEGIN
  call TitulosBancariosCria ( NEW.Matricula_id ) ;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `TabelasPrecos`
--

DROP TABLE IF EXISTS `TabelasPrecos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TabelasPrecos` (
  `TabelaPrecoId` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) NOT NULL,
  `Valor` decimal(6,2) NOT NULL,
  PRIMARY KEY (`TabelaPrecoId`),
  UNIQUE KEY `Nome` (`Nome`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TabelasPrecos`
--

LOCK TABLES `TabelasPrecos` WRITE;
/*!40000 ALTER TABLE `TabelasPrecos` DISABLE KEYS */;
INSERT INTO `TabelasPrecos` VALUES (1,'tabela teste alterada',1500.00),(2,'tabela teste',1000.00);
/*!40000 ALTER TABLE `TabelasPrecos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TitulosBancarios`
--

DROP TABLE IF EXISTS `TitulosBancarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TitulosBancarios` (
  `TituloBancario_id` int NOT NULL AUTO_INCREMENT,
  `Vencimento` date NOT NULL,
  `Valor` decimal(10,2) NOT NULL,
  `Pagamento` date DEFAULT NULL,
  `NumeroBancario` varchar(20) DEFAULT NULL,
  `Matricula_id` int NOT NULL,
  `ResponsavelMensalidade_id` int NOT NULL,
  PRIMARY KEY (`TituloBancario_id`),
  KEY `TitulosBancarios_Matricula_id_7c4d1800_fk_Matricula` (`Matricula_id`),
  KEY `TitulosBancarios_ResponsavelMensalida_71fa64cc_fk_Responsav` (`ResponsavelMensalidade_id`),
  KEY `TitulosBancarios_Vencimento_d9b79d6f` (`Vencimento`),
  KEY `TitulosBancarios_Pagamento_03443780` (`Pagamento`),
  CONSTRAINT `TitulosBancarios_Matricula_id_7c4d1800_fk_Matricula` FOREIGN KEY (`Matricula_id`) REFERENCES `Matriculas` (`Matricula_id`),
  CONSTRAINT `TitulosBancarios_ResponsavelMensalida_71fa64cc_fk_Responsav` FOREIGN KEY (`ResponsavelMensalidade_id`) REFERENCES `ResponsaveisMensalidades` (`ResponsavelMensalidade_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TitulosBancarios`
--

LOCK TABLES `TitulosBancarios` WRITE;
/*!40000 ALTER TABLE `TitulosBancarios` DISABLE KEYS */;
INSERT INTO `TitulosBancarios` VALUES (1,'2022-01-01',1500.00,NULL,NULL,1,4),(2,'2022-02-01',1500.00,NULL,NULL,1,4),(3,'2022-03-01',1500.00,NULL,NULL,1,4),(4,'2022-04-01',1500.00,NULL,NULL,1,4),(5,'2022-05-01',1500.00,NULL,NULL,1,4),(6,'2022-06-01',1500.00,NULL,NULL,1,4),(7,'2022-07-01',1500.00,NULL,NULL,1,4),(8,'2022-08-01',1500.00,NULL,NULL,1,4),(9,'2022-09-01',1500.00,NULL,NULL,1,4),(10,'2022-10-01',1500.00,NULL,NULL,1,4),(11,'2022-11-01',1500.00,NULL,NULL,1,4),(12,'2022-12-01',1500.00,NULL,NULL,1,4),(13,'2022-01-01',1500.00,NULL,NULL,2,7),(14,'2022-02-01',1500.00,NULL,NULL,2,7),(15,'2022-03-01',1500.00,NULL,NULL,2,7),(16,'2022-04-01',1500.00,NULL,NULL,2,7),(17,'2022-05-01',1500.00,NULL,NULL,2,7),(18,'2022-06-01',1500.00,NULL,NULL,2,7),(19,'2022-07-01',1500.00,NULL,NULL,2,7),(20,'2022-08-01',1500.00,NULL,NULL,2,7),(21,'2022-09-01',1500.00,NULL,NULL,2,7),(22,'2022-10-01',1500.00,NULL,NULL,2,7),(23,'2022-11-01',1500.00,NULL,NULL,2,7),(24,'2022-12-01',1500.00,NULL,NULL,2,7);
/*!40000 ALTER TABLE `TitulosBancarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TitulosPagos`
--

DROP TABLE IF EXISTS `TitulosPagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TitulosPagos` (
  `TituloPago_id` int NOT NULL,
  `TituloBancario_id` int NOT NULL,
  `DataPagamento` date NOT NULL,
  `Valor` decimal(10,2) NOT NULL,
  PRIMARY KEY (`TituloPago_id`),
  KEY `Ref2630` (`TituloBancario_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TitulosPagos`
--

LOCK TABLES `TitulosPagos` WRITE;
/*!40000 ALTER TABLE `TitulosPagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `TitulosPagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Turmas`
--

DROP TABLE IF EXISTS `Turmas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Turmas` (
  `TurmaId` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) NOT NULL,
  `AnoLetivo` int NOT NULL,
  `AnoEscolar` int NOT NULL,
  PRIMARY KEY (`TurmaId`),
  UNIQUE KEY `Nome` (`Nome`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Turmas`
--

LOCK TABLES `Turmas` WRITE;
/*!40000 ALTER TABLE `Turmas` DISABLE KEYS */;
INSERT INTO `Turmas` VALUES (1,'Fundamental 1',2022,1);
/*!40000 ALTER TABLE `Turmas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TurmasProfessores`
--

DROP TABLE IF EXISTS `TurmasProfessores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TurmasProfessores` (
  `TurmaProfessor_id` int NOT NULL AUTO_INCREMENT,
  `Professor_id` int NOT NULL,
  `Turma_id` int NOT NULL,
  PRIMARY KEY (`TurmaProfessor_id`),
  KEY `TurmasProfessores_Professor_id_c031cd3c_fk_Professor` (`Professor_id`),
  KEY `TurmasProfessores_Turma_id_1712fa57_fk_Turmas_TurmaId` (`Turma_id`),
  CONSTRAINT `TurmasProfessores_Professor_id_c031cd3c_fk_Professor` FOREIGN KEY (`Professor_id`) REFERENCES `Professores` (`Professor_id`),
  CONSTRAINT `TurmasProfessores_Turma_id_1712fa57_fk_Turmas_TurmaId` FOREIGN KEY (`Turma_id`) REFERENCES `Turmas` (`TurmaId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TurmasProfessores`
--

LOCK TABLES `TurmasProfessores` WRITE;
/*!40000 ALTER TABLE `TurmasProfessores` DISABLE KEYS */;
INSERT INTO `TurmasProfessores` VALUES (1,1,1);
/*!40000 ALTER TABLE `TurmasProfessores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TurmasTabelas`
--

DROP TABLE IF EXISTS `TurmasTabelas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TurmasTabelas` (
  `TurmaTabela_id` int NOT NULL AUTO_INCREMENT,
  `Tabela_id` int NOT NULL,
  `Turma_id` int NOT NULL,
  PRIMARY KEY (`TurmaTabela_id`),
  KEY `TurmasTabelas_Tabela_id_3b8e40b1_fk_TabelasPrecos_TabelaPrecoId` (`Tabela_id`),
  KEY `TurmasTabelas_Turma_id_5cfa8cbc_fk_Turmas_TurmaId` (`Turma_id`),
  CONSTRAINT `TurmasTabelas_Tabela_id_3b8e40b1_fk_TabelasPrecos_TabelaPrecoId` FOREIGN KEY (`Tabela_id`) REFERENCES `TabelasPrecos` (`TabelaPrecoId`),
  CONSTRAINT `TurmasTabelas_Turma_id_5cfa8cbc_fk_Turmas_TurmaId` FOREIGN KEY (`Turma_id`) REFERENCES `Turmas` (`TurmaId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TurmasTabelas`
--

LOCK TABLES `TurmasTabelas` WRITE;
/*!40000 ALTER TABLE `TurmasTabelas` DISABLE KEYS */;
INSERT INTO `TurmasTabelas` VALUES (1,1,1);
/*!40000 ALTER TABLE `TurmasTabelas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TurmasTabelasPrecos`
--

DROP TABLE IF EXISTS `TurmasTabelasPrecos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TurmasTabelasPrecos` (
  `TurmaTabelaPreco_id` int NOT NULL AUTO_INCREMENT,
  `Valor` decimal(6,2) NOT NULL,
  `Turma_id` int NOT NULL,
  PRIMARY KEY (`TurmaTabelaPreco_id`),
  KEY `TurmasTabelasPrecos_Turma_id_772d7144_fk_Turmas_TurmaId` (`Turma_id`),
  CONSTRAINT `TurmasTabelasPrecos_Turma_id_772d7144_fk_Turmas_TurmaId` FOREIGN KEY (`Turma_id`) REFERENCES `Turmas` (`TurmaId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TurmasTabelasPrecos`
--

LOCK TABLES `TurmasTabelasPrecos` WRITE;
/*!40000 ALTER TABLE `TurmasTabelasPrecos` DISABLE KEYS */;
/*!40000 ALTER TABLE `TurmasTabelasPrecos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Convidados');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Agenda',7,'add_agendas'),(26,'Can change Agenda',7,'change_agendas'),(27,'Can delete Agenda',7,'delete_agendas'),(28,'Can view Agenda',7,'view_agendas'),(29,'Can add Alimento',8,'add_alimentos'),(30,'Can change Alimento',8,'change_alimentos'),(31,'Can delete Alimento',8,'delete_alimentos'),(32,'Can view Alimento',8,'view_alimentos'),(33,'Can add Aluno',9,'add_alunos'),(34,'Can change Aluno',9,'change_alunos'),(35,'Can delete Aluno',9,'delete_alunos'),(36,'Can view Aluno',9,'view_alunos'),(37,'Can add Item',10,'add_itens'),(38,'Can change Item',10,'change_itens'),(39,'Can delete Item',10,'delete_itens'),(40,'Can view Item',10,'view_itens'),(41,'Can add Medicamento',11,'add_medicamentos'),(42,'Can change Medicamento',11,'change_medicamentos'),(43,'Can delete Medicamento',11,'delete_medicamentos'),(44,'Can view Medicamento',11,'view_medicamentos'),(45,'Can add Pessoa',12,'add_pessoas'),(46,'Can change Pessoa',12,'change_pessoas'),(47,'Can delete Pessoa',12,'delete_pessoas'),(48,'Can view Pessoa',12,'view_pessoas'),(49,'Can add Professor',13,'add_professores'),(50,'Can change Professor',13,'change_professores'),(51,'Can delete Professor',13,'delete_professores'),(52,'Can view Professor',13,'view_professores'),(53,'Can add Responsavel',14,'add_responsaveis'),(54,'Can change Responsavel',14,'change_responsaveis'),(55,'Can delete Responsavel',14,'delete_responsaveis'),(56,'Can view Responsavel',14,'view_responsaveis'),(57,'Can add Turma',15,'add_turmas'),(58,'Can change Turma',15,'change_turmas'),(59,'Can delete Turma',15,'delete_turmas'),(60,'Can view Turma',15,'view_turmas'),(61,'Can add Professor da Turma',16,'add_turmasprofessores'),(62,'Can change Professor da Turma',16,'change_turmasprofessores'),(63,'Can delete Professor da Turma',16,'delete_turmasprofessores'),(64,'Can view Professor da Turma',16,'view_turmasprofessores'),(65,'Can add Responsavel pelo Aluno',17,'add_responsaveisalunos'),(66,'Can change Responsavel pelo Aluno',17,'change_responsaveisalunos'),(67,'Can delete Responsavel pelo Aluno',17,'delete_responsaveisalunos'),(68,'Can view Responsavel pelo Aluno',17,'view_responsaveisalunos'),(69,'Can add Prescrição',18,'add_prescricoes'),(70,'Can change Prescrição',18,'change_prescricoes'),(71,'Can delete Prescrição',18,'delete_prescricoes'),(72,'Can view Prescrição',18,'view_prescricoes'),(73,'Can add Matrícula',19,'add_matriculas'),(74,'Can change Matrícula',19,'change_matriculas'),(75,'Can delete Matrícula',19,'delete_matriculas'),(76,'Can view Matrícula',19,'view_matriculas'),(77,'Can add Sono da Agenda',20,'add_agendassonos'),(78,'Can change Sono da Agenda',20,'change_agendassonos'),(79,'Can delete Sono da Agenda',20,'delete_agendassonos'),(80,'Can view Sono da Agenda',20,'view_agendassonos'),(81,'Can add Recado da Agenda',21,'add_agendasrecados'),(82,'Can change Recado da Agenda',21,'change_agendasrecados'),(83,'Can delete Recado da Agenda',21,'delete_agendasrecados'),(84,'Can view Recado da Agenda',21,'view_agendasrecados'),(85,'Can add Medicamento da Agenda',22,'add_agendasmedicamentos'),(86,'Can change Medicamento da Agenda',22,'change_agendasmedicamentos'),(87,'Can delete Medicamento da Agenda',22,'delete_agendasmedicamentos'),(88,'Can view Medicamento da Agenda',22,'view_agendasmedicamentos'),(89,'Can add Item da Agenda',23,'add_agendasitens'),(90,'Can change Item da Agenda',23,'change_agendasitens'),(91,'Can delete Item da Agenda',23,'delete_agendasitens'),(92,'Can view Item da Agenda',23,'view_agendasitens'),(93,'Can add Fisiologia da Agenda',24,'add_agendasfisiologias'),(94,'Can change Fisiologia da Agenda',24,'change_agendasfisiologias'),(95,'Can delete Fisiologia da Agenda',24,'delete_agendasfisiologias'),(96,'Can view Fisiologia da Agenda',24,'view_agendasfisiologias'),(97,'Can add Banho da Agenda',25,'add_agendasbanhos'),(98,'Can change Banho da Agenda',25,'change_agendasbanhos'),(99,'Can delete Banho da Agenda',25,'delete_agendasbanhos'),(100,'Can view Banho da Agenda',25,'view_agendasbanhos'),(101,'Can add Alimento da Agenda',26,'add_agendasalimentos'),(102,'Can change Alimento da Agenda',26,'change_agendasalimentos'),(103,'Can delete Alimento da Agenda',26,'delete_agendasalimentos'),(104,'Can view Alimento da Agenda',26,'view_agendasalimentos'),(105,'Can add Tabela de Preços',27,'add_turmastabelasprecos'),(106,'Can change Tabela de Preços',27,'change_turmastabelasprecos'),(107,'Can delete Tabela de Preços',27,'delete_turmastabelasprecos'),(108,'Can view Tabela de Preços',27,'view_turmastabelasprecos'),(109,'Can add Tabela',28,'add_tabelasprecos'),(110,'Can change Tabela',28,'change_tabelasprecos'),(111,'Can delete Tabela',28,'delete_tabelasprecos'),(112,'Can view Tabela',28,'view_tabelasprecos'),(113,'Can add Tabela de Preços da Turma',29,'add_turmastabelas'),(114,'Can change Tabela de Preços da Turma',29,'change_turmastabelas'),(115,'Can delete Tabela de Preços da Turma',29,'delete_turmastabelas'),(116,'Can view Tabela de Preços da Turma',29,'view_turmastabelas'),(117,'Can add Compromisso financeiro do responsável',30,'add_responsaveismensalidades'),(118,'Can change Compromisso financeiro do responsável',30,'change_responsaveismensalidades'),(119,'Can delete Compromisso financeiro do responsável',30,'delete_responsaveismensalidades'),(120,'Can view Compromisso financeiro do responsável',30,'view_responsaveismensalidades'),(121,'Can add Mensalidade',31,'add_titulosbancarios'),(122,'Can change Mensalidade',31,'change_titulosbancarios'),(123,'Can delete Mensalidade',31,'delete_titulosbancarios'),(124,'Can view Mensalidade',31,'view_titulosbancarios');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$JSzWfeOndvsHngqiEl9UHT$ifv0tLd7dlRq3sjMKpyNc5ciHFjdZA3TbEP2YlFZJlU=','2022-06-19 02:00:46.834761',1,'AEadmin','','','antonio.mano@gmail.com',1,1,'2022-04-24 19:38:45.246291'),(2,'pbkdf2_sha256$260000$FCllsJQ1JbYmqnvRKjgvZM$4b4Oma3PRZE4lva7Ozip0W9I05BtSlrjATr8FAxdmMw=','2022-04-24 20:14:37.814542',0,'Pedro','','','pedro@gmail.com',0,1,'2022-04-24 19:55:31.693696'),(3,'pbkdf2_sha256$260000$QlrcDbefKp7mN5ymsY6sJh$WKO1fBuQH8P8J31eSb51TPnJfkWbrn0Mldls89J19q4=','2022-04-24 20:14:56.689135',0,'Marco','','','marco@gmail.com',0,1,'2022-04-24 20:08:49.859144'),(4,'pbkdf2_sha256$260000$BpAWRyyraEaiZ53Gdo1Om6$HxPf73nCptE1LhB6s5ex356KFllyxNPSGOLqZpklu/k=','2022-04-25 12:33:07.157773',0,'10Alex06@','','','alepimentel@uol.com.br',0,1,'2022-04-25 12:03:15.762987'),(5,'pbkdf2_sha256$260000$Q86WS2E8ODMRtpJOn1sSW7$IOrTz+HH3Xg3b8wcgW7pHzGKaSdjlkwRLm/QLb4OqLw=','2022-04-25 12:41:25.829500',0,'10Alex05@','','','alepimentel@bol.com.br',0,1,'2022-04-25 12:41:10.291876'),(6,'pbkdf2_sha256$260000$gk8TsKfjwGesrs58IkLZaY$/7VakODga7eis+uD4IoAU/OZOQvohRAvFXLr7OVIKj8=','2022-04-25 23:45:22.776154',0,'alexandre','','','alexandre@gmail.com',0,1,'2022-04-25 23:44:47.272734'),(7,'pbkdf2_sha256$260000$bXy4WYBvC4EIqk1s3GTjr6$LUSvkXW4tw+eaILu0/UX4Z2jh3r2jweBOgkGlrU98AY=','2022-04-25 23:45:38.260510',0,'LuisSotovia','','','sotovia@gmail.com',0,1,'2022-04-25 23:45:29.264403'),(8,'pbkdf2_sha256$260000$u7GoB2MIFwLNNCyMxbpsI8$p+jad+ZoPfpMvMU4RIG55Ha8k4qSYrAr0oBthb9/JJQ=','2022-04-28 23:11:33.900345',0,'Marcelo2022','','','marceloboliveira1580@gmail.com',0,1,'2022-04-27 00:43:13.258759'),(9,'pbkdf2_sha256$260000$jgM3Lkkashv6YdlVYeabLt$mAl2KFjikRqlfVH756s4KgJOmsvOaqVCQdqFqU8Y8GI=','2022-05-11 21:06:13.548797',0,'Geovaniolima','','','reparafibra@gmail.com',0,1,'2022-05-11 21:05:21.470024'),(10,'pbkdf2_sha256$260000$6XS6bgV1fX3YlolJwqqCB0$mg+uSrvlzkEYdX0qyGCmDyeRTF3uR6Hg3h5w0O00PwQ=','2022-06-14 22:56:44.336716',0,'mano','','','antonio.mano2@gmail.com',0,1,'2022-06-14 22:56:18.579263');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,3,1),(3,4,1),(4,5,1),(5,6,1),(6,7,1),(7,8,1),(8,9,1),(9,10,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-04-24 19:55:03.724698','1','Convidados',1,'[{\"added\": {}}]',3,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'Cadastros','agendas'),(26,'Cadastros','agendasalimentos'),(25,'Cadastros','agendasbanhos'),(24,'Cadastros','agendasfisiologias'),(23,'Cadastros','agendasitens'),(22,'Cadastros','agendasmedicamentos'),(21,'Cadastros','agendasrecados'),(20,'Cadastros','agendassonos'),(8,'Cadastros','alimentos'),(9,'Cadastros','alunos'),(10,'Cadastros','itens'),(19,'Cadastros','matriculas'),(11,'Cadastros','medicamentos'),(12,'Cadastros','pessoas'),(18,'Cadastros','prescricoes'),(13,'Cadastros','professores'),(14,'Cadastros','responsaveis'),(17,'Cadastros','responsaveisalunos'),(30,'Cadastros','responsaveismensalidades'),(28,'Cadastros','tabelasprecos'),(31,'Cadastros','titulosbancarios'),(15,'Cadastros','turmas'),(16,'Cadastros','turmasprofessores'),(29,'Cadastros','turmastabelas'),(5,'contenttypes','contenttype'),(27,'Financeiro','turmastabelasprecos'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-04-24 19:37:07.755971'),(2,'auth','0001_initial','2022-04-24 19:37:34.126395'),(3,'admin','0001_initial','2022-04-24 19:37:40.850572'),(4,'admin','0002_logentry_remove_auto_add','2022-04-24 19:37:41.006219'),(5,'admin','0003_logentry_add_action_flag_choices','2022-04-24 19:37:41.305760'),(6,'contenttypes','0002_remove_content_type_name','2022-04-24 19:37:45.958944'),(7,'auth','0002_alter_permission_name_max_length','2022-04-24 19:37:48.885757'),(8,'auth','0003_alter_user_email_max_length','2022-04-24 19:37:52.274247'),(9,'auth','0004_alter_user_username_opts','2022-04-24 19:37:52.461800'),(10,'auth','0005_alter_user_last_login_null','2022-04-24 19:37:55.063881'),(11,'auth','0006_require_contenttypes_0002','2022-04-24 19:37:55.310433'),(12,'auth','0007_alter_validators_add_error_messages','2022-04-24 19:37:55.448433'),(13,'auth','0008_alter_user_username_max_length','2022-04-24 19:37:58.410642'),(14,'auth','0009_alter_user_last_name_max_length','2022-04-24 19:38:01.118765'),(15,'auth','0010_alter_group_name_max_length','2022-04-24 19:38:03.822498'),(16,'auth','0011_update_proxy_permissions','2022-04-24 19:38:03.976633'),(17,'auth','0012_alter_user_first_name_max_length','2022-04-24 19:38:06.786314'),(18,'sessions','0001_initial','2022-04-24 19:38:08.829203'),(19,'Cadastros','0001_initial','2022-04-24 19:50:10.481514'),(20,'Cadastros','0002_auto_20211117_1857','2022-04-24 19:50:22.117630'),(21,'Cadastros','0003_auto_20211117_1959','2022-04-24 19:50:27.972058'),(22,'Cadastros','0004_rename_alunos_prescricoes_aluno','2022-04-24 19:50:32.500043'),(23,'Cadastros','0005_alter_pessoas_usuario','2022-04-24 19:50:32.807255'),(24,'Cadastros','0006_auto_20220424_1648','2022-04-24 19:50:33.164193'),(25,'Cadastros','0006_auto_20220605_1917','2022-06-05 22:17:26.106278'),(26,'Financeiro','0001_initial','2022-06-05 22:42:39.149967'),(27,'Financeiro','0002_rename_turmastabelasdeprecos_turmastabelasprecos','2022-06-05 22:42:39.309375'),(28,'Cadastros','0006_auto_20220613_2054','2022-06-13 23:54:11.805111'),(29,'Cadastros','0007_turmastabelas','2022-06-14 00:17:06.458500'),(30,'Cadastros','0008_responsaveismensalidades','2022-06-14 23:14:19.618523'),(31,'Cadastros','0009_rename_responsavel_responsaveismensalidades_responsavelaluno','2022-06-15 00:01:37.141464'),(32,'Cadastros','0010_titulosbancarios','2022-06-15 00:16:12.305071');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('78s3kql6jo85u13h4uu8q63855k84k88','.eJxVjEEOgjAQRe_StWmYMtOCS_eeoZlpp4IaSCisjHdXEha6_e-9_zKRt3WIW9UljtmcDZjT7yacHjrtIN95us02zdO6jGJ3xR602uuc9Xk53L-DgevwrQklFOeEChJ1bRDOqgkwkPjSNcDApSfIPSioT-gQOLTJY--oEXLm_QHg_Ddo:1o1Yok:gZ68PTbTlLsL7G5W5sglevC-w8ODsK96yGhbZmpN9Cw','2022-06-29 19:36:42.762991'),('fanxi7rt2j16etczh1oag8fp9cpy4u34','.eJxVjEEOwiAQRe_C2hA6giMu3XsGMgODVA0kpV0Z726bdKHb_977bxVomUtYukxhTOqiUB1-N6b4lLqB9KB6bzq2Ok8j603RO-361pK8rrv7d1Col7WO2QM7F711NhMNhCYZB5kwgfgTUBxAiP3RMkNmRLLi0Z3FGBdXrD5f_ME4Wg:1nj8Og:QxuG_6H5gBpI3uBfei-MAJSzcfk7Zd1BU5nu32wh_DQ','2022-05-09 23:45:38.403789'),('hiio4t6j11pz2be5is06qcgmte62o20b','.eJxVjEEOgjAQRe_StWmYMtOCS_eeoZlpp4IaSCisjHdXEha6_e-9_zKRt3WIW9UljtmcDZjT7yacHjrtIN95us02zdO6jGJ3xR602uuc9Xk53L-DgevwrQklFOeEChJ1bRDOqgkwkPjSNcDApSfIPSioT-gQOLTJY--oEXLm_QHg_Ddo:1notaB:gqIvt66HYCCTxFOgUbL5g_4-LLmClD00wG69oLnWeuE','2022-05-25 21:09:19.045480'),('i6e0rc1twjvhwgqitobe39qiu8uanx9k','.eJxVjEEOgjAQRe_StWmYMtOCS_eeoZlpp4IaSCisjHdXEha6_e-9_zKRt3WIW9UljtmcDZjT7yacHjrtIN95us02zdO6jGJ3xR602uuc9Xk53L-DgevwrQklFOeEChJ1bRDOqgkwkPjSNcDApSfIPSioT-gQOLTJY--oEXLm_QHg_Ddo:1o1ynw:-2AvApjj8c21I-SLwTFnF1h-t7yhpp-W0NIi0qKsI-Y','2022-06-30 23:21:36.052419'),('i8goaf6ddx1xc4v12pl6ns35cphr2wrm','.eJxVjDsOwjAQBe_iGlnZrD8xJX3OYO16LRxAjhQnFeLuyFIKaN_MvLeKdOwlHi1vcRF1VVZdfjem9My1A3lQva86rXXfFtZd0Sdtel4lv26n-3dQqJVeu8laSGwYWRLLkEmy925EdBiyAQ8heHDIOILFybkgYA2QNTQERPX5AtxLNrM:1niy1t:y7shbTx0hh54VS1DQyMzT9jtnFnYvP5g7uuvCHpR7sM','2022-05-09 12:41:25.975924'),('kn5cwcwedqrazi2yxm152mlylphazhi1','.eJxVjMsOwiAQRf-FtSF0YKbg0r3fQHgMUjU0Ke3K-O_apAvd3nPOfQkftrX6rfPipyzOQovT7xZDenDbQb6Hdptlmtu6TFHuijxol9c58_NyuH8HNfT6rQcGhwGVGamgpWzZKDRgNRULyY1JG0JM0cYEpWh2pMAYRWrgHABIvD-3kza_:1niidE:H1LeP5NnRwPIGGOlM8SmBrAGCBF8TsEt5gib2CnOyg4','2022-05-08 20:14:56.943227'),('p444vx1gybx0qr91n5roh0e2f2x6q2xm','.eJxVjEEOgjAQRe_StWmYMtOCS_eeoZlpp4IaSCisjHdXEha6_e-9_zKRt3WIW9UljtmcDZjT7yacHjrtIN95us02zdO6jGJ3xR602uuc9Xk53L-DgevwrQklFOeEChJ1bRDOqgkwkPjSNcDApSfIPSioT-gQOLTJY--oEXLm_QHg_Ddo:1o1FTT:KuhvWcwE7vVmgStQu1wCJFM1S8aYKfDOZ4CWcc3gTAc','2022-06-28 22:57:27.588489'),('spvqya44hnfag2rv8kqbfv066x0ah7lj','.eJxVjEEOgjAQRe_StWmYMtOCS_eeoZlpp4IaSCisjHdXEha6_e-9_zKRt3WIW9UljtmcDZjT7yacHjrtIN95us02zdO6jGJ3xR602uuc9Xk53L-DgevwrQklFOeEChJ1bRDOqgkwkPjSNcDApSfIPSioT-gQOLTJY--oEXLm_QHg_Ddo:1o2kF5:vwqM2XhqywTEzziloyYa1DxT_riVxOPonZfn3reuTrw','2022-07-03 02:00:47.142016'),('wun76wfattq9kocej4vc93fw4ru3sfne','.eJxVjEEOgjAQRe_StWmYMtOCS_eeoZlpp4IaSCisjHdXEha6_e-9_zKRt3WIW9UljtmcDZjT7yacHjrtIN95us02zdO6jGJ3xR602uuc9Xk53L-DgevwrQklFOeEChJ1bRDOqgkwkPjSNcDApSfIPSioT-gQOLTJY--oEXLm_QHg_Ddo:1nxybk:sK_bUVTrS3MxfEMgby6D10XyGMNm5qLpXcyYNR70XWk','2022-06-19 22:20:28.835576');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-19 16:16:47
