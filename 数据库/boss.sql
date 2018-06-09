/*
Navicat MySQL Data Transfer

Source Server         : conn
Source Server Version : 50624
Source Host           : 127.0.0.1:3306
Source Database       : boss

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2018-01-14 15:55:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add staff', '7', 'add_staff');
INSERT INTO `auth_permission` VALUES ('20', 'Can change staff', '7', 'change_staff');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete staff', '7', 'delete_staff');
INSERT INTO `auth_permission` VALUES ('22', 'Can add dept', '8', 'add_dept');
INSERT INTO `auth_permission` VALUES ('23', 'Can change dept', '8', 'change_dept');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete dept', '8', 'delete_dept');
INSERT INTO `auth_permission` VALUES ('25', 'Can add check type', '9', 'add_checktype');
INSERT INTO `auth_permission` VALUES ('26', 'Can change check type', '9', 'change_checktype');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete check type', '9', 'delete_checktype');
INSERT INTO `auth_permission` VALUES ('28', 'Can add time setting', '10', 'add_timesetting');
INSERT INTO `auth_permission` VALUES ('29', 'Can change time setting', '10', 'change_timesetting');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete time setting', '10', 'delete_timesetting');
INSERT INTO `auth_permission` VALUES ('31', 'Can add user type', '11', 'add_usertype');
INSERT INTO `auth_permission` VALUES ('32', 'Can change user type', '11', 'change_usertype');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete user type', '11', 'delete_usertype');
INSERT INTO `auth_permission` VALUES ('34', 'Can add check info', '12', 'add_checkinfo');
INSERT INTO `auth_permission` VALUES ('35', 'Can change check info', '12', 'change_checkinfo');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete check info', '12', 'delete_checkinfo');
INSERT INTO `auth_permission` VALUES ('37', 'Can add reply_ img', '13', 'add_reply_img');
INSERT INTO `auth_permission` VALUES ('38', 'Can change reply_ img', '13', 'change_reply_img');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete reply_ img', '13', 'delete_reply_img');
INSERT INTO `auth_permission` VALUES ('40', 'Can add daily', '14', 'add_daily');
INSERT INTO `auth_permission` VALUES ('41', 'Can change daily', '14', 'change_daily');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete daily', '14', 'delete_daily');
INSERT INTO `auth_permission` VALUES ('43', 'Can add reply', '15', 'add_reply');
INSERT INTO `auth_permission` VALUES ('44', 'Can change reply', '15', 'change_reply');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete reply', '15', 'delete_reply');
INSERT INTO `auth_permission` VALUES ('46', 'Can add 新闻', '16', 'add_theme');
INSERT INTO `auth_permission` VALUES ('47', 'Can change 新闻', '16', 'change_theme');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete 新闻', '16', 'delete_theme');
INSERT INTO `auth_permission` VALUES ('49', 'Can add system setting', '17', 'add_systemsetting');
INSERT INTO `auth_permission` VALUES ('50', 'Can change system setting', '17', 'change_systemsetting');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete system setting', '17', 'delete_systemsetting');
INSERT INTO `auth_permission` VALUES ('52', 'Can add theme_ img', '18', 'add_theme_img');
INSERT INTO `auth_permission` VALUES ('53', 'Can change theme_ img', '18', 'change_theme_img');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete theme_ img', '18', 'delete_theme_img');
INSERT INTO `auth_permission` VALUES ('55', 'Can add leave', '19', 'add_leave');
INSERT INTO `auth_permission` VALUES ('56', 'Can change leave', '19', 'change_leave');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete leave', '19', 'delete_leave');
INSERT INTO `auth_permission` VALUES ('58', 'Can add notice', '20', 'add_notice');
INSERT INTO `auth_permission` VALUES ('59', 'Can change notice', '20', 'change_notice');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete notice', '20', 'delete_notice');
INSERT INTO `auth_permission` VALUES ('61', 'Can add notice_ img', '21', 'add_notice_img');
INSERT INTO `auth_permission` VALUES ('62', 'Can change notice_ img', '21', 'change_notice_img');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete notice_ img', '21', 'delete_notice_img');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$PQ3WPiYjZPSD$9c2vl8s3krC7R9yO8pV5qpezI78dozqV+ybmIYFOLSQ=', '2018-01-12 05:32:56.069213', '1', 'twilight', '', '', '', '1', '1', '2017-12-25 09:31:28.172499');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2017-12-25 09:36:51.070129', '2', '财务部', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2017-12-25 09:37:04.185299', '2', '财务部', '2', '[]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2017-12-25 09:38:06.188563', '1', '普通员工', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2017-12-25 09:38:24.945457', '2', '人事管理', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2017-12-25 09:38:55.276938', '3', '经理', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2017-12-25 09:39:15.252740', '4', '管理员', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2017-12-25 09:43:36.983311', 'sakura', 'sakura', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2017-12-25 09:45:48.451056', '签到', '签到', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2017-12-25 09:46:02.903613', '签退', '签退', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2017-12-25 09:46:14.147671', '请假', '请假', '1', '[{\"added\": {}}]', '9', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('12', 'winter_sakura', 'checkinfo');
INSERT INTO `django_content_type` VALUES ('9', 'winter_sakura', 'checktype');
INSERT INTO `django_content_type` VALUES ('14', 'winter_sakura', 'daily');
INSERT INTO `django_content_type` VALUES ('8', 'winter_sakura', 'dept');
INSERT INTO `django_content_type` VALUES ('19', 'winter_sakura', 'leave');
INSERT INTO `django_content_type` VALUES ('20', 'winter_sakura', 'notice');
INSERT INTO `django_content_type` VALUES ('21', 'winter_sakura', 'notice_img');
INSERT INTO `django_content_type` VALUES ('15', 'winter_sakura', 'reply');
INSERT INTO `django_content_type` VALUES ('13', 'winter_sakura', 'reply_img');
INSERT INTO `django_content_type` VALUES ('7', 'winter_sakura', 'staff');
INSERT INTO `django_content_type` VALUES ('17', 'winter_sakura', 'systemsetting');
INSERT INTO `django_content_type` VALUES ('16', 'winter_sakura', 'theme');
INSERT INTO `django_content_type` VALUES ('18', 'winter_sakura', 'theme_img');
INSERT INTO `django_content_type` VALUES ('10', 'winter_sakura', 'timesetting');
INSERT INTO `django_content_type` VALUES ('11', 'winter_sakura', 'usertype');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-12-24 08:46:10.185392');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-12-24 08:46:15.610662');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-12-24 08:46:16.762924');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-12-24 08:46:16.807865');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-12-24 08:46:17.501148');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-12-24 08:46:17.840955');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-12-24 08:46:18.211136');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-12-24 08:46:18.278533');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-12-24 08:46:18.811564');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-12-24 08:46:18.859937');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-12-24 08:46:18.905771');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2017-12-24 08:46:19.371142');
INSERT INTO `django_migrations` VALUES ('13', 'sessions', '0001_initial', '2017-12-24 08:46:20.059412');
INSERT INTO `django_migrations` VALUES ('14', 'winter_sakura', '0001_initial', '2017-12-24 08:46:32.654213');
INSERT INTO `django_migrations` VALUES ('15', 'winter_sakura', '0002_auto_20171224_1640', '2017-12-24 08:46:34.080000');
INSERT INTO `django_migrations` VALUES ('16', 'winter_sakura', '0003_auto_20171225_1558', '2017-12-25 07:58:41.479256');
INSERT INTO `django_migrations` VALUES ('17', 'winter_sakura', '0004_auto_20171225_1559', '2017-12-25 07:59:50.205302');
INSERT INTO `django_migrations` VALUES ('18', 'winter_sakura', '0005_auto_20171225_1743', '2017-12-25 09:43:13.131209');
INSERT INTO `django_migrations` VALUES ('19', 'winter_sakura', '0006_auto_20171226_2023', '2017-12-26 12:24:03.185843');
INSERT INTO `django_migrations` VALUES ('20', 'winter_sakura', '0007_auto_20171230_1902', '2018-01-06 15:47:25.874825');
INSERT INTO `django_migrations` VALUES ('21', 'winter_sakura', '0008_auto_20180106_2349', '2018-01-06 15:50:36.113958');
INSERT INTO `django_migrations` VALUES ('22', 'winter_sakura', '0009_auto_20180106_2350', '2018-01-06 15:50:36.662768');
INSERT INTO `django_migrations` VALUES ('23', 'winter_sakura', '0010_auto_20180107_0147', '2018-01-06 17:48:24.276428');
INSERT INTO `django_migrations` VALUES ('24', 'winter_sakura', '0011_auto_20180107_0152', '2018-01-06 17:52:25.328893');
INSERT INTO `django_migrations` VALUES ('25', 'winter_sakura', '0012_auto_20180107_1334', '2018-01-07 05:34:53.559826');
INSERT INTO `django_migrations` VALUES ('26', 'winter_sakura', '0013_auto_20180107_1334', '2018-01-07 05:34:53.649375');
INSERT INTO `django_migrations` VALUES ('27', 'winter_sakura', '0014_auto_20180107_1402', '2018-01-07 06:18:07.035362');
INSERT INTO `django_migrations` VALUES ('28', 'winter_sakura', '0015_auto_20180107_1412', '2018-01-07 06:18:07.751566');
INSERT INTO `django_migrations` VALUES ('29', 'winter_sakura', '0016_auto_20180107_1441', '2018-01-07 06:41:27.327892');
INSERT INTO `django_migrations` VALUES ('30', 'winter_sakura', '0017_auto_20180111_0206', '2018-01-10 18:06:55.200634');
INSERT INTO `django_migrations` VALUES ('31', 'winter_sakura', '0018_auto_20180111_0440', '2018-01-10 20:40:53.881689');
INSERT INTO `django_migrations` VALUES ('32', 'winter_sakura', '0019_auto_20180111_0446', '2018-01-10 20:53:32.880729');
INSERT INTO `django_migrations` VALUES ('33', 'winter_sakura', '0020_auto_20180111_0449', '2018-01-10 20:53:32.952712');
INSERT INTO `django_migrations` VALUES ('34', 'winter_sakura', '0021_auto_20180111_0454', '2018-01-10 20:55:55.013717');
INSERT INTO `django_migrations` VALUES ('35', 'winter_sakura', '0022_leave_state', '2018-01-13 07:43:18.629486');
INSERT INTO `django_migrations` VALUES ('36', 'winter_sakura', '0023_leave_create_date', '2018-01-13 07:53:52.243717');
INSERT INTO `django_migrations` VALUES ('37', 'winter_sakura', '0024_leave_staff_no', '2018-01-13 08:01:20.492281');
INSERT INTO `django_migrations` VALUES ('38', 'winter_sakura', '0025_leave_check_id', '2018-01-13 08:26:35.285303');
INSERT INTO `django_migrations` VALUES ('39', 'winter_sakura', '0026_remove_leave_staff_dept', '2018-01-13 08:36:16.175186');
INSERT INTO `django_migrations` VALUES ('40', 'winter_sakura', '0027_auto_20180114_0711', '2018-01-14 07:11:43.990612');
INSERT INTO `django_migrations` VALUES ('41', 'winter_sakura', '0028_auto_20180114_0712', '2018-01-14 07:12:19.434575');
INSERT INTO `django_migrations` VALUES ('42', 'winter_sakura', '0029_auto_20180114_0829', '2018-01-14 08:29:42.319286');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('5zlqldnjwtft04dcisejd5l57sfeahir', 'YmZjOGNjZDNmMDBmMjUzYjQ5ZDJkZjFhYjQxZDg2N2M3NGY0MGM3NTp7InVzZXJuYW1lIjoibWFuYWdlciIsIm5pY2tuYW1lIjoiXHU2MjExXHU2NjJmXHU3YmExXHU3NDA2In0=', '2018-01-28 13:52:28.828677');
INSERT INTO `django_session` VALUES ('pipcdtuyvprwex107eda9uzb7w8qms61', 'NDBiMmVkOGZlZGY2OGJiMWZhNDUxNmI1ZTNlMTlhZDIwMjU3ZGI4ZDp7InVzZXJuYW1lIjoidHdpbGlnaHQiLCJuaWNrbmFtZSI6Ilx1NWU3ZFx1OWIzY1x1NTE1NCJ9', '2018-01-28 15:23:49.959943');
INSERT INTO `django_session` VALUES ('z4oyp52dx73ln0wdamh61ds6gvu6vomp', 'YmZjOGNjZDNmMDBmMjUzYjQ5ZDJkZjFhYjQxZDg2N2M3NGY0MGM3NTp7InVzZXJuYW1lIjoibWFuYWdlciIsIm5pY2tuYW1lIjoiXHU2MjExXHU2NjJmXHU3YmExXHU3NDA2In0=', '2018-01-28 14:03:55.092671');
INSERT INTO `django_session` VALUES ('za5hizmjxtmsqycz495dutd1e1pdg695', 'YmIyNmE3NWM2MDBjNTc4YWU5ODQzZmQ3ZTZlMWU5MzQzYzcwNzdkODp7InVzZXJuYW1lIjoidHdpbGlnaHQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMyNzE1NzU0OTMzNDdlNDY3OGRhMDkwYWFhNjk5MTM4M2Q1MzEwMGUiLCJfYXV0aF91c2VyX2lkIjoiMSIsIm5pY2tuYW1lIjoiXHU1ZTdkXHU5YjNjXHU1MTU0In0=', '2018-01-27 06:55:47.444278');

-- ----------------------------
-- Table structure for winter_sakura_checkinfo
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_checkinfo`;
CREATE TABLE `winter_sakura_checkinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `check_time` datetime(6) NOT NULL,
  `remarks` varchar(25) DEFAULT NULL,
  `check_type_id` int(11) NOT NULL,
  `dept_id_id` int(11) NOT NULL,
  `staff_id_id` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_checki_check_type_id_ebfcf32d_fk_winter_sa` (`check_type_id`),
  KEY `winter_sakura_checki_dept_id_id_757f3ab1_fk_winter_sa` (`dept_id_id`),
  KEY `winter_sakura_checki_staff_id_id_e0fd749b_fk_winter_sa` (`staff_id_id`),
  CONSTRAINT `winter_sakura_checki_check_type_id_ebfcf32d_fk_winter_sa` FOREIGN KEY (`check_type_id`) REFERENCES `winter_sakura_checktype` (`id`),
  CONSTRAINT `winter_sakura_checki_dept_id_id_757f3ab1_fk_winter_sa` FOREIGN KEY (`dept_id_id`) REFERENCES `winter_sakura_dept` (`id`),
  CONSTRAINT `winter_sakura_checki_staff_id_id_e0fd749b_fk_winter_sa` FOREIGN KEY (`staff_id_id`) REFERENCES `winter_sakura_staff` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_checkinfo
-- ----------------------------
INSERT INTO `winter_sakura_checkinfo` VALUES ('51', '2018-01-14 05:22:54.050464', '已通过', '3', '3', 'twilight');
INSERT INTO `winter_sakura_checkinfo` VALUES ('52', '2018-01-14 05:48:31.910086', '已驳回', '3', '3', 'twilight');
INSERT INTO `winter_sakura_checkinfo` VALUES ('53', '2018-01-14 13:51:55.025236', '已驳回', '3', '3', 'lucas');
INSERT INTO `winter_sakura_checkinfo` VALUES ('54', '2018-01-14 13:56:27.057024', '已通过', '3', '3', 'lucas');
INSERT INTO `winter_sakura_checkinfo` VALUES ('55', '2018-01-14 14:05:09.643547', null, '1', '3', 'twilight');
INSERT INTO `winter_sakura_checkinfo` VALUES ('56', '2018-01-14 14:05:16.440916', null, '2', '3', 'twilight');
INSERT INTO `winter_sakura_checkinfo` VALUES ('57', '2018-01-14 14:33:48.355274', null, '1', '3', 'twilight');
INSERT INTO `winter_sakura_checkinfo` VALUES ('58', '2018-01-14 14:33:57.615700', null, '2', '3', 'twilight');
INSERT INTO `winter_sakura_checkinfo` VALUES ('59', '2018-01-14 14:34:32.441014', null, '1', '3', 'lucas');
INSERT INTO `winter_sakura_checkinfo` VALUES ('60', '2018-01-14 14:35:55.813476', null, '1', '2', 'rabbit');
INSERT INTO `winter_sakura_checkinfo` VALUES ('61', '2018-01-14 14:48:03.393662', null, '1', '2', 'rabbit');
INSERT INTO `winter_sakura_checkinfo` VALUES ('62', '2018-01-14 14:48:07.322521', null, '2', '2', 'rabbit');
INSERT INTO `winter_sakura_checkinfo` VALUES ('63', '2018-01-14 14:48:26.423343', null, '1', '3', 'twilight');
INSERT INTO `winter_sakura_checkinfo` VALUES ('64', '2018-01-14 14:48:56.654277', null, '1', '3', 'lucas');

-- ----------------------------
-- Table structure for winter_sakura_checktype
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_checktype`;
CREATE TABLE `winter_sakura_checktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_checktype
-- ----------------------------
INSERT INTO `winter_sakura_checktype` VALUES ('1', '签到');
INSERT INTO `winter_sakura_checktype` VALUES ('2', '签退');
INSERT INTO `winter_sakura_checktype` VALUES ('3', '请假');

-- ----------------------------
-- Table structure for winter_sakura_daily
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_daily`;
CREATE TABLE `winter_sakura_daily` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_count` int(11) NOT NULL,
  `check_staff` int(11) NOT NULL,
  `uncheck_staff` int(11) NOT NULL,
  `late_staff` int(11) NOT NULL,
  `leave_staff` int(11) NOT NULL,
  `daily_text` longtext NOT NULL,
  `create_time` date NOT NULL,
  `late_and_leave_staff` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_daily
-- ----------------------------
INSERT INTO `winter_sakura_daily` VALUES ('67', '4', '0', '1', '2', '0', '缺勤人员：李强(312)  |正常考勤人员:  |迟到人员:徐中华(121)李华俊(213)  |早退人员:  |迟到早退人员:王洪棚(310)', '2018-01-14', '1');

-- ----------------------------
-- Table structure for winter_sakura_dept
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_dept`;
CREATE TABLE `winter_sakura_dept` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(20) NOT NULL,
  `charge` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_dept
-- ----------------------------
INSERT INTO `winter_sakura_dept` VALUES ('1', '人事部', '强哥');
INSERT INTO `winter_sakura_dept` VALUES ('2', '财务部', '李哥');
INSERT INTO `winter_sakura_dept` VALUES ('3', '开发部', '杰哥');
INSERT INTO `winter_sakura_dept` VALUES ('4', '营销部', '尚哥');

-- ----------------------------
-- Table structure for winter_sakura_leave
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_leave`;
CREATE TABLE `winter_sakura_leave` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(50) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  `staff_id_id` varchar(25) NOT NULL,
  `state` int(11) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `staff_no` varchar(20) DEFAULT NULL,
  `check_id_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_leave_staff_id_id_0c1a0096_fk_winter_sa` (`staff_id_id`),
  KEY `winter_sakura_leave_check_id_id_1dc076f4_fk_winter_sa` (`check_id_id`),
  CONSTRAINT `winter_sakura_leave_check_id_id_1dc076f4_fk_winter_sa` FOREIGN KEY (`check_id_id`) REFERENCES `winter_sakura_checkinfo` (`id`),
  CONSTRAINT `winter_sakura_leave_staff_id_id_0c1a0096_fk_winter_sa` FOREIGN KEY (`staff_id_id`) REFERENCES `winter_sakura_staff` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_leave
-- ----------------------------
INSERT INTO `winter_sakura_leave` VALUES ('4', '感冒发烧', '2018-01-14 00:00:00.000000', '2018-01-15 00:00:00.000000', 'twilight', '1', '2018-01-14 05:22:54.070478', '310', '51');
INSERT INTO `winter_sakura_leave` VALUES ('5', '不想上班', '2018-01-14 00:00:00.000000', '2018-01-15 00:00:00.000000', 'twilight', '2', '2018-01-14 05:48:31.911067', '310', '52');
INSERT INTO `winter_sakura_leave` VALUES ('6', '闺蜜结婚', '2018-01-15 00:00:00.000000', '2018-01-17 00:00:00.000000', 'lucas', '2', '2018-01-14 13:51:55.027237', '312', '53');
INSERT INTO `winter_sakura_leave` VALUES ('7', '拉肚子', '2018-01-16 00:00:00.000000', '2018-01-18 00:00:00.000000', 'lucas', '1', '2018-01-14 13:56:27.062029', '312', '54');

-- ----------------------------
-- Table structure for winter_sakura_notice
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_notice`;
CREATE TABLE `winter_sakura_notice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notice_text` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `pub_user_id` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_notice_pub_user_id_07939a56_fk_winter_sa` (`pub_user_id`),
  CONSTRAINT `winter_sakura_notice_pub_user_id_07939a56_fk_winter_sa` FOREIGN KEY (`pub_user_id`) REFERENCES `winter_sakura_staff` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_notice
-- ----------------------------
INSERT INTO `winter_sakura_notice` VALUES ('1', '测试公告1', '2018-01-14 08:59:36.878322', 'manager');
INSERT INTO `winter_sakura_notice` VALUES ('2', '测试公告2', '2018-01-14 09:00:17.911160', 'manager');
INSERT INTO `winter_sakura_notice` VALUES ('3', '今天，全体放假，公司集体出公费旅游。', '2018-01-14 15:23:08.170549', 'manager');

-- ----------------------------
-- Table structure for winter_sakura_notice_img
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_notice_img`;
CREATE TABLE `winter_sakura_notice_img` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_url` varchar(100) NOT NULL,
  `tid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_notice_tid_id_aab6cf25_fk_winter_sa` (`tid_id`),
  CONSTRAINT `winter_sakura_notice_tid_id_aab6cf25_fk_winter_sa` FOREIGN KEY (`tid_id`) REFERENCES `winter_sakura_notice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_notice_img
-- ----------------------------

-- ----------------------------
-- Table structure for winter_sakura_reply
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_reply`;
CREATE TABLE `winter_sakura_reply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `theme_id` int(11) NOT NULL,
  `user_id` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_reply_theme_id_0dd55a2b_fk_winter_sakura_theme_id` (`theme_id`),
  KEY `winter_sakura_reply_user_id_0cc16020_fk_winter_sa` (`user_id`),
  CONSTRAINT `winter_sakura_reply_theme_id_0dd55a2b_fk_winter_sakura_theme_id` FOREIGN KEY (`theme_id`) REFERENCES `winter_sakura_theme` (`id`),
  CONSTRAINT `winter_sakura_reply_user_id_0cc16020_fk_winter_sa` FOREIGN KEY (`user_id`) REFERENCES `winter_sakura_staff` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_reply
-- ----------------------------
INSERT INTO `winter_sakura_reply` VALUES ('1', '测试回复1', '2018-01-14 04:52:54.897752', '6', 'twilight');
INSERT INTO `winter_sakura_reply` VALUES ('2', '非常同意，大家应该都去学PHP！', '2018-01-14 15:24:38.059957', '7', 'twilight');

-- ----------------------------
-- Table structure for winter_sakura_reply_img
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_reply_img`;
CREATE TABLE `winter_sakura_reply_img` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_url` varchar(100) NOT NULL,
  `rid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_reply__rid_id_6e1b397c_fk_winter_sa` (`rid_id`),
  CONSTRAINT `winter_sakura_reply__rid_id_6e1b397c_fk_winter_sa` FOREIGN KEY (`rid_id`) REFERENCES `winter_sakura_reply` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_reply_img
-- ----------------------------

-- ----------------------------
-- Table structure for winter_sakura_staff
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_staff`;
CREATE TABLE `winter_sakura_staff` (
  `username` varchar(25) NOT NULL,
  `password` varchar(200) NOT NULL,
  `sex` varchar(20) NOT NULL,
  `true_name` varchar(25) NOT NULL,
  `tel` varchar(25) NOT NULL,
  `address` varchar(25) DEFAULT NULL,
  `staff_dept_id` int(11) NOT NULL,
  `user_type_id` int(11) NOT NULL,
  `staff_no` varchar(20) DEFAULT NULL,
  `nickname` varchar(20) NOT NULL,
  `active_session` varchar(50) DEFAULT NULL,
  `state` int(11) NOT NULL,
  `day_note` int(11) NOT NULL,
  PRIMARY KEY (`username`),
  KEY `winter_sakura_staff_staff_dept_id_0dfc8ef0_fk_winter_sa` (`staff_dept_id`),
  KEY `winter_sakura_staff_user_type_id_8832bca0_fk_winter_sa` (`user_type_id`),
  CONSTRAINT `winter_sakura_staff_staff_dept_id_0dfc8ef0_fk_winter_sa` FOREIGN KEY (`staff_dept_id`) REFERENCES `winter_sakura_dept` (`id`),
  CONSTRAINT `winter_sakura_staff_user_type_id_8832bca0_fk_winter_sa` FOREIGN KEY (`user_type_id`) REFERENCES `winter_sakura_usertype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_staff
-- ----------------------------
INSERT INTO `winter_sakura_staff` VALUES ('lucas', 'pbkdf2_sha256$36000$bCE1VPmgXY0S$LZ+nERwS4xVtWK/QuEJqpZBzlZGx0+GSxhL1qTLhMjk=', '男', '李强', '13507301856', '重庆市重庆文理学院', '3', '1', '312', '零点零', null, '0', '0');
INSERT INTO `winter_sakura_staff` VALUES ('manager', 'pbkdf2_sha256$36000$AlR1pYFUs3G1$PlhQnXsEJDLHves0lGjM4IRxfi+9xiqXuqpzYjIHKnc=', '男', '徐中华', '13507301606', '重庆市永川区', '1', '2', '121', '我是管理', null, '0', '0');
INSERT INTO `winter_sakura_staff` VALUES ('rabbit', 'pbkdf2_sha256$36000$G0rDkSqniZ8s$ANKRpAMaNRvXG7IKUSIvzdIT47+qzwS+GDP106sMeVg=', '男', '李华俊', '18873093850', '重庆市渝北区', '2', '1', '213', '乌拉拉', null, '0', '0');
INSERT INTO `winter_sakura_staff` VALUES ('twilight', 'pbkdf2_sha256$36000$hFmYLgiNJ3lR$P6XNTWE1T6GP3EwYC1DaBDgTWfKUyMR2w1vQSUv2ras=', '男', '王洪棚', '18873093850', 'snow', '3', '1', '310', '幽鬼兔', null, '0', '0');

-- ----------------------------
-- Table structure for winter_sakura_systemsetting
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_systemsetting`;
CREATE TABLE `winter_sakura_systemsetting` (
  `setting` varchar(20) NOT NULL,
  `value` int(11) NOT NULL,
  PRIMARY KEY (`setting`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_systemsetting
-- ----------------------------

-- ----------------------------
-- Table structure for winter_sakura_theme
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_theme`;
CREATE TABLE `winter_sakura_theme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` varchar(720) NOT NULL,
  `url` varchar(200) NOT NULL,
  `reply_count` int(11) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `user_id` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_theme_title_290912b5` (`title`),
  KEY `winter_sakura_theme_user_id_159e36b5_fk_winter_sa` (`user_id`),
  CONSTRAINT `winter_sakura_theme_user_id_159e36b5_fk_winter_sa` FOREIGN KEY (`user_id`) REFERENCES `winter_sakura_staff` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_theme
-- ----------------------------
INSERT INTO `winter_sakura_theme` VALUES ('1', '测试标题', '这里是测试内容', '', '0', '2018-01-14 03:43:10.554940', '2018-01-14 03:43:10.554940', 'twilight');
INSERT INTO `winter_sakura_theme` VALUES ('2', '测试标题2', '这里是测试内容2', '', '0', '2018-01-14 03:52:48.512865', '2018-01-14 03:52:48.512865', 'twilight');
INSERT INTO `winter_sakura_theme` VALUES ('3', '测试标题3', '这里是测试内容3', '', '0', '2018-01-14 04:25:11.194350', '2018-01-14 04:25:11.194350', 'twilight');
INSERT INTO `winter_sakura_theme` VALUES ('4', '测试标题4', '这里是测试内容4', '', '0', '2018-01-14 04:25:24.305710', '2018-01-14 04:25:24.305710', 'twilight');
INSERT INTO `winter_sakura_theme` VALUES ('5', '测试标题5', '这里是测试内容5', '', '0', '2018-01-14 04:25:35.470068', '2018-01-14 04:25:35.470068', 'twilight');
INSERT INTO `winter_sakura_theme` VALUES ('6', '测试标题6', '这里是测试内容6', '', '1', '2018-01-14 04:25:45.711100', '2018-01-14 04:25:45.711100', 'twilight');
INSERT INTO `winter_sakura_theme` VALUES ('7', 'PHP是最好的语言', 'PHP最强大，最完美！！！！', '', '1', '2018-01-14 15:24:05.315783', '2018-01-14 15:24:05.316284', 'manager');

-- ----------------------------
-- Table structure for winter_sakura_theme_img
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_theme_img`;
CREATE TABLE `winter_sakura_theme_img` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_url` varchar(100) NOT NULL,
  `tid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `winter_sakura_theme__tid_id_0a3be5c1_fk_winter_sa` (`tid_id`),
  CONSTRAINT `winter_sakura_theme__tid_id_0a3be5c1_fk_winter_sa` FOREIGN KEY (`tid_id`) REFERENCES `winter_sakura_theme` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_theme_img
-- ----------------------------

-- ----------------------------
-- Table structure for winter_sakura_timesetting
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_timesetting`;
CREATE TABLE `winter_sakura_timesetting` (
  `setting` varchar(20) NOT NULL,
  `value` time(6) NOT NULL,
  PRIMARY KEY (`setting`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_timesetting
-- ----------------------------
INSERT INTO `winter_sakura_timesetting` VALUES ('1', '09:00:00.000000');
INSERT INTO `winter_sakura_timesetting` VALUES ('2', '17:30:00.000000');

-- ----------------------------
-- Table structure for winter_sakura_usertype
-- ----------------------------
DROP TABLE IF EXISTS `winter_sakura_usertype`;
CREATE TABLE `winter_sakura_usertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of winter_sakura_usertype
-- ----------------------------
INSERT INTO `winter_sakura_usertype` VALUES ('1', '普通员工');
INSERT INTO `winter_sakura_usertype` VALUES ('2', '人事管理');
INSERT INTO `winter_sakura_usertype` VALUES ('3', '经理');
INSERT INTO `winter_sakura_usertype` VALUES ('4', '管理员');
