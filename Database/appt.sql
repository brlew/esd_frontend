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
CREATE DATABASE IF NOT EXISTS `g1t6_appt` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `g1t6_appt`;

/*--------------------------------------------------------------
# Table structure for table 'appt'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `appt`;
CREATE TABLE IF NOT EXISTS `appt` (
  `apptID` int(11) NOT NULL AUTO_INCREMENT,
  `pID` int(11) NOT NULL,
  `dID` int(11) NOT NULL,
  `apptDateTime` datetime NOT NULL,
  `apptStatus` varchar(10) NOT NULL DEFAULT 'Pending',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`apptID`),
  KEY `appt_fk1` (`dID`),
  KEY `appt_fk2` (`pID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table `appt`
INSERT INTO `appt` (`apptID`, `pID`, `dID`, `apptDateTime`, `apptStatus`, `created`, `modified`) VALUES
(1, 1, 2, '2021-08-17 04:00:00', 'pending', '2020-06-12 02:14:55', '2020-06-12 02:14:55');

-- Foreign Key
ALTER TABLE `appt`
  ADD CONSTRAINT `appt_fk1` FOREIGN KEY (`dID`) REFERENCES g1t6_doctor.doctor(`dID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `appt_fk2` FOREIGN KEY (`pID`) REFERENCES g1t6_patient.patient(`pID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

