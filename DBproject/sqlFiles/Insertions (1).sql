
set identity_insert Salons ON
INSERT INTO Salons (SalonID, Name, PlotNo, StreetNo, AreaCode, City, PostalCode)
VALUES 
	(101,'Elegant Cuts',203,45,10345,'Karachi', 74700),
	(102, 'Chic Styles',305,78, 23456,'Lahore', 54500),
	(103,'Glamorous Haven',408,12, 34567,'Islamabad', 44100),
	(104, 'Tress Trends', 512, 63, 45678, 'Rawalpindi', 46200),
    (105, 'Vogue Studio', 617, 94, 56789, 'Faisalabad', 38860),
    (106, 'Shear Elegance', 720, 27, 67890, 'Peshawar', 25000),
    (107, 'Snip & Style', 823, 58, 78901, 'Quetta', 87300),
    (108, 'The Mane Place', 936, 31, 89012, 'Multan', 61000),
    (109, 'Posh Parlor', 1040, 74, 90123, 'Sialkot', 51311),
    (110, 'Divine Locks', 1154, 19, 12347, 'Gujranwala', 54560),
    (111, 'Style Sanctuary', 1267, 82, 12345, 'Faisalabad', 38090),
    (112, 'Aura Salon', 1371, 35, 23456, 'Islamabad',44666),
    (113, 'Eclat Elegance', 1485, 68, 34567, 'Rawalpindi', 46300),
    (114, 'Panache Palace', 1599, 13, 45678, 'Peshawar', 25120),
    (115, 'Elite Styles', 1612, 46, 56789, 'Lahore',53701);

Set identity_insert Salons Off
Set identity_insert Customer ON
INSERT INTO Customer (CustomerID, Name, Email, Contact_Number)
VALUES
    (201, 'John Doe', 'john.doe@email.com', 123456),
    (202, 'Jane Smith', 'jane.smith@email.com', 987654),
    (203, 'Bob Johnson', 'bob.johnson@email.com', 456789),
    (204, 'Alice Brown', 'alice.brown@email.com', 789012),
    (205, 'Emily Davis', 'em.dave@email.com', 234567),
    (206, 'Emma White', 'emma.white@email.com', 890123),
    (207, 'David Miller', 'david.miller@email.com', 345678),
    (208, 'Grace Taylor', 'grace.taylor@email.com', 678901),
    (209, 'Kevin Wilson', 'kevin.wilson@email.com', 901234),
    (210, 'Lily Parker', 'lily.parker@email.com', 234667),
    (211, 'Mark Davis', 'mark.davis@email.com', 567890),
    (212, 'Olivia Moore', 'olivia.moore@email.com', 891123),
    (213, 'Ryan Adams', 'ryan.adams@email.com', 123890),
    (214, 'Sophia Reed', 'sophia.reed@email.com', 456790),
    (215, 'Tyler Harris', 'tyler.harris@email.com', 789456);

Set identity_insert Customer Off

Set identity_insert Account ON
INSERT INTO Account (LoginID, UserName, Password, customerID)
VALUES
	(111, 'user1', 'P@ssw0rd1', 201),
    (121, 'jane_smith', 'Secure123!', 202),
    (131, 'random_user', 'Passw0rd@', 203 ),
    (141, 'access_granted', '9876Pass!', 204),
    (151, 'emily_davis', 'LetMeIn2023', 205),
    (161, 'unique123', 'Pa$$w0rd', 206),
    (171, 'secret_squirrel', 'HiddenPwd45', 207),
    (181, 'alpha_beta', 'Abcd@1234', 208),
    (191, 'test_user', 'Testing!234', 209),
    (1101, 'secure_acc', 'Secur3P@ss!', 210),
    (1111, 'user1234', 'Pwd!user123', 211),
    (1121, 'access123', 'A1b2C#d3', 212),
    (1131, 'my_account', 'MyP@ssword!', 213),
    (1141, '2FA_user', 'TwoFactorPwd!', 214),
    (1151, 'new_member', 'N3wMemb#r', 215);



Set identity_insert Account Off

Set identity_insert Employee ON
INSERT INTO Employee (EmployeeID, SalonID, Name, Joining_Date, Contact_number, Email, Specialty, Salary, Rating)

VALUES
    (401, 101, 'Ayesha Khan', '2022-01-15', 111222, 'ayesha.khan@email.com', 'Hair Styling', 60000, 4),
    (402, 102, 'Imran Ahmed', '2021-05-20', 333444, 'imran.ahmed@email.com', 'Nail Art', 70000, 5),
    (403, 103, 'Saima Javed', '2022-03-10', 555666, 'saima.javed@email.com', 'Makeup Artist', 80000, 4),
    (404, 104,'Omar Farooq', '2021-08-12', 777888, 'omar.farooq@email.com', 'Barber', 75000, 5),
    (405, 105,'Farida Malik', '2022-02-28', 999000, 'farida.malik@email.com', 'Color Specialist', 90000, 4),
    (406, 106,'Salman Haider', '2021-11-05', 123234, 'salman.haider@email.com', 'Esthetician', 65000, 5),
    (407, 107,'Sadia Riaz', '2022-04-17', 345456, 'sadia.riaz@email.com', 'Fashion Consultant', 80000, 4),
    (408, 108,'Bilal Ahmed', '2021-07-03', 567678, 'bilal.ahmed@email.com', 'Spa Therapist', 100000, 5),
    (409, 109,'Zainab Ali', '2022-01-01', 789890, 'zainab.ali@email.com', 'Manicurist', 85000, 4),
    (410, 110,'Nida Iqbal', '2021-09-22', 123345, 'nida.iqbal@email.com', 'Hair Extensions Specialist', 95000, 5),
    (411, 111,'Hassan Khan', '2022-05-08', 456567, 'hassan.khan@email.com', 'Wedding Stylist', 85000, 4),
    (412, 112,'Fariha Shah', '2021-12-12', 789789, 'fariha.shah@email.com', 'Nail Technician', 70000, 5),
    (413, 113,'Junaid Qureshi', '2022-03-28', 234567, 'junaid.qureshi@email.com', 'Eyebrow Specialist', 75000, 4),
    (414, 114, 'Naima Rafique', '2021-10-15', 456789, 'naima.rafique@email.com', 'Waxing Specialist', 80000, 5),
    (415, 115,'Asadullah Khan', '2022-06-05', 789012, 'asadullah.khan@email.com', 'Makeup Artist', 90000, 4),
    (501, 101, 'Sara Khan', '2022-08-18', 135246, 'sara.khan@email.com', 'Manager', 100000, 4),
    (502, 102, 'Ali Raza', '2022-07-25', 468135, 'ali.raza@email.com', 'Manager', 120000, 5),
    (503, 103, 'Nadia Ahmed', '2022-06-12', 791357, 'nadia.ahmed@email.com', 'Manager', 130000, 4),
    (504, 104, 'Saad Khan', '2022-05-30', 124689, 'saad.khan@email.com', 'Manager', 100000, 5),
    (505, 105,'Aisha Malik', '2022-04-15', 357912, 'aisha.malik@email.com', 'Manager', 90000, 4),
    (506, 106,'Bilal Ali', '2022-03-01', 680124, 'bilal.ali@email.com', 'Manager', 80000, 5),
    (507, 107, 'Naima Shah', '2022-02-18', 913457, 'naima.shah@email.com', 'Manager', 110000, 4),
    (508, 108, 'Zubair Ahmed', '2022-01-05', 246890, 'zubair.ahmed@email.com', 'Manager', 95000, 5),
    (509, 109,'Hina Khan', '2021-12-22', 579123, 'hina.khan@email.com', 'Manager', 100000, 4),
    (510, 110,'Kashif Riaz', '2021-11-08', 802456, 'kashif.riaz@email.com', 'Manager', 130000, 5),
    (511, 111,'Samina Ali', '2021-10-25', 135789, 'samina.ali@email.com', 'Manager', 125000, 4),
    (512, 112,'Tariq Malik', '2021-09-10', 468012, 'tariq.malik@email.com', 'Manager', 110000, 5),
    (513, 113,'Fiza Shah', '2021-08-28', 791234, 'fiza.shah@email.com', 'Manager', 115000, 4),
    (514,114, 'Imran Qureshi', '2021-07-15', 124567, 'imran.qureshi@email.com', 'Manager', 110000, 5),
    (515, 115,'Sana Khan', '2021-06-01', 357890, 'sana.khan@email.com', 'Manager', 130000, 4);

Set identity_insert Employee Off
INSERT INTO Availability (SalonID, EmployeeID, Day, Date, Time)
VALUES
(101, 401, 'Monday', '2023-11-13', '10:00:00'),
(102, 402, 'Tuesday', '2023-11-14', '11:30:00'),
(103, 403, 'Wednesday', '2023-11-15', '09:00:00'),
(104, 404, 'Thursday', '2023-11-16', '14:00:00'),
(105, 405, 'Friday', '2023-11-17', '13:30:00'),
(106, 406, 'Saturday', '2023-11-18', '12:00:00'),
(107, 407, 'Sunday', '2023-11-19', '15:30:00'),
(108, 408, 'Monday', '2023-11-20', '16:45:00'),
(109, 409, 'Tuesday', '2023-11-21', '11:15:00'),
(110, 410, 'Wednesday', '2023-11-22', '10:30:00'),
(111, 411, 'Thursday', '2023-11-23', '14:45:00'),
(112, 412, 'Friday', '2023-11-24', '09:30:00'),
(113, 413, 'Saturday', '2023-11-25', '13:00:00'),
(114, 414, 'Sunday', '2023-11-26', '15:00:00');

SET IDENTITY_INSERT SalonRating ON
INSERT INTO SalonRating (RatingID,SalonID, Rating, Month, Year)
VALUES
(1,101, 4, 'January', 2023),
(2,102, 5, 'February', 2023),
(3,103, 4, 'March', 2023),
(4,104, 5, 'April', 2023),
(5,105, 4, 'May', 2023),
(6,106, 5, 'June', 2023),
(7,107, 4, 'July', 2023),
(8,108, 5, 'August', 2023),
(9,109, 4, 'September', 2023),
(10,110, 5, 'October', 2023),
(11,111, 4, 'November', 2023),
(12,112, 5, 'December', 2023),
(13,113, 4, 'January', 2024),
(14,114, 5, 'February', 2024),
(15,115, 4, 'March', 2024);

SET IDENTITY_INSERT SalonRating Off
SET IDENTITY_INSERT Product ON
INSERT INTO Product (ProductID, Product_Name, Price)
VALUES
    (1,'Shampoo', 1700),
    (2,'Conditioner', 1800),
    (3,'Hair Gel', 1500),
    (4,'Nail Polish', 500),
    (5,'Face Mask', 1500),
    (6,'Lipstick', 1200),
    (8,'Massage Oil', 2500),
    (9,'Body Lotion', 1800),
    (10,'Hair Dye', 2000),
    (11,'Sunscreen', 2200),
    (12,'Nail Art Kit', 4500),
    (13,'Perfume', 4000),
    (14,'Eyeshadow Palette', 5000),
    (15,'Eyebrow Pencil', 1000),
    (16,'Wax Strips', 500);

SET IDENTITY_INSERT Product Off
SET IDENTITY_INSERT Services On

INSERT INTO Services (ServicesID, Name, Description, Price, Duration, ProductID)
VALUES
    (1,'Haircut', 'Standard haircut for men and women', 500, 45, 1),
    (2,'Manicure', 'Basic manicure service', 300, 30, 4),
    (3,'Makeup', 'Professional makeup service', 800, 60, 6),
    (4,'Facial', 'Deep cleansing facial treatment', 600, 45, 5),
    (5,'Hair Color', 'Hair coloring service', 700, 60, 10),
    (6,'Massage', 'Full-body massage', 1000, 90, 8),
    (7,'Waxing', 'Body waxing service', 400, 30, 16),
    (8,'Nail Art', 'Creative nail art designs', 350, 45, 12),
    (9,'Spa Package', 'Full spa experience', 1200, 120, 9),
    (10,'Hair Extensions', 'Hair extensions service', 900, 75, 10),
    (11,'Bridal Makeup', 'Special makeup for weddings', 1200, 90, 13),
    (12,'Eyebrow Shaping', 'Eyebrow shaping service', 250, 30, 15),
    (13,'Waxing', 'Eyebrow and facial waxing', 350, 30, 16);


SET IDENTITY_INSERT Services Off

INSERT INTO Salon_Serv (ServicesID, SalonID)
VALUES
    (1, 101),
    (2, 102),
    (3, 103),
    (4, 104),
    (5, 105),
    (6, 106),
    (7, 107),
    (8, 108),
    (9, 109),
    (10, 110),
    (11, 111),
    (12, 112),
    (13, 113),
    (3, 114),
    (1, 115);