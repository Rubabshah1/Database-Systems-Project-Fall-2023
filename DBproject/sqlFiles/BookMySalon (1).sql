create table Salons(
SalonID INT PRIMARY KEY IDENTITY(101,1),
Name nvarchar(30),
PlotNo int,
StreetNo int,
AreaCode nvarchar(10),
City char(15))

ALTER TABLE Salons
ADD PostalCode INT;

create table Customer (
CustomerID INT PRIMARY KEY IDENTITY(201,1),
Name nvarchar(30),
Email nvarchar(60),
Contact_number int)

create table Account(
LoginID INT PRIMARY KEY IDENTITY(111,1),
UserName varchar(20),
Password nvarchar(15),
customerID int,
Foreign Key (customerID) References Customer(CustomerID))

create table Employee(
EmployeeID INT IDENTITY(401,1),
Name nvarchar(30),
Joining_Date Date,
Contact_number int,
Email nvarchar(60),
Specialty varchar(100),
Salary int,
Rating int)
Alter Table Employee
ADD SalonID int not null,
Foreign Key (SalonID) References Salons(SalonID)
Alter Table Employee
ADD Primary Key (EmployeeID, SalonID)

CREATE TABLE Product (
    ProductID int identity(1,1),
    Product_Name nvarchar(30),
    Price int,
    Primary Key(ProductID)
);

create table Services(
ServicesID int identity (1,1),
Name nvarchar(30),
Description varchar(100),
Price int,
Duration int,
ProductID int,
Primary Key (ServicesID),
Foreign Key (ProductID) REFERENCES Product(ProductID))

create table Salon_Serv(
ServicesID int,
SalonID int,
Primary Key(ServicesID, SalonID),
Foreign Key(ServicesID) References Services(ServicesID),
Foreign Key (SalonID) References Salons(SalonID))

create table Appointment(
ApptID int identity (1,1),
CustomerID int not null,
Date date,
Time time,
ServicesID int,
EmployeeID int,
SalonID int,
Primary Key (ApptID, CustomerID),
Foreign Key (CustomerID) References Customer(CustomerID),
Foreign Key(EmployeeID,SalonID) References Employee(EmployeeID,SalonID),
Foreign Key (SalonID) References Salons(SalonID),
Foreign Key (ServicesID) References Services (ServicesID))

create table Receipt(
ReceiptID int identity(1,1),
ApptID int,
CustomerID int,
PayMethod char(15),
TotalAmt int,
Primary Key(ReceiptID, ApptID, CustomerID),
Foreign Key (ApptID, CustomerID) References Appointment(ApptID, CustomerID),
Foreign Key (CustomerID) References Customer(CustomerID))

create table Availability(
SalonID int not null,
EmployeeID int not null,
Day char(10),
Date date,
Time time,
Primary Key(SalonID, EmployeeID),
Foreign Key (EmployeeID,SalonID) References Employee(EmployeeID,SalonID),
Foreign Key (SalonID) References Salons(SalonID))

create table Manager(
SalonID int not null,
EmployeeID int not null,
Primary Key(SalonID, EmployeeID),
Foreign Key (EmployeeID,SalonID) References Employee(EmployeeID,SalonID),
Foreign Key (SalonID) References Salons(SalonID))

create table SalonRating(
RatingID int identity(1,1),
SalonID int,
Rating int,
Month char(11),
Year int,
Primary Key(RatingID, SalonID),
Foreign Key (SalonID) References Salons(SalonID))

create table Service_Product(
ServicesID int,
ProductID int,
Primary Key (ServicesID, ProductID),
Foreign Key(ServicesID) References Services(ServicesID),
Foreign Key (ProductID) References Product (ProductID))

create table Inventory(
SalonID int,
ProductID int,
QuantityLeft int,
Primary Key (SalonID, ProductID),
Foreign Key (SalonID) References Salons(SalonID),
Foreign Key (ProductID) References Product (ProductID))

create table Suppliers(
SupplierID int identity(1,1),
ProductID int,
Sup_Contact int,
Sup_Email nvarchar(60),
Primary Key (SupplierID,ProductID),
Foreign Key (ProductID) References Product (ProductID))

create table Orders(
OrderID int identity(1,1),
SalonID int,
ProductID int,
SupplierID int,
QuantOrdered int,
Primary Key (OrderID),
Foreign Key (SalonID) References Salons(SalonID),
Foreign Key (ProductID) References Product(ProductID),
Foreign Key (SupplierID, ProductID) References Suppliers(SupplierID,ProductID))
