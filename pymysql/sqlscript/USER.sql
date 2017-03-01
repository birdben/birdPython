/*
 Navicat Premium Data Transfer

 Source Server         : 本地数据库
 Source Server Type    : MySQL
 Source Server Version : 50627
 Source Host           : localhost
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 50627
 File Encoding         : utf-8

 Date: 03/01/2017 15:08:43 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `USER`
-- ----------------------------
DROP TABLE IF EXISTS `USER`;
CREATE TABLE `USER` (
  `ID` int(11) DEFAULT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `JOB` varchar(50) DEFAULT NULL,
  `CITY` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `USER`
-- ----------------------------
BEGIN;
INSERT INTO `USER` VALUES ('1', 'bird', 'developer', 'beijing'), ('2', 'ben', 'test', 'shanghai'), ('3', 'birdben', 'manager', 'shanghai'), ('4', 'zhangsan', 'developer', 'shanghai');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
