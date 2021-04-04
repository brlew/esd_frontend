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
CREATE DATABASE IF NOT EXISTS `g1t6_employee` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `g1t6_employee`;


/*--------------------------------------------------------------
# Table structure for table 'doctorLogin'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `doctorLogin`;
CREATE TABLE IF NOT EXISTS `doctorLogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dName` varchar(50) NOT NULL,
  `dUsername` varchar(50) NOT NULL,
  `dPwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table `empLogin`
INSERT INTO `doctorLogin` (`id`, `dUsername`, `dName`, `dPwd`) VALUES
(11, 'tommy123', 'Tommy', 'tommy123'),
(12, 'henry123', 'Henry', 'henry123');


/*--------------------------------------------------------------
# Table structure for table 'pharmacistLogin'
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `pharmacistLogin`;
CREATE TABLE IF NOT EXISTS `pharmacistLogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pharName` varchar(50) NOT NULL,
  `pharUsername` varchar(50) NOT NULL,
  `pharPwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table `empLogin`
INSERT INTO `pharmacistLogin` (`id`, `pharName`, `pharUsername`, `pharPwd`) VALUES
(21, 'Li Ying', 'liying', 'liying'),
(22, 'Bo Ren', 'boren', 'boren');
