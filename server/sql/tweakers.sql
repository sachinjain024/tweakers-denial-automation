-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 23, 2016 at 05:27 PM
-- Server version: 5.5.50-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tweakers`
--

-- --------------------------------------------------------

--
-- Table structure for table `entities`
--

CREATE TABLE IF NOT EXISTS `entities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `rating` int(11) NOT NULL,
  `enabled` int(11) NOT NULL DEFAULT '1',
  `imageUrl` varchar(500) NOT NULL,
  `pending_orders` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `entities`
--

INSERT INTO `entities` (`id`, `name`, `rating`, `enabled`, `imageUrl`, `pending_orders`) VALUES
(1, 'Jungle Jamboree', 10, 1, 'https://d4t7t8y8xqo0t.cloudfront.net/resized/750X436/restaurant/121473/3801_Jungle%20Jamboree%203.jpg', 4),
(2, 'Parikrama - The Revolving Restaurant', 9, 1, 'http://zeat.in/upload/Restro//ardor.jpg', 0),
(3, 'Garam Dharam', 8, 1, 'http://static.dnaindia.com/sites/default/files/2015/09/09/374251-pti-dharmendra-restaurant.jpg', 0),
(4, 'Cafe Hawkers', 7, 1, 'http://www.zhc.in/images/gallery/hawkers/2.jpg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE IF NOT EXISTS `items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `enabled` tinyint(1) NOT NULL DEFAULT '1',
  `entity` int(11) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT '10',
  `imageUrl` varchar(1000) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `stars` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `name`, `price`, `enabled`, `entity`, `quantity`, `imageUrl`, `description`, `stars`) VALUES
(1, 'Choley', 100, 1, 1, 27, 'http://a.ctimg.net/8fw-Y3EgQqeQeA8RfOWrdw/choley-spicy-chickpeas-curry-recipe-12663-dish.1024x1024.jpg', 'Garnished with coriander leaves and served with Poori, Roti or Bhature', 4),
(2, 'Paneer tikka', 150, 1, 1, 5, 'http://www.fauziaskitchenfun.com/sites/default/files/paneer%20tikka.JPG', 'Paneer tikka is an Indian dish made from chunks of paneer marinated in spices and grilled in a tandoor.', 5),
(3, 'Dal makhani', 100, 1, 1, 0, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRRcSb_DQqAPzO2hl9a006zITO9TiFQZ7A5REwLF13wu8-mCjd', 'Dal makhani or dal makhni is a popular dish originating from the Punjab region of the Indian Subcontinent. ', 4);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE IF NOT EXISTS `transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `items` varchar(1000) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`id`, `items`, `status`) VALUES
(1, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(2, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(3, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(4, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(5, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(6, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(7, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(8, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(9, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(10, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(11, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 1),
(12, '[{"price": 100, "id": 1, "name": "Choley", "quantity":100}]', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
