-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 25, 2023 at 02:42 PM
-- Server version: 10.5.15-MariaDB-0+deb11u1
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wprojectcpe62`
--

-- --------------------------------------------------------

--
-- Table structure for table `datasellpage`
--

CREATE TABLE `datasellpage` (
  `ID` int(11) NOT NULL,
  `Date` text NOT NULL,
  `Time` text NOT NULL,
  `Username` text NOT NULL,
  `Lastname` text NOT NULL,
  `Model` text NOT NULL,
  `Weight` text NOT NULL,
  `Price` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datasellpage`
--

INSERT INTO `datasellpage` (`ID`, `Date`, `Time`, `Username`, `Lastname`, `Model`, `Weight`, `Price`) VALUES
(49, '23/06/2021', '01:54:43', 'Custom Owner', '-W-', 'Wavy', '20', '1200'),
(53, '25/06/2021', '00:36:09', 'fdgsdfds', 'awdqsdq', 'Square', '10', '600'),
(54, '25/06/2021', '00:36:29', 'Hello', 'World', 'Square/Wavy', '5/5', '600'),
(55, '25/06/2021', '02:04:52', 'BBBBaz', 'dDA', 'Square', '10', '600'),
(57, '25/06/2021', '02:50:25', 'Hello', 'World', 'Square/Wavy', '5/5', '600'),
(58, '25/06/2021', '02:54:43', 'Hello', 'World', 'Square/Wavy', '5/5', '600'),
(59, '01/07/2021', '02:49:14', 'v', 'v', 'Square/Wavy', '1/2', '180'),
(60, '05/07/2021', '02:52:01', 'Ga', 'Dsx', 'Square', '10', '600'),
(61, '05/07/2021', '02:52:25', 'mmmmmnnn', 'bnnbbbb', 'Square', '10', '600'),
(62, '05/07/2021', '02:57:08', 'Ga', 'Dsx', 'Square', '10', '600'),
(63, '06/07/2021', '03:36:15', 'Fhasez', 'Zafas', 'Square/Wavy', '42/12', '3240'),
(64, '06/07/2021', '03:36:47', 'Custom Owner', 'xxxxx', 'Wavy', '32', '1920'),
(65, '06/07/2021', '05:33:49', 'วัชรนนท์', 'เกิดแก้ว', 'Square/Wavy', '20/5', '1500'),
(66, '06/07/2021', '22:48:11', 'วัชรนนท์', 'เกิดแก้ว', 'Square/Wavy', '20/5', '1500'),
(67, '06/07/2021', '22:48:34', 'วัชรนนท์', 'เกิดแก้ว', 'Square/Wavy', '20/5', '1500'),
(68, '06/07/2021', '22:49:03', 'mmmmmnnn', 'bnnbbbb', 'Square', '10', '600'),
(69, '06/07/2021', '22:49:21', 'Hello', 'World', 'Square/Wavy', '5/5', '600'),
(70, '06/07/2021', '23:47:02', 'วัชรนนท์', 'เกิดแก้ว', 'Square/Wavy', '20/5', '1500'),
(71, '07/07/2021', '00:01:01', 'วัชรนนท์', 'เกิดแก้ว', 'Square/Wavy', '20/5', '1500'),
(72, '14/07/2021', '03:53:42', 'Owner', 'Custom', 'Wavy', '1', '60'),
(73, '14/07/2021', '03:54:17', 'Owner', 'Custom', 'Wavy', '1', '60'),
(74, '14/07/2021', '03:54:57', 'Owner', 'Custom', 'Wavy', '1', '10'),
(75, '14/07/2021', '03:55:10', 'Owner', 'Custom', 'Wavy', '2', '20'),
(76, '14/07/2021', '03:55:20', 'Owner', 'Custom', 'Wavy', '3', '30'),
(77, '14/07/2021', '03:55:31', 'Owner', 'Custom', 'Square', '1', '30'),
(78, '14/07/2021', '03:56:44', 'Owner', 'Custom', 'Wavy', '3', '180'),
(79, '14/07/2021', '03:56:56', 'Owner', 'Custom', 'Square', '1', '60'),
(80, '14/07/2021', '03:58:37', 'Owner', 'Custom', 'Square', '3', '180'),
(81, '14/07/2021', '04:38:07', 'Owner', 'Custom', 'Wavy', '3', '210'),
(82, '14/07/2021', '04:38:14', 'Owner', 'Custom', 'Wavy', '1', '70'),
(83, '14/07/2021', '04:38:19', 'Owner', 'Custom', 'Square', '1', '60'),
(84, '14/07/2021', '20:55:36', 'Owner', 'Custom', 'Square', '15', '900'),
(85, '19/07/2021', '00:33:41', 'Owner', 'Custom', 'Wavy', '2', '120'),
(86, '30/07/2021', '23:39:06', 'Owner', 'Custom', 'Square', '2', '120'),
(87, '30/07/2021', '23:39:48', 'Owner', 'Custom', 'Square', '10', '600'),
(88, '30/07/2021', '23:39:53', 'Owner', 'Custom', 'Square', '25', '1500'),
(89, '30/07/2021', '23:42:38', 'Fhasez', 'Zafas', 'Square/Wavy', '42/12', '3240'),
(90, '30/07/2021', '23:43:35', 'Fhasez', 'Zafas', 'Square/Wavy', '42/12', '3240'),
(91, '30/07/2021', '23:44:01', 'fassss', 'asddddq', 'Square/Wavy', '10/12', '1320'),
(92, '30/07/2021', '23:44:04', 'วัชรนนท์', 'เกิดแก้ว', 'Square/Wavy', '20/5', '1500'),
(93, '30/07/2021', '23:44:21', 'qQQ', 'EQQ', 'Square/Wavy', '12/31', '2580'),
(94, '30/07/2021', '23:44:26', 'BBBBaz', 'dDA', 'Square', '10', '600'),
(95, '30/07/2021', '23:45:42', 'Owner', 'Custom', 'Wavy', '3', '180'),
(96, '30/07/2021', '23:45:46', 'Owner', 'Custom', 'Wavy', '95', '5700'),
(97, '30/07/2021', '23:47:39', 'Owner', 'Custom', 'Wavy', '80', '4800'),
(98, '30/07/2021', '23:47:53', 'Owner', 'Custom', 'Wavy', '2', '120'),
(99, '02/08/2021', '10:47:33', 'Owner', 'Custom', 'Wavy', '25', '1500'),
(100, '19/01/2022', '12:49:35', 'Owner', 'Custom', 'Square', '23', '1380'),
(101, '19/01/2022', '13:21:03', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(102, '19/01/2022', '13:21:15', 'qwqq', 'qqw', 'Square', '1', '60'),
(103, '19/01/2022', '14:09:16', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(104, '20/01/2022', '02:13:44', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(105, '20/01/2022', '02:15:54', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(106, '20/01/2022', '02:18:23', 'qwqq', 'qqw', 'Square', '1', '60'),
(107, '20/01/2022', '02:21:05', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(108, '20/01/2022', '02:22:22', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(109, '20/01/2022', '02:30:34', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(110, '20/01/2022', '03:53:57', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(111, '21/01/2022', '03:22:38', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(112, '21/01/2022', '03:48:44', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(113, '21/01/2022', '03:50:17', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(114, '21/01/2022', '03:50:34', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(115, '21/01/2022', '03:50:53', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(116, '21/01/2022', '03:51:16', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(117, '21/01/2022', '03:53:08', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(118, '21/01/2022', '09:43:24', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(119, '21/01/2022', '09:48:37', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(120, '21/01/2022', '09:49:10', 'qwqq', 'qqw', 'Square', '1', '60'),
(121, '21/01/2022', '09:49:23', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(122, '21/01/2022', '09:50:22', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(123, '21/01/2022', '09:53:20', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(124, '21/01/2022', '09:58:27', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(125, '21/01/2022', '10:03:07', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(126, '21/01/2022', '10:18:09', 'qwqq', 'qqw', 'Square', '1', '60'),
(127, '21/01/2022', '10:25:38', 'qwqq', 'qqw', 'Square', '1', '60'),
(128, '21/01/2022', '10:27:45', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(129, '21/01/2022', '11:21:28', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(130, '21/01/2022', '11:29:33', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(131, '22/01/2022', '03:02:47', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(132, '22/01/2022', '04:21:13', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(133, '29/01/2022', '02:02:44', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(134, '29/01/2022', '02:09:04', 'wq', 'wq', 'Square/Wavy', '1/1', '120'),
(135, '29/01/2022', '08:01:38', 'qwqq', 'qqw', 'Square', '1', '60'),
(136, '29/01/2022', '09:00:26', 'qwqq', 'qqw', 'Square', '1', '60'),
(137, '29/01/2022', '09:10:53', 'qwqq', 'qqw', 'Square', '1', '60'),
(138, '29/01/2022', '09:30:11', 'qwqq', 'qqw', 'Square', '1', '60'),
(139, '30/01/2022', '03:10:24', 'qwqq', 'qqw', 'Square', '1', '60'),
(140, '30/01/2022', '03:37:04', 'qwqq', 'qqw', 'Square', '1', '60'),
(141, '30/01/2022', '03:39:42', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(142, '30/01/2022', '03:48:06', 'wq', 'wq', 'Square/Wavy', '1/1', '120'),
(143, '30/01/2022', '08:44:22', 'qwqq', 'qqw', 'Square', '1', '60'),
(144, '30/01/2022', '08:46:07', 'qwqq', 'qqw', 'Square', '1', '60'),
(145, '30/01/2022', '08:47:20', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(146, '30/01/2022', '08:48:39', 'qwqq', 'qqw', 'Square', '1', '60'),
(147, '30/01/2022', '09:21:25', 'qwqq', 'qqw', 'Square', '1', '60'),
(148, '30/01/2022', '09:42:06', 'qwqq', 'qqw', 'Square', '1', '60'),
(149, '30/01/2022', '10:14:51', 'qwqq', 'qqw', 'Square', '1', '60'),
(150, '30/01/2022', '10:34:53', 'qwqq', 'qqw', 'Square', '1', '60'),
(151, '31/01/2022', '03:42:24', 'qwqq', 'qqw', 'Square', '1', '60'),
(152, '31/01/2022', '03:50:38', 'qwqq', 'qqw', 'Square', '1', '60'),
(153, '31/01/2022', '03:54:30', 'Owner', 'Custom', 'Square', '1', '60'),
(154, '31/01/2022', '03:59:34', 'qwqq', 'qqw', 'Square', '1', '60'),
(155, '31/01/2022', '04:09:15', 'qwqq', 'qqw', 'Square', '1', '60'),
(156, '31/01/2022', '04:10:52', 'qwqq', 'qqw', 'Square', '1', '60'),
(157, '31/01/2022', '08:07:27', 'qwqq', 'qqw', 'Square', '1', '60'),
(158, '31/01/2022', '08:15:21', 'qwqq', 'qqw', 'Square', '1', '60'),
(159, '31/01/2022', '08:48:40', 'qwqq', 'qqw', 'Square', '1', '60'),
(160, '31/01/2022', '08:50:30', 'qwqq', 'qqw', 'Square', '1', '60'),
(161, '31/01/2022', '08:51:59', 'qwqq', 'qqw', 'Square', '1', '60'),
(162, '31/01/2022', '08:54:00', 'qwqq', 'qqw', 'Square', '1', '60'),
(163, '31/01/2022', '08:56:00', 'qwqq', 'qqw', 'Square', '1', '60'),
(164, '31/01/2022', '08:57:45', 'qwqq', 'qqw', 'Square', '1', '60'),
(165, '31/01/2022', '08:59:50', 'qwqq', 'qqw', 'Square', '1', '60'),
(166, '31/01/2022', '09:05:05', 'qwqq', 'qqw', 'Square', '1', '60'),
(167, '31/01/2022', '09:09:50', 'qwqq', 'qqw', 'Square', '1', '60'),
(168, '31/01/2022', '09:13:08', 'qwqq', 'qqw', 'Square', '1', '60'),
(169, '31/01/2022', '09:15:20', 'qwqq', 'qqw', 'Square', '1', '60'),
(170, '31/01/2022', '04:48:20 PM', 'qwqq', 'qqw', 'Square', '1', '60'),
(171, '31/01/2022', '04:55:16 PM', 'qwqq', 'qqw', 'Square', '1', '60'),
(172, '01/02/2022', '03:10:07 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(173, '01/02/2022', '03:13:15 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(174, '01/02/2022', '03:16:32 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(175, '01/02/2022', '03:19:39 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(176, '01/02/2022', '03:22:30 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(177, '01/02/2022', '03:23:30 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(178, '02/02/2022', '11:11:37 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(179, '02/02/2022', '11:28:19 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(180, '04/02/2022', '10:36:03 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(181, '04/02/2022', '10:40:42 AM', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(182, '04/02/2022', '10:46:31 AM', 'wq', 'wq', 'Square/Wavy', '1/1', '120'),
(183, '04/02/2022', '10:53:45 AM', 'qwqq', 'qqw', 'Square', '1', '60'),
(184, '05/02/2022', '07:27:51', 'qwqq', 'qqw', 'Square', '1', '60'),
(185, '05/02/2022', '08:37:25', 'qwqq', 'qqw', 'Square', '1', '60'),
(186, '05/02/2022', '12:48:32', 'qwqq', 'qqw', 'Square', '1', '60'),
(187, '05/02/2022', '13:45:43', 'qwqq', 'qqw', 'Square', '1', '60'),
(188, '05/02/2022', '13:57:54', 'qwqq', 'qqw', 'Square', '1', '60'),
(189, '05/02/2022', '14:01:16', 'qwqq', 'qqw', 'Square', '1', '60'),
(190, '06/02/2022', '08:42:00', 'qwqq', 'qqw', 'Square', '1', '60'),
(191, '06/02/2022', '09:12:24', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(192, '06/02/2022', '09:30:48', 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '600'),
(193, '09/02/2022', '11:29:05', 'qwqq', 'qqw', 'Square', '1', '60'),
(194, '09/02/2022', '11:40:22', 'qwqq', 'qqw', 'Square', '1', '60'),
(195, '09/02/2022', '14:17:52', 'qwqq', 'qqw', 'Square', '1', '60'),
(196, '09/02/2022', '14:18:34', 'qwqq', 'qqw', 'Square', '1', '60'),
(197, '09/02/2022', '15:10:37', 'qwqq', 'qqw', 'Square', '1', '60'),
(198, '09/02/2022', '15:11:33', 'qwqq', 'qqw', 'Square', '1', '60'),
(199, '09/02/2022', '15:12:02', 'qwqq', 'qqw', 'Square', '1', '60'),
(200, '09/02/2022', '15:21:09', 'qwqq', 'qqw', 'Square', '1', '60'),
(201, '09/02/2022', '15:37:32', 'qwqq', 'qqw', 'Square', '1', '60'),
(202, '09/02/2022', '15:50:04', 'qwqq', 'qqw', 'Square', '1', '60'),
(203, '12/02/2022', '05:59:56', '22', '11', 'Square/Wavy', '1/1', '120'),
(204, '12/02/2022', '06:05:20', '22', '11', 'Square/Wavy', '1/1', '120'),
(205, '12/02/2022', '06:09:12', '22', '11', 'Square/Wavy', '1/1', '120'),
(206, '12/02/2022', '14:08:37', 'qwqq', 'qqw', 'Square', '1', '60'),
(207, '12/02/2022', '14:09:53', 'Owner', 'Custom', 'Wavy', '2', '120'),
(208, '12/02/2022', '14:10:31', 'Owner', 'Custom', 'Wavy', '1', '60'),
(209, '03/09/2022', '18:36:17', 'หไ', 'หฟฟ', 'Square', '1', '60'),
(210, '03/09/2022', '18:51:27', 'Owner', 'Custom', 'Square', '1', '60'),
(211, '03/09/2022', '19:06:41', 'Owner', 'Custom', 'Square', '1', '60'),
(212, '03/09/2022', '19:09:10', 'Owner', 'Custom', 'Square', '1', '60'),
(213, '25/03/2023', '14:05:56', 'Owner', 'Custom', 'Square', '10', '600'),
(214, '25/03/2023', '14:09:11', 'Owner', 'Custom', 'Wavy', '10', '600');

-- --------------------------------------------------------

--
-- Table structure for table `loadcell`
--

CREATE TABLE `loadcell` (
  `ID` int(1) NOT NULL,
  `sweight` float NOT NULL,
  `outweight` float NOT NULL,
  `kweight` float NOT NULL,
  `berstatus` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loadcell`
--

INSERT INTO `loadcell` (`ID`, `sweight`, `outweight`, `kweight`, `berstatus`) VALUES
(1, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `ownerpage`
--

CREATE TABLE `ownerpage` (
  `ID` int(11) NOT NULL,
  `Username` text NOT NULL,
  `Lastname` text NOT NULL,
  `Model` text NOT NULL,
  `Weight` text NOT NULL,
  `Phone` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ownerpage`
--

INSERT INTO `ownerpage` (`ID`, `Username`, `Lastname`, `Model`, `Weight`, `Phone`) VALUES
(1076, 'qwqq', 'qqw', 'Square', '1', '14124214'),
(1077, 'วัชรนนท์', 'เกิดแก้ว', 'Wavy', '10', '0823259840'),
(1080, '22', '11', 'Square/Wavy', '1/1', '0861932650'),
(1081, 'หไ', 'หฟฟ', 'Square', '1', '061926502');

-- --------------------------------------------------------

--
-- Table structure for table `qdataownerpage`
--

CREATE TABLE `qdataownerpage` (
  `ID` int(11) NOT NULL,
  `Model` text NOT NULL,
  `Weight` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `qorderpage`
--

CREATE TABLE `qorderpage` (
  `ID` int(11) NOT NULL,
  `Username` text NOT NULL,
  `Lastname` text NOT NULL,
  `Model` text NOT NULL,
  `Weight` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `STOP`
--

CREATE TABLE `STOP` (
  `motorst` int(1) NOT NULL,
  `num` int(1) NOT NULL,
  `contro` int(1) NOT NULL,
  `ID` int(1) NOT NULL,
  `Motor` int(5) NOT NULL,
  `stsp` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `STOP`
--

INSERT INTO `STOP` (`motorst`, `num`, `contro`, `ID`, `Motor`, `stsp`) VALUES
(1, 0, 0, 1, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `datasellpage`
--
ALTER TABLE `datasellpage`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `loadcell`
--
ALTER TABLE `loadcell`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `ownerpage`
--
ALTER TABLE `ownerpage`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `qorderpage`
--
ALTER TABLE `qorderpage`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `STOP`
--
ALTER TABLE `STOP`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `datasellpage`
--
ALTER TABLE `datasellpage`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=215;

--
-- AUTO_INCREMENT for table `loadcell`
--
ALTER TABLE `loadcell`
  MODIFY `ID` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ownerpage`
--
ALTER TABLE `ownerpage`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1082;

--
-- AUTO_INCREMENT for table `qorderpage`
--
ALTER TABLE `qorderpage`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=650;

--
-- AUTO_INCREMENT for table `STOP`
--
ALTER TABLE `STOP`
  MODIFY `ID` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
