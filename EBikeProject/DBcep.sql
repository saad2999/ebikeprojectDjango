-- drop database Ebike;
Create database Ebike;
use Ebike;
Create table user (
userID int not null unique,
Fname varchar(20),
Lname varchar(20),
Gender char(1),
Email varchar(30),
contactno int(10),
primary key(userID)
);

create table battery(
batteryID int not null unique,
batteryTYPE varchar(100),
volts int(10),
Watthour int(10),
lifetime int(10),
primary key (batteryID)
);

create table motor(
motorID int not null unique,
motorTYPE varchar(10),
placement varchar(10),
Wattage int(10),
volts int(10),
manufacturer varchar(10),
primary key (motorID)
);

create table inverter(
inverterID int not null unique,
Wattage int(10),
volts int(10),
primary key (inverterID)
);

create table structure(
structureID int not null unique,
frame varchar(10),
payloadCAP int(10),
color varchar(10),
primary key (structureID)
);

Create table vehicle (
vehicleID int not null unique,
userID int,
structureID int,
batteryID int,
motorID int,
inverterID int,
vehicleTYPE varchar(10),
weightKG int,
OrderDATE datetime,
warantyDATE datetime,
tyre varchar(10),
helmet varchar(10),
pedal varchar(10),
meter varchar(10),
primary key(vehicleID),
foreign key (userID) References user(userID) 
ON UPDATE CASCADE On delete restrict,
Foreign key (batteryID) References battery(batteryID) 
ON UPDATE CASCADE On delete restrict,
Foreign key (motorID) References motor(motorID) 
ON UPDATE CASCADE On delete restrict,
Foreign key (inverterID) References inverter(inverterID) 
ON UPDATE CASCADE On delete restrict,
Foreign key (structureID) References structure(structureID) 
ON UPDATE CASCADE On delete restrict
);

Create table review(
reviewNO int not null unique,
reviewTEXT varchar(50),
userID int,
vehicleID int,
primary key (reviewNO),
foreign key (userID) References user(userID) 
ON UPDATE CASCADE On delete restrict,
Foreign key (vehicleID) References vehicle(vehicleID) 
ON UPDATE CASCADE On delete restrict

);




create table billingDetails(
detailno int not null unique,
userID int,
address varchar(50),
country varchar(15),
zip int(10),
CCno int(10),
promocode varchar(10),
primary key (userID,detailno),
foreign key (userID) References user(userID) 
ON UPDATE CASCADE On delete restrict
);



