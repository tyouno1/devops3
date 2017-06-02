--USER
CREATE TABLE `user` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`username` varchar(40) NOT NULL COMMENT '用户名',
`password` varchar(64) NOT NULL COMMENT '密码',
`name` varchar(80) NOT NULL COMMENT '姓名',
`email` varchar(64) NOT NULL COMMENT '公司邮箱',
`mobile` varchar(16) NOT NULL COMMENT '手机号',
`r_id`  varchar(32) NOT NULL COMMENT '角色允许多个,以逗号分隔',
`is_lock` tinyint NOT NULL COMMENT '是否锁定 0:未锁定，1:锁定',
`join_date` datetime NOT NULL COMMENT '注册时间',
`last_login` datetime NOT NULL COMMENT '最后登录时间',
primary key (`id`),
unique key `username`(`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--role
CREATE TABLE `role` (
`id` int unsigned NOT NULL AUTO_INCREMENT,
`name`  varchar(20) NOT NULL COMMENT '角色名',
`name_cn` varchar(40) NOT NULL COMMENT '角色中文名',
`p_id`  varchar(20) NOT NULL COMMENT '权限id,允许多个p_id,存为字符串类型',
`info`  varchar(50) DEFAULT NULL COMMENT '角色描述信息'
PRIMARY KEY (`id`),
UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--power
CREATE TABLE `power` (
`id` int unsigned NOT NULL AUTO_INCREMENT,
`name`  varchar(20) NOT NULL COMMENT '权限名',
`name_cn` varchar(40) NOT NULL COMMENT '权限中文名',
`url`  varchar(128) NOT NULL COMMENT '权限对应的URL',
`comment`  varchar(128) DEFAULT NULL COMMENT '备注'
PRIMARY KEY (`id`),
UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
