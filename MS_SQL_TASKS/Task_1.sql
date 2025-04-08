create database StudentRecords;
use StudentRecords;


EXEC sp_renameDB 'StudentRecords', 'UniversityRecords';


CREATE TABLE Students (
    StudentID INT PRIMARY KEY, 
    FirstName VARCHAR(50) NOT NULL,  
    LastName VARCHAR(50) NOT NULL,  
    Email VARCHAR(100) UNIQUE NOT NULL,  
    Phone VARCHAR(15) UNIQUE,  
    DateOfBirth DATE,  
    Gender CHAR(1) CHECK (Gender IN ('M', 'F')), 
    Address TEXT,  
    EnrollmentDate DATE DEFAULT GETDATE(),  
    Department VARCHAR(100),
    CGPA DECIMAL(3,2) CHECK (CGPA BETWEEN 0 AND 10) 
);

ALTER TABLE Students DROP CONSTRAINT UQ__Students__A9D105340956F797;

ALTER TABLE Students  
DROP COLUMN Email;


EXEC SP_RENAME 'Students' , 'UniversityStudents';
SELECT * from UniversityStudents;

ALTER TABLE UniversityStudents  
ADD Email VARCHAR(50);  

INSERT INTO UniversityStudents(StudentID, FirstName, LastName, Phone, DateOfBirth, Gender, Address, EnrollmentDate, Department, CGPA)  
VALUES  
(1, 'Rohan', 'Sharma', '9123456789', '2002-02-15', 'M', '101 MG Road, Hyderabad', '2023-06-15', 'Computer Science', 8.3),  
(2, 'Pooja', 'Reddy', '9234567891', '2001-08-22', 'F', '202 Gandhi Nagar, Vijayawada', '2022-07-10', 'Electrical', 9.0),  
(3, 'Vikram', 'Kumar', '9345678902', '2000-11-10', 'M', '303 RTC Colony, Visakhapatnam', '2021-08-01', 'Mechanical', 7.5),  
(4, 'Sita', 'Verma', '9456789013', '2003-04-05', 'F', '404 LB Nagar, Hyderabad', '2023-09-05', 'Electronics', 8.7),  
(5, 'Arjun', 'Naidu', '9567890124', '2002-06-30', 'M', '505 Benz Circle, Guntur', '2023-07-20', 'Civil', 7.9);

UPDATE UniversityStudents SET Email = 'rohan.sharma@example.com' WHERE StudentID = 2;
UPDATE UniversityStudents SET Email = 'pooja.reddy@example.com' WHERE StudentID = 3;
UPDATE UniversityStudents SET Email = 'vikram.kumar@example.com' WHERE StudentID = 4;
UPDATE UniversityStudents SET Email = 'sita.verma@example.com' WHERE StudentID = 5;
UPDATE UniversityStudents SET Email  = 'ram@gmail.com' WHERE StudentId=1;


UPDATE UniversityStudents SET Email='satish@gmail.com' WHERE StudentID = 1;

DELETE UniversityStudents WHERE EnrollmentDate ='2021-08-01';

Select FirstName , LastName , Email from UniversityStudents 

SELECT * from UniversityStudents where DateOfBirth <'2003-12-01';

Select * from UniversityStudents;
SELECT * from UniversityStudents where Department= 'Computer Science';

SELECT * from UniversityStudents WHERE CGPA <8.00;