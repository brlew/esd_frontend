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
# Database: `g1t6_patient
--------------------------------------------------------------*/
CREATE DATABASE IF NOT EXISTS `g1t6_patient` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `g1t6_patient`;

/*--------------------------------------------------------------
# Table structure for table 'patient'
--------------------------------------------------------------*/
-- name/nric/race/dob/mobile_no
DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `pID` int(11) NOT NULL AUTO_INCREMENT, --NRIC
  `pName` varchar(50) NOT NULL,
  `pAge` int(11) NOT NULL,
  `pNumber` varchar(8) NOT NULL,
  `pAddress` varchar(100) NOT NULL,
  `pAllergies` varchar(100) NULL,
  PRIMARY KEY (`pID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- Dumping data for table `patient`
INSERT INTO `patient` (`pID`, `pName`, `pAge`, `pNumber`, `pAddress`, `pAllergies`) VALUES
(1, 'Veronica', '21', '98765432', 'cck', 'Paracetamol'),
(2, 'Jasmine', '21', '87654321', 'amk', 'Cetirizine');


/*--------------------------------------------------------------
# Table structure for table 'medical_records'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `medicalRecord`;
CREATE TABLE IF NOT EXISTS `medicalRecord` (
  `pID` int(11) NOT NULL,
  `pDiagnosis` varchar(50),
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`created`, `pID`),
  KEY `medicalRecord_fk1` (`pID`)
)ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table `medicalRecords`
INSERT INTO `medicalRecord`(`pID`, `pDiagnosis`) VALUES
(1, 'Paracetamol');


-- Foreign Key
ALTER TABLE `medicalRecord`
  ADD CONSTRAINT `medicalRecord_fk1` FOREIGN KEY (`pID`) REFERENCES `patient` (`pID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
