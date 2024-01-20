select * from Receipt
select * from Account

select * from Manager
select * from Product
select * from Service_Product
select * from Orders
select * from Suppliers

select * from Inventory


select * from Salon_Serv
select * from Employee
select * from Manager
select * from customer
select * from Availability
select * from Appointment
select * from Receipt
select * from Services


set identity_insert Salons ON
INSERT INTO Salons (SalonID, Name, PlotNo, StreetNo, AreaCode, City, PostalCode)
VALUES 
	(116, 'Karachi Glam', 1726, 79, 67890, 'Karachi', 74800),
    (117, 'Lahore Luxe', 1840, 14, 78901, 'Lahore', 54600),
    (118, 'Islamabad Elegance', 1954, 47, 89012, 'Islamabad', 44200),
    (119, 'Rawalpindi Radiance', 2068, 92, 90123, 'Rawalpindi', 46400),
    (120, 'Faisalabad Finesse', 2182, 37, 12347, 'Faisalabad', 38900),
    (121, 'Peshawar Pizzazz', 2296, 70, 12345, 'Peshawar', 25200),
    (122, 'Quetta Queendom', 2410, 25, 23456, 'Quetta', 87400),
    (123, 'Multan Marvel', 2524, 58, 34567, 'Multan', 61100),
    (124, 'Sialkot Style', 2638, 11, 45678, 'Sialkot', 51312),
    (125, 'Gujranwala Glamour', 2752, 44, 56789, 'Gujranwala', 54650),
    -- Additional salons for each city
    (126, 'Karachi Chic', 2866, 77, 67890, 'Karachi', 74900),
    (127, 'Lahore Luster', 2980, 12, 78901, 'Lahore', 54700),
    (128, 'Islamabad Impeccable', 3094, 45, 89012, 'Islamabad', 44300),
    (129, 'Rawalpindi Refinement', 3208, 90, 90123, 'Rawalpindi', 46500),
    (130, 'Faisalabad Fad', 3322, 35, 12347, 'Faisalabad', 39000),
    (131, 'Peshawar Panache', 3436, 68, 12345, 'Peshawar', 25300),
    (132, 'Quetta Quirk', 3550, 23, 23456, 'Quetta', 87500)

Set identity_insert Salons Off



-- Enable identity insert for Employee table
SET IDENTITY_INSERT Employee ON;

-- Additional non-manager employees for each added salon
INSERT INTO Employee (EmployeeID, SalonID, Name, Joining_Date, Contact_number, Email, Specialty, Salary, Rating)
VALUES
    -- Continue adding more employees for SalonID 116-130
    -- Continue adding more employees for SalonID 116-130

    --(415, 116, 'Zohaib Ahmed', '2025-03-01', 111222, 'zohaib.ahmed@email.com', 'Hair Styling', 60000, 4),
    (416, 116, 'Aisha Akram', '2025-04-15', 133444, 'aisha.akram1@email.com', 'Nail Art', 70000, 5),
    (417, 116, 'Sadia Khan', '2025-05-30', 255666, 'sadia.khan2@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 116 as needed

    (418, 117, 'Rizwan Malik', '2025-06-15', 377888, 'rizwan.malik3@email.com', 'Barber', 75000, 5),
    (419, 117, 'Nida Hassan', '2025-07-01', 499000, 'nida.hassan4@email.com', 'Color Specialist', 90000, 4),
    (420, 117, 'Faisal Ahmed', '2025-08-18', 523234, 'faisal.ahmed5@email.com', 'Esthetician', 65000, 5),
    -- Add more employees for SalonID 117 as needed

    -- Continue this pattern for SalonID 118-130
    (421, 118, 'Shahid Ahmed', '2025-09-15', 689012, 'shahid.ahmed6@email.com', 'Hair Styling', 60000, 4),
    (422, 118, 'Fariha Khan', '2025-10-30', 711223, 'fariha.khan7@email.com', 'Nail Art', 70000, 5),
    (423, 118, 'Asad Riaz', '2025-11-15', 834445, 'asad.riaz8@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 118 as needed

    (424, 119, 'Sana Ali', '2026-01-01', 989012, 'sana.ali9@email.com', 'Hair Styling', 60000, 4),
    (425, 119, 'Kashan Malik', '2026-02-15', 101223, 'kashan.malik10@email.com', 'Nail Art', 70000, 5),
    (426, 119, 'Naima Riaz', '2026-03-01', 114445, 'naima.riaz11@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 119 as needed

    (427, 120, 'Faisal Khan', '2026-04-15', 129012, 'faisal.khan12@email.com', 'Hair Styling', 60000, 2),
    (428, 120, 'Sadia Ahmed', '2026-05-30', 131223, 'sadia.ahmed13@email.com', 'Nail Art', 70000, 5),
    (429, 120, 'Ali Riaz', '2026-06-15', 144445, 'ali.riaz14@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 120 as needed

    -- Continue this pattern for SalonID 121-130
    (430, 121, 'Hina Malik', '2026-07-01', 159012, 'hina.malik15@email.com', 'Hair Styling', 60000, 4),
    (431, 121, 'Imran Ali', '2026-08-15', 161223, 'imran.ali16@email.com', 'Nail Art', 70000, 5),
    (432, 121, 'Sana Riaz', '2026-09-30', 174445, 'sana.riaz17@email.com', 'Makeup Artist', 80000, 3),
    -- Add more employees for SalonID 121 as needed

    (433, 122, 'Kamran Ali', '2026-10-15', 189012, 'kamran.ali18@email.com', 'Hair Styling', 60000, 4),
    (434, 122, 'Nida Shah', '2026-11-30', 191223, 'nida.shah19@email.com', 'Nail Art', 70000, 5),
    (435, 122, 'Asad Malik', '2026-12-15', 204445, 'asad.malik20@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 122 as needed

    (436, 123, 'Sara Riaz', '2027-01-01', 219012, 'sara.riaz21@email.com', 'Hair Styling', 60000, 4),
    (437, 123, 'Imran Ahmed', '2027-02-15', 221223, 'imran.ahmed22@email.com', 'Nail Art', 70000, 3),
    (438, 123, 'Nadia Ali', '2027-03-01', 234445, 'nadia.ali23@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 123 as needed

    (439, 124, 'Saad Riaz', '2027-04-15', 249012, 'saad.riaz24@email.com', 'Hair Styling', 60000, 3),
    (440, 124, 'Saima Ahmed', '2027-05-30', 251223, 'saima.ahmed25@email.com', 'Nail Art', 70000, 5),
    (441, 124, 'Fahad Malik', '2027-06-15', 264445, 'fahad.malik26@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 124 as needed

    (442, 125, 'Zainab Ali', '2027-07-01', 279012, 'zainab.ali27@email.com', 'Hair Styling', 60000, 4),
    (443, 125, 'Hassan Riaz', '2027-08-15', 281223, 'hassan.riaz28@email.com', 'Nail Art', 70000, 5),
    (444, 125, 'Fariha Malik', '2027-09-30', 294445, 'fariha.malik29@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 125 as needed

    -- Continue this pattern for SalonID 126-130
    (445, 126, 'Farhan Ahmed', '2027-10-15', 309012, 'farhan.ahmed30@email.com', 'Hair Styling', 60000, 3),
    (446, 126, 'Nida Malik', '2027-11-30', 311223, 'nida.malik31@email.com', 'Nail Art', 70000, 4),
    (447, 126, 'Bilal Riaz', '2027-12-15', 324445, 'bilal.riaz32@email.com', 'Makeup Artist', 80000, 5),
    -- Add more employees for SalonID 126 as needed

    (448, 127, 'Ayesha Riaz', '2028-01-01', 339012, 'ayesha.riaz33@email.com', 'Hair Styling', 60000, 4),
    (449, 127, 'Farhan Malik', '2028-02-15', 341223, 'farhan.malik34@email.com', 'Nail Art', 70000, 5),
    (450, 127, 'Saba Khan', '2028-03-01', 354445, 'saba.khan35@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 127 as needed

    (451, 128, 'Imran Ahmed', '2028-04-15', 369012, 'imran.ahmed36@email.com', 'Hair Styling', 60000, 4),
    (452, 128, 'Nadia Ali', '2028-05-30', 371223, 'nadia.ali37@email.com', 'Nail Art', 70000, 5),
    (453, 128, 'Sara Riaz', '2028-06-15', 384445, 'sara.riaz38@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 128 as needed

    (454, 129, 'Nida Ali', '2028-07-01', 399012, 'nida.ali39@email.com', 'Hair Styling', 60000, 3),
    (455, 129, 'Hassan Riaz', '2028-08-15', 401223, 'hassan.riaz40@email.com', 'Nail Art', 70000, 5),
    (456, 129, 'Fariha Khan', '2028-09-30', 414445, 'fariha.khan41@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 129 as needed

    (457, 130, 'Zainab Ali', '2028-10-15', 429012, 'zainab.ali42@email.com', 'Hair Styling', 60000, 4),
    (458, 130, 'Hassan Riaz', '2028-11-30', 431223, 'hassan.riaz43@email.com', 'Nail Art', 70000, 5),
    (459, 130, 'Fariha Malik', '2028-12-15', 444445, 'fariha.malik44@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 130 as needed

    -- Continue this pattern for the remaining salons
    (460, 131, 'Amir Ali', '2027-04-01', 459012, 'amir.ali45@email.com', 'Hair Styling', 60000, 4),
    (461, 131, 'Sana Gul', '2027-05-15', 461223, 'sana.gul46@email.com', 'Nail Art', 70000, 5),
    (462, 131, 'Kamran Shah', '2027-06-30', 474445, 'kamran.shah47@email.com', 'Makeup Artist', 80000, 4),
    -- Add more employees for SalonID 131 as needed

    (463, 132, 'Nida Riaz', '2029-01-01', 489012, 'nida.riaz48@email.com', 'Hair Styling', 60000, 4),
    (464, 132, 'Farhan Ahmed', '2029-02-15', 491223, 'farhan.ahmed49@email.com', 'Nail Art', 70000, 5),
    (465, 132, 'Ayesha Khan', '2029-03-01', 504445, 'ayesha.khan50@email.com', 'Makeup Artist', 80000, 4),

    (516, 116, 'Usman Ali', '2033-01-01', 123456, 'usman.ali51@email.com', 'Manager', 100000, 4),
    (517, 117, 'Sana Ahmed', '2033-01-02', 234567, 'sana.ahmed52@email.com', 'Manager', 128000, 3),
    (518, 118, 'Ahmed Khan', '2033-01-03', 345678, 'ahmed.khan54@email.com', 'Manager', 130000, 5),
    (519, 119, 'Saima Riaz', '2033-01-04', 450788, 'saima.riaz55@email.com', 'Manager', 120000, 4),
    (520, 120, 'Ali Zain', '2033-01-05', 567890, 'ali.zain56@email.com', 'Manager', 140000, 3),
    (521, 121, 'Ayesha Malik', '2033-01-06', 678901, 'ayesha.malik57@email.com', 'Manager', 150000, 4),
    (522, 122, 'Imran Ahmed', '2033-01-07', 789012, 'imran.ahmed58@email.com', 'Manager', 120000, 2),
    (523, 123, 'Nadia Ali', '2033-01-08', 890123, 'nadia.ali59@email.com', 'Manager', 110000, 5),
    (524, 124, 'Sara Riaz', '2033-01-09', 901234, 'sara.riaz60@email.com', 'Manager', 115000, 4),
    (525, 125, 'Fahad Malik', '2033-01-10', 123456, 'fahad.malik61@email.com', 'Manager', 156000, 4),
    (526, 126, 'Zainab Ali', '2033-01-11', 234567, 'zainab.ali62@email.com', 'Manager', 135000, 5),
    (527, 127, 'Hassan Riaz', '2033-01-12', 345678, 'hassan.riaz63@email.com', 'Manager', 125000, 1),
    (528, 128, 'Fariha Malik', '2033-01-13', 45389, 'fariha.malik64@email.com', 'Manager', 145000, 5),
    (529, 129, 'Farhan Ahmed', '2033-01-14', 567890, 'farhan.ahmed65@email.com', 'Manager', 150000, 5),
    (530, 130, 'Nida Malik', '2033-01-15', 678901, 'nida.malik66@email.com', 'Manager', 130000, 2),
    (531, 131, 'Ali Ahmed', '2032-01-01', 456789, 'ali.ahmed67@email.com', 'Manager', 120000, 4),
    (532, 132, 'Nadia Riaz', '2032-01-01', 456389, 'nadia.riaz68@email.com', 'Manager', 125000, 3);

-- Disable identity insert for Employee table
SET IDENTITY_INSERT Employee OFF;


-- Disable identity insert for Employee table
--SET IDENTITY_INSERT Employee OFF;

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



select * from Availability
select * from Employee
select * from Salons



delete from customer where customerID = 2;


delete from account where customerID = 224;
delete from customer where customerID = 224;
select * from Account
select * from Customer
select * from Receipt
