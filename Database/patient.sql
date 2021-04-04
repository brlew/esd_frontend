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
# Table structure for table 'patientLogin'
--------------------------------------------------------------*/
CREATE TABLE `patient` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `name` varchar(25) NOT NULL,
  `partialnric` varchar(15) NOT NULL,
  `race` varchar(15) NOT NULL,
  `dob` varchar(15) NOT NULL,
  `mobileno` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dumping data for table `patientLogin`
INSERT INTO `patient` (`id`, `username`, `password`, `email`, `name`, `partialnric`, `race`, `dob`, `mobileno`) VALUES
(1, 'brlewtest', 'sha256$mGFXdgMi$1e24573419401bb2f72d964c3d4229beddc9ed00355d0683ac31c5a3fab92524', 'brlewtest@brlewtest.com', '', '0', '', '', 0),
(2, 'seekhealthadmin', 'sha256$cs6f7KtH$dd61931c1ba072e848d7e93eb2e2fe04e0a4f268e4b41c0746400968a4587898', 'seekhealthadmin@f.com', '', '0', '', '', 0),
(3, 'bwong375', 'sha256$dXmVEk5f$8bbe66ef13d80224223eb14d54f5c5121ca1ab5725a6f1ab10a2bf89e1b44cb1', 'bwong375@gmail.com', 'BERNARD WONG', '*****375C', 'CHINESE', '10 Sep 1948', 97399245),
(4, 'tanxiaohui98', 'sha256$et6Xf8xb$bde8b74d8aa83c23908e8fcfa137ea4be3267aa327b295289390d4399efa2766', 'tanxiaohui98@gmail.com', 'TAN XIAO HUI', '*****381D', 'CHINESE', '6 Jun 1998', 97399245);


DROP TABLE IF EXISTS `medicalRecord`;
CREATE TABLE IF NOT EXISTS `medicalRecord` (
  `id` int(11) NOT NULL,
  `pDiagnosis` varchar(50),
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY (`created`, `id`),
  KEY `medicalRecord_fk1` (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table `medicalRecords`
INSERT INTO `medicalRecord`(`id`, `pDiagnosis`) VALUES
(1, 'Paracetamol'),
(3, 'Paracetamol'),
(3, 'Covid'),
(3, 'Fever'),
(4, 'Paracetamol');
