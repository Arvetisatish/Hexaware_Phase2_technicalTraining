create database EmployeeRecords;
use EmployeeRecords;

EXEC sp_renameDB EmployeeRecords , HR_Database;

drop database HR_Database;

ALTER DATABASE HR_DATABASE 
SET SINGLE_USER WITH ROLLBACK IMMEDIATE;

DROP DATABASE HR_DATABASE;

USE master;
GO

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,  
    FullName VARCHAR(100) NOT NULL, 
    Email VARCHAR(100) UNIQUE NOT NULL,  
    Phone VARCHAR(15) UNIQUE,  
    DateJoined DATE DEFAULT GETDATE() 
);

ALTER TABLE CUSTOMERS
ADD ADDRESS TEXT;

EXEC SP_RENAME CUSTOMERS , CLIENTDETAILS;


USE MASTER 
GO

DROP TABLE CLIENTDETAILS;
INSERT INTO Customers (CustomerID, FullName, Email, Phone, DateJoined)  
VALUES  
(1, 'Satish Babu', 'satish.babu@example.com', '9876543210', '2025-03-21'),
(2, 'Anusha Reddy', 'anusha.reddy@example.com', '9123456780', '2025-03-20'),
(3, 'Ravi Kumar', 'ravi.kumar@example.com', '9234567890', '2025-03-19'),
(4, 'Pooja Naidu', 'pooja.naidu@example.com', '9345678901', '2025-03-18'),
(5, 'Vikram Rao', 'vikram.rao@example.com', '9456789012', '2025-03-17'),
(6, 'Divya Shetty', 'divya.shetty@example.com', '9567890123', '2025-03-16'),
(7, 'Sandeep Goud', 'sandeep.goud@example.com', '9678901234', '2025-03-15'),
(8, 'Arjun Yadav', 'arjun.yadav@example.com', '9789012345', '2025-03-14'),
(9, 'Meghana Sharma', 'meghana.sharma@example.com', '9890123456', '2025-03-13'),
(10, 'Rajesh Verma', 'rajesh.verma@example.com', '9901234567', '2025-03-12');

UPDATE CUSTOMERS SET EMAIL='ARVETI@GAMIL.COM' WHERE CUSTOMERID=3;
DELETE CUSTOMERS WHERE CUSTOMERID =5;

UPDATE CUSTOMERS SET EMAIL ='HEEYYBRO@GAMIL.COM' WHERE CUSTOMERID =6;

SELECT FULLNAME , EMAIL FROM CUSTOMERS;

SELECT * FROM CUSTOMERS WHERE DATEJOINED = '2020-01-01';

SELECT * FROM CUSTOMERS 
WHERE FULLNAME LIKE 'A%';

SELECT * FROM CUSTOMERS 
WHERE PHONE =NULL;

SELECT * FROM CUSTOMERS
WHERE CUSTOMERID IN(1,3,7);

SELECT * FROM CUSTOMERS
WHERE DATEJOINED BETWEEN '2018-01-01' AND '2023-12-31';


SELECT 

 C.FullName AS Name, 
    C.Email AS ContactEmail, 
    C.Phone AS ContactNumber, 
    C.DateJoined AS JoinedDate

FROM CUSTOMERS C;


