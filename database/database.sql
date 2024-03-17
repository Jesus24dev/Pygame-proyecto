-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               10.4.21-MariaDB-log - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for juego
CREATE DATABASE IF NOT EXISTS `juego` /*!40100 DEFAULT CHARACTER SET utf32 COLLATE utf32_spanish2_ci */;
USE `juego`;

-- Dumping structure for table juego.avatar
CREATE TABLE IF NOT EXISTS `avatar` (
  `ID_AVATAR` int(11) NOT NULL AUTO_INCREMENT,
  `COLOR` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`ID_AVATAR`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.avatar: ~4 rows (approximately)
INSERT INTO `avatar` (`ID_AVATAR`, `COLOR`) VALUES
	(1, 'AMARILLO'),
	(2, 'AZUL'),
	(3, 'ROJO'),
	(4, 'VERDE');

-- Dumping structure for table juego.creador
CREATE TABLE IF NOT EXISTS `creador` (
  `ID_CREADOR` int(11) NOT NULL AUTO_INCREMENT,
  `JUEGO` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  `NOMBRE` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`ID_CREADOR`),
  KEY `FK_creador_juego` (`JUEGO`),
  CONSTRAINT `FK_creador_juego` FOREIGN KEY (`JUEGO`) REFERENCES `juego` (`NOMBRE`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.creador: ~2 rows (approximately)
INSERT INTO `creador` (`ID_CREADOR`, `JUEGO`, `NOMBRE`) VALUES
	(1, 'FLAT WORLD', 'NAZARIO RODRIGUEZ'),
	(2, 'FLAT WORLD', 'JESUS SIRIT');

-- Dumping structure for table juego.datos_juego
CREATE TABLE IF NOT EXISTS `datos_juego` (
  `ID_DATOS` int(11) NOT NULL AUTO_INCREMENT,
  `JUEGO` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  `ID_JUGADOR` int(11) DEFAULT NULL,
  `ACIERTOS` int(11) DEFAULT NULL,
  `FALLOS` int(11) DEFAULT NULL,
  `PRECISION` float DEFAULT NULL,
  `NIVELES_COMPLETADOS` int(11) DEFAULT NULL,
  `PUNTAJE_TOTAL` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_DATOS`),
  UNIQUE KEY `FK_datos_juego_juego` (`JUEGO`) USING BTREE,
  UNIQUE KEY `FK_datos_juego_jugador` (`ID_JUGADOR`) USING BTREE,
  CONSTRAINT `FK_datos_juego_juego` FOREIGN KEY (`JUEGO`) REFERENCES `juego` (`NOMBRE`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_datos_juego_jugador` FOREIGN KEY (`ID_JUGADOR`) REFERENCES `jugador` (`ID_JUGADOR`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.datos_juego: ~0 rows (approximately)

-- Dumping structure for table juego.descripcion
CREATE TABLE IF NOT EXISTS `descripcion` (
  `ID_DESCRIPCION` int(11) NOT NULL AUTO_INCREMENT,
  `DESCRIPCION` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`ID_DESCRIPCION`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.descripcion: ~3 rows (approximately)
INSERT INTO `descripcion` (`ID_DESCRIPCION`, `DESCRIPCION`) VALUES
	(1, 'CONSTRUCCION'),
	(2, 'AREAS'),
	(3, 'RECONOCIMIENTO');

-- Dumping structure for table juego.dificultad
CREATE TABLE IF NOT EXISTS `dificultad` (
  `ID_DIFICULTAD` int(11) NOT NULL AUTO_INCREMENT,
  `DIFICULTAD` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`ID_DIFICULTAD`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.dificultad: ~3 rows (approximately)
INSERT INTO `dificultad` (`ID_DIFICULTAD`, `DIFICULTAD`) VALUES
	(1, 'FACIL'),
	(2, 'MEDIO'),
	(3, 'DIFICIL');

-- Dumping structure for table juego.estado
CREATE TABLE IF NOT EXISTS `estado` (
  `ID_ESTADO` int(11) NOT NULL AUTO_INCREMENT,
  `ESTADO` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`ID_ESTADO`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.estado: ~2 rows (approximately)
INSERT INTO `estado` (`ID_ESTADO`, `ESTADO`) VALUES
	(1, 'COMPLETADO'),
	(2, 'EN PROCESO');

-- Dumping structure for table juego.juego
CREATE TABLE IF NOT EXISTS `juego` (
  `NOMBRE` varchar(50) COLLATE utf32_spanish2_ci NOT NULL,
  `DESCRIPCION` text COLLATE utf32_spanish2_ci DEFAULT NULL,
  `NIVELES` int(11) DEFAULT NULL,
  PRIMARY KEY (`NOMBRE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.juego: ~1 rows (approximately)
INSERT INTO `juego` (`NOMBRE`, `DESCRIPCION`, `NIVELES`) VALUES
	('FLAT WORLD', 'JUEGO DISEÑADO PARA NIÑOS', 12);

-- Dumping structure for table juego.jugador
CREATE TABLE IF NOT EXISTS `jugador` (
  `ID_JUGADOR` int(11) NOT NULL AUTO_INCREMENT,
  `JUEGO` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  `NICKNAME` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  `CLAVE` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  `ID_AVATAR` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_JUGADOR`),
  KEY `Index 2` (`JUEGO`),
  KEY `FK_jugador_avatar` (`ID_AVATAR`),
  CONSTRAINT `FK_jugador_avatar` FOREIGN KEY (`ID_AVATAR`) REFERENCES `avatar` (`ID_AVATAR`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_jugador_juego` FOREIGN KEY (`JUEGO`) REFERENCES `juego` (`NOMBRE`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci COMMENT='Tabla del jugador';

-- Dumping data for table juego.jugador: ~1 rows (approximately)
INSERT INTO `jugador` (`ID_JUGADOR`, `JUEGO`, `NICKNAME`, `CLAVE`, `ID_AVATAR`) VALUES
	(1, 'FLAT WORLD', 'Jesusito24', '12345', 4);

-- Dumping structure for table juego.nivel
CREATE TABLE IF NOT EXISTS `nivel` (
  `ID_NIVEL` int(11) NOT NULL AUTO_INCREMENT,
  `JUEGO` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  `DESCRIPCION` int(11) DEFAULT NULL,
  `NOMBRE` varchar(50) COLLATE utf32_spanish2_ci DEFAULT NULL,
  `DIFICULTAD` int(11) DEFAULT NULL,
  `OBJETIVOS` text COLLATE utf32_spanish2_ci DEFAULT NULL,
  `PUNTAJE_MAXIMO` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_NIVEL`),
  KEY `FK_nivel_juego` (`JUEGO`),
  KEY `FK_nivel_descripcion` (`DESCRIPCION`),
  KEY `FK_nivel_dificultad` (`DIFICULTAD`),
  CONSTRAINT `FK_nivel_descripcion` FOREIGN KEY (`DESCRIPCION`) REFERENCES `descripcion` (`ID_DESCRIPCION`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_nivel_dificultad` FOREIGN KEY (`DIFICULTAD`) REFERENCES `dificultad` (`ID_DIFICULTAD`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_nivel_juego` FOREIGN KEY (`JUEGO`) REFERENCES `juego` (`NOMBRE`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.nivel: ~0 rows (approximately)

-- Dumping structure for table juego.progreso_nivel
CREATE TABLE IF NOT EXISTS `progreso_nivel` (
  `ID_PROGRESO` int(11) NOT NULL AUTO_INCREMENT,
  `ID_JUGADOR` int(11) DEFAULT NULL,
  `ID_NIVEL` int(11) DEFAULT NULL,
  `PUNTAJE` int(11) DEFAULT NULL,
  `ESTADO` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_PROGRESO`),
  KEY `FK_progreso_nivel_jugador` (`ID_JUGADOR`),
  KEY `FK_progreso_nivel_nivel` (`ID_NIVEL`),
  KEY `FK_progreso_nivel_estado` (`ESTADO`),
  CONSTRAINT `FK_progreso_nivel_estado` FOREIGN KEY (`ESTADO`) REFERENCES `estado` (`ID_ESTADO`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_progreso_nivel_jugador` FOREIGN KEY (`ID_JUGADOR`) REFERENCES `jugador` (`ID_JUGADOR`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_progreso_nivel_nivel` FOREIGN KEY (`ID_NIVEL`) REFERENCES `nivel` (`ID_NIVEL`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

-- Dumping data for table juego.progreso_nivel: ~0 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;