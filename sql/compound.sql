CREATE TABLE `compound_basic`(
`compound_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '化合物ID' ,
`cas` varchar(20)  NOT NULL COMMENT 'CAS',
`chinese_name` VARCHAR(255) NOT NULL COMMENT '中文名字',
`english_name` VARCHAR(255)  NOT NULL COMMENT '英文名字',
`Molecular_formula` VARCHAR(255)  NOT NULL COMMENT '分子式',
`Molecular_weight` VARCHAR(255)  NOT NULL COMMENT '分子量',
`Structural_formula` varchar(128) NULL COMMENT '头像', 
`status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否删除，0-否，1-是',
`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
`update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
	PRIMARY KEY (`compound_id`),
  	UNIQUE KEY `cas` (`cas`),
	UNIQUE KEY `chinese_name` (`chinese_name`),
	UNIQUE KEY `english_name` (`english_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='化合物基本信息表';


CREATE TABLE `compound_profile`(
`compound_id` bigint(20) unsigned NOT NULL COMMENT '化合物ID' ,
`Melting_point` varchar(20)   NULL COMMENT '熔点',
`Boiling_point` VARCHAR(20)  NULL COMMENT '沸点',
`density` VARCHAR(20)   NULL COMMENT '密度',
`Refractive_index` VARCHAR(50)  NOT NULL COMMENT '折射率',
`Flash_point` VARCHAR(20)  NOT NULL COMMENT '闪点',
`Steam_density` varchar(128) NULL COMMENT '蒸汽密度', 
`Storage_conditions` varchar(128) NULL COMMENT '存储条件',
`form` VARCHAR(128)  NOT NULL COMMENT '形态',
`color` varchar(128) NULL COMMENT '颜色', 
`Solubility` varchar(128) NULL COMMENT '溶解性',
`Sensitivity` varchar(128) NULL COMMENT '敏感性',
`Special_properties` varchar(128) NULL COMMENT '特殊性质',
`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
`update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
	PRIMARY KEY (`compound_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='化合物详细信息表';


