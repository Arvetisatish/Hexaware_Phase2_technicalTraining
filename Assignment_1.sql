CREATE DATABASE TechShop;
USE TechShop;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY ,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    Address TEXT
);


CREATE TABLE Products (
    ProductID INT PRIMARY KEY ,
    ProductName VARCHAR(100),
    Description TEXT,
    Price DECIMAL(10,2)
);



CREATE TABLE Orders (
    OrderID INT PRIMARY KEY ,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);





CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);





CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY ,
    ProductID INT,
    QuantityInStock INT,
    LastStockUpdate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);






INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES
(1, 'Satish', 'Reddy', 'satish@example.com', '9876543210', '123 MG Road, Hyderabad'),
(2, 'Lakshmi', 'Prasad', 'lakshmi@example.com', '9123456780', '456 Gandhi Nagar, Vijayawada'),
(3, 'Ravi', 'Teja', 'ravi@example.com', '9234567890', '789 RTC Colony, Visakhapatnam'),
(4, 'Anusha', 'Kumar', 'anusha@example.com', '9345678901', '321 KPHB, Hyderabad'),
(5, 'Ramesh', 'Naidu', 'ramesh@example.com', '9456789012', '654 Benz Circle, Guntur'),
(6, 'Sandeep', 'Goud', 'sandeep@example.com', '9567890123', '987 Prakash Nagar, Warangal'),
(7, 'Divya', 'Shetty', 'divya@example.com', '9678901234', '741 LB Nagar, Hyderabad'),
(8, 'Manoj', 'Chowdary', 'manoj@example.com', '9789012345', '852 RTC X Road, Karimnagar'),
(9, 'Pavani', 'Rao', 'pavani@example.com', '9890123456', '963 MG Road, Tirupati'),
(10, 'Venkatesh', 'Yadav', 'venkatesh@example.com', '9901234567', '147 Arundelpet, Ongole');






INSERT INTO Products (ProductID, ProductName, Description, Price) VALUES
(1, 'Laptop', 'Gaming laptop with 16GB RAM', 1200.00),
(2, 'Smartphone', 'Latest model with OLED display', 800.00),
(3, 'Headphones', 'Noise-canceling wireless headphones', 200.00),
(4, 'Smartwatch', 'Water-resistant with heart rate monitor', 150.00),
(5, 'Tablet', '10-inch screen with 128GB storage', 500.00),
(6, 'Wireless Mouse', 'Ergonomic design with long battery life', 50.00),
(7, 'Keyboard', 'Mechanical keyboard with RGB lights', 100.00),
(8, 'Monitor', '27-inch 4K display', 400.00),
(9, 'Printer', 'Wireless all-in-one printer', 250.00),
(10, 'Camera', 'DSLR with 24MP sensor', 700.00);




INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(1, 1, '2025-03-10', 2000.00),
(2, 2, '2025-03-11', 800.00),
(3, 3, '2025-03-12', 500.00),
(4, 4, '2025-03-13', 700.00),
(5, 5, '2025-03-14', 1500.00),
(6, 6, '2025-03-15', 300.00),
(7, 7, '2025-03-16', 450.00),
(8, 8, '2025-03-17', 600.00),
(9, 9, '2025-03-18', 900.00),
(10, 10, '2025-03-19', 1100.00);





INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES
(1, 1, 1, 1),
(2, 2, 2, 1),
(3, 3, 3, 2),
(4, 4, 4, 1),
(5, 5, 5, 3),
(6, 6, 6, 1),
(7, 7, 7, 2),
(8, 8, 8, 1),
(9, 9, 9, 2),
(10, 10, 10, 1);







INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate) VALUES
(1, 1, 50, '2025-03-01'),
(2, 2, 30, '2025-03-02'),
(3, 3, 100, '2025-03-03'),
(4, 4, 20, '2025-03-04'),
(5, 5, 40, '2025-03-05'),
(6, 6, 60, '2025-03-06'),
(7, 7, 25, '2025-03-07'),
(8, 8, 15, '2025-03-08'),
(9, 9, 35, '2025-03-09'),
(10, 10, 10, '2025-03-10');






SELECT FirstName, LastName, Email FROM Customers;

SELECT Orders.OrderID, Orders.OrderDate, Customers.FirstName, Customers.LastName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;



INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) 
VALUES (11, 'Krishna', 'Rao', 'krishna@example.com', '9012345678', '678 Gandhi Road, Hyderabad');




UPDATE Products SET Price = Price * 1.10;

DELETE FROM OrderDetails WHERE OrderID = 5;
DELETE FROM Orders WHERE OrderID = 5;


INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) 
VALUES (11, 3, '2025-03-21', 750.00);


UPDATE Customers 
SET Email = 'newemail@example.com', Address = 'New Address, Vijayawada' 
WHERE CustomerID = 2;



UPDATE Orders O 
SET TotalAmount = (SELECT SUM(OD.Quantity * P.Price) 
                   FROM OrderDetails OD 
                   JOIN Products P ON OD.ProductID = P.ProductID 
                   WHERE OD.OrderID = O.OrderID);

DELETE FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID = 3);
DELETE FROM Orders WHERE CustomerID = 3;



INSERT INTO Products (ProductID, ProductName, Description, Price) 
VALUES (11, 'Gaming Console', 'Latest console with 4K support', 500.00);




UPDATE Orders 
SET TotalAmount = TotalAmount + 0 
WHERE OrderID = 2;


UPDATE Customers C
SET OrdersCount = (SELECT COUNT(*) FROM Orders O WHERE O.CustomerID = C.CustomerID);


ALTER TABLE Customers ADD OrdersCount INT DEFAULT 0;


UPDATE Customers 
SET OrdersCount = (SELECT COUNT(*) FROM Orders WHERE Orders.CustomerID = Customers.CustomerID);


UPDATE Orders
SET TotalAmount = (
    SELECT SUM(OD.Quantity * P.Price)
    FROM OrderDetails OD
    JOIN Products P ON OD.ProductID = P.ProductID
    WHERE OD.OrderID = Orders.OrderID
);



create database StudentRecords;
use StudentRecords;

use TechShop;

