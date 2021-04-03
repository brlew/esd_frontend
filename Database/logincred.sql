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
# Database: `g1t6_logincred`
--------------------------------------------------------------*/
CREATE DATABASE IF NOT EXISTS `g1t6_logincred` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `g1t6_logincred`;

/*--------------------------------------------------------------
# Table structure for table 'patientLogin'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `patientLogin`;
CREATE TABLE IF NOT EXISTS `patientLogin` (
  `pUsername` varchar(50) NOT NULL,
  `pPwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pUsername`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- Dumping data for table `patientLogin`
INSERT INTO `patientLogin` (`pUsername`, `pPwd`) VALUES
('veronlehhh', 'vpwd'),
('jasjas', 'jpwd');


/*--------------------------------------------------------------
# Table structure for table 'doctorLogin'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `doctorLogin`;
CREATE TABLE IF NOT EXISTS `doctorLogin` (
  `dID` int(11) NOT NULL AUTO_INCREMENT,
  `dName` varchar(50) NOT NULL,
  `dUsername` varchar(50) NOT NULL,
  `dPwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`dID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table `empLogin`
INSERT INTO `doctorLogin` (`dID`, `dUsername`, `dName`, `dPwd`) VALUES
(1, 'Tom', 'tom123', 'tom123'),
(2, 'Henry', 'henry123', 'henry123');


/*--------------------------------------------------------------
# Table structure for table 'pharmacistLogin'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `pharmacistLogin`;
CREATE TABLE IF NOT EXISTS `pharmacistLogin` (
  `pharID` int(11) NOT NULL AUTO_INCREMENT,
  `pharName` varchar(50) NOT NULL,
  `pharUsername` varchar(50) NOT NULL,
  `pharPwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pharID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table `empLogin`
INSERT INTO `pharmacistLogin` (`pharID`, `pharName`, `pharUsername`, `pharPwd`) VALUES
(1, 'Li Ying', 'liying', 'liying'),
(2, 'Bo Ren', 'boren', 'boren');
