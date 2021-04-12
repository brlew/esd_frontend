-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 12, 2021 at 02:29 AM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `g1t6_employee`
--

-- --------------------------------------------------------
CREATE DATABASE IF NOT EXISTS `g1t6_employee` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `g1t6_employee`;

--
-- Table structure for table `doctorlogin`
--

DROP TABLE IF EXISTS `doctorlogin`;
CREATE TABLE IF NOT EXISTS `doctorlogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dName` varchar(50) NOT NULL,
  `dUsername` varchar(50) NOT NULL,
  `dPwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctorlogin`
--

INSERT INTO `doctorlogin` (`id`, `dName`, `dUsername`, `dPwd`) VALUES
(11, 'Tommy', 'tommy123', 'tommy123'),
(12, 'Henry', 'henry123', 'henry123');

-- --------------------------------------------------------

--
-- Table structure for table `pharmacistlogin`
--

USE `g1t6_employee`;

DROP TABLE IF EXISTS `pharmacistlogin`;
CREATE TABLE IF NOT EXISTS `pharmacistlogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pharName` varchar(50) NOT NULL,
  `pharUsername` varchar(50) NOT NULL,
  `pharPwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pharmacistlogin`
--

INSERT INTO `pharmacistlogin` (`id`, `pharName`, `pharUsername`, `pharPwd`) VALUES
(21, 'Li Ying', 'liying123', 'liying123'),
(22, 'Bo Ren', 'boren123', 'boren123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
