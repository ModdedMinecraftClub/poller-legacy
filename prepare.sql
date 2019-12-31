-- Create database
create database poller;

-- Create tables
create table server
(
	serverId int auto_increment
		primary key,
	serverIp varchar(50) not null,
	serverPort int(16) not null,
	serverName varchar(50) null,
	enabled tinyint(1) not null
);

create table pings
(
	serverId int null,
	pingTime datetime null,
	playersOnline int null,
	playersMax int null,
	constraint pings_server_serverId_fk
		foreign key (serverId) references server (serverId)
);
