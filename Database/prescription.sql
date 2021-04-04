-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 12, 2020 at 02:17 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*--------------------------------------------------------------
# Database: `g1t6_prescription`
--------------------------------------------------------------*/
CREATE DATABASE IF NOT EXISTS `g1t6_prescription` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `g1t6_prescription`;

/*--------------------------------------------------------------
# Table structure for table 'prescription'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `prescription`;
CREATE TABLE IF NOT EXISTS `prescription` (
  `prescriptionID` int(8) NOT NULL AUTO_INCREMENT,
  `medName` varchar(25) NOT NULL,
  `dosage` varchar(20) NOT NULL,
  `pID` int(11) NOT NULL,
  `aID` int(11) NOT NULL,
  PRIMARY KEY (`prescriptionID`),
  KEY `FK_pID` (`pID`),
  KEY `FK_aID` (`aID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table `prescription`
INSERT INTO `prescription` (`prescriptionID`, `medName`, `dosage`, `pID`, `aID`) VALUES 
(1, 'amoxicillin', '200mg', 1, 1),
(2, 'vaccine', '200mg', 3, 3),
(3, 'Docusate', '200mg', 3, 6),
(4, 'amoxicillin', '200mg', 3, 5);

-- Foreign Key
-- ALTER TABLE `prescription`
--   ADD CONSTRAINT `FK_pID` FOREIGN KEY (`pID`) REFERENCES g1t6_patient.patient(`pID`) ON DELETE CASCADE ON UPDATE CASCADE,
--   ADD CONSTRAINT `FK_aID` FOREIGN KEY (`aID`) REFERENCES g1t6_appt.appt(`apptID`) ON DELETE CASCADE ON UPDATE CASCADE;
-- COMMIT;
