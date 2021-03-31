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
# Database: `g1t6_doctor`
--------------------------------------------------------------*/
CREATE DATABASE IF NOT EXISTS `g1t6_doctor` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `g1t6_doctor`;


/*--------------------------------------------------------------
# Table structure for table 'doctor' //MD5('henrypwd')
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `doctor`;
CREATE TABLE IF NOT EXISTS `doctor` (
    `dID` int(11) NOT NULL AUTO_INCREMENT,
    `dName` varchar(50) NOT NULL,
    `dDepartment` varchar(32) NOT NULL,
    `dRoom` varchar(32) NOT NULL,
    PRIMARY KEY (`dID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table `doctor`
INSERT INTO `doctor` (`dID`, `dName`, `dDepartment`, `dRoom`) VALUES
(1, 'Tom', 'Cardiologists', 'Rm3-1'), 
(2, 'Henry', 'Cardiologists', 'Rm3-2'); 


/*--------------------------------------------------------------
# Table structure for table `doctorAvail`
--------------------------------------------------------------*/
DROP TABLE IF EXISTS `doctorAvail`;
CREATE TABLE IF NOT EXISTS `doctorAvail` (
    `dID` int(11) NOT NULL,
    `timeSlotID` int(11) NOT NULL,
    `timeSlot` datetime NOT NULL,
    `bookingStatus` varchar(32) NOT NULL DEFAULT 'Available',
    PRIMARY KEY (`dID`, `timeSlotID`),
    KEY `doctorAvail_fk1` (`dID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `docAvail`
INSERT INTO `doctorAvail` (`dID`,  `timeSlotID`, `timeSlot`, `bookingStatus`) VALUES
(1, 1, '2021-06-12 02:00:00', 'Available'),
(1, 2, '2021-06-13 02:30:00', 'Available'),
(1, 3, '2021-07-14 03:00:00', 'Available'),
(1, 4, '2021-07-15 03:30:00', 'Available'),
(1, 5, '2021-08-16 04:00:00', 'Available'),
(2, 6, '2021-08-17 04:30:00', 'Available'),
(2, 7, '2021-08-18 05:00:00', 'Available'),
(2, 8, '2021-09-19 05:30:00', 'Available'),
(2, 9, '2021-09-20 06:00:00', 'Available');

-- Foreign Key
ALTER TABLE `doctorAvail`
    ADD CONSTRAINT `doctorAvail_fk1` FOREIGN KEY (`dID`) REFERENCES `doctor` (`dID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;