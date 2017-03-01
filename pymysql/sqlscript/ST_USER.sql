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

 Date: 03/01/2017 15:08:38 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `ST_USER`
-- ----------------------------
DROP TABLE IF EXISTS `ST_USER`;
CREATE TABLE `ST_USER` (
  `ST_USER_ID` int(11) NOT NULL,
  `COMPANY_ID` varchar(32) DEFAULT NULL,
  `REF_USER_ID` int(11) DEFAULT NULL,
  `REF_USER_NAME` varchar(50) DEFAULT NULL,
  `CREATED_DT` datetime DEFAULT NULL,
  `MODIFIED_DT` datetime DEFAULT NULL,
  PRIMARY KEY (`ST_USER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `ST_USER`
-- ----------------------------
BEGIN;
INSERT INTO `ST_USER` VALUES ('10001', '999999999', '3', 'birdben', '2017-03-01 15:08:13', '2017-03-01 15:08:13'), ('10002', '999999999', '4', 'zhangsan', '2017-03-01 15:08:13', '2017-03-01 15:08:13');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
