CREATE DATABASE TechShop;
USE TechShop;


-- Customers Table
CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    Phone NVARCHAR(15) UNIQUE NOT NULL,
    Address NVARCHAR(255) NOT NULL
);

-- Products Table
CREATE TABLE Products (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    Description NVARCHAR(255),
    Price DECIMAL(10,2) NOT NULL
);

-- Orders Table
CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10,2) NOT NULL,
    CONSTRAINT FK_Orders_Customers FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- OrderDetails Table
CREATE TABLE OrderDetails (
    OrderDetailID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    CONSTRAINT FK_OrderDetails_Orders FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    CONSTRAINT FK_OrderDetails_Products FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Inventory Table
CREATE TABLE Inventory (
    InventoryID INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT NOT NULL,
    QuantityInStock INT NOT NULL,
    LastStockUpdate DATETIME DEFAULT GETDATE(),
    CONSTRAINT FK_Inventory_Products FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);




INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES
('Amit', 'Sharma', 'amit.sharma@gmail.com', '9876543210', 'Bangalore, Karnataka'),
('Priya', 'Verma', 'priya.verma@yahoo.com', '9876543211', 'New Delhi'),
('Rajesh', 'Patil', 'rajesh.patil@outlook.com', '9876543212', 'Pune, Maharashtra'),
('Sneha', 'Reddy', 'sneha.reddy@gmail.com', '9876543213', 'Hyderabad, Telangana'),
('Vikram', 'Singh', 'vikram.singh@rediffmail.com', '9876543214', 'Kolkata, West Bengal'),
('Anjali', 'Mehta', 'anjali.mehta@gmail.com', '9876543215', 'Chennai, Tamil Nadu'),
('Arun', 'Nair', 'arun.nair@hotmail.com', '9876543216', 'Kochi, Kerala'),
('Pooja', 'Yadav', 'pooja.yadav@rediffmail.com', '9876543217', 'Jaipur, Rajasthan'),
('Manoj', 'Mishra', 'manoj.mishra@yahoo.com', '9876543218', 'Lucknow, Uttar Pradesh'),
('Kiran', 'Rao', 'kiran.rao@gmail.com', '9876543219', 'Hyderabad, Telangana');



INSERT INTO Products (ProductName, Description, Price) VALUES
('Samsung Galaxy S23', '5G smartphone with AMOLED display', 74999),
('Apple MacBook Air', 'M2 chip with Retina display', 124999),
('iPad Pro', '12.9-inch Retina Display with Apple Pencil support', 99999),
('OnePlus Nord Watch', 'Fitness tracker with AMOLED display', 7999),
('Sony WF-1000XM4', 'Noise-canceling wireless earbuds', 16999),
('PlayStation 5', 'Gaming console with DualSense controller', 59999),
('JBL Flip 6', 'Bluetooth speaker with deep bass', 10999),
('Dell Ultrasharp 27', '4K UHD monitor with IPS panel', 34999),
('Logitech G Pro', 'RGB mechanical gaming keyboard', 12999),
('WD My Passport 1TB', 'External HDD with password protection', 4999);



INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES
(1, '2025-03-01', 74999),
(2, '2025-03-02', 124999),
(3, '2025-03-03', 99999),
(4, '2025-03-04', 7999),
(5, '2025-03-05', 16999),
(6, '2025-03-06', 59999),
(7, '2025-03-07', 10999),
(8, '2025-03-08', 34999),
(9, '2025-03-09', 12999),
(10, '2025-03-10', 4999);




INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 2),
(5, 5, 1),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1),
(9, 9, 2),
(10, 10, 1);




INSERT INTO Inventory (ProductID, QuantityInStock) VALUES
(1, 50),
(2, 40),
(3, 35),
(4, 30),
(5, 25),
(6, 20),
(7, 45),
(8, 55),
(9, 60),
(10, 70);


SELECT FirstName, LastName, Email FROM Customers;



SELECT O.OrderID, O.OrderDate, C.FirstName, C.LastName 
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;



INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) 
VALUES ('Rahul', 'Kapoor', 'rahul.kapoor@example.com', '9876543220', 'Mumbai, Maharashtra');



UPDATE Products 
SET Price = Price * 1.10;




DECLARE @OrderID INT = 5;

DELETE FROM OrderDetails WHERE OrderID = @OrderID;
DELETE FROM Orders WHERE OrderID = @OrderID;




INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) 
VALUES (3, GETDATE(), 15999); 



DECLARE @CustomerID INT = 2; -- Replace with actual CustomerID
DECLARE @NewEmail NVARCHAR(100) = 'updated.email@example.com';
DECLARE @NewAddress NVARCHAR(255) = 'Updated Address, City';

UPDATE Customers 
SET Email = @NewEmail, Address = @NewAddress 
WHERE CustomerID = @CustomerID;



UPDATE Orders
SET TotalAmount = COALESCE((
    SELECT SUM(OD.Quantity * P.Price)
    FROM OrderDetails OD
    JOIN Products P ON OD.ProductID = P.ProductID
    WHERE OD.OrderID = Orders.OrderID
), 0);


DECLARE @CustomerID INT = 4; -- Replace with actual CustomerID

DELETE FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID = @CustomerID);
DELETE FROM Orders WHERE CustomerID = @CustomerID;



INSERT INTO Products (ProductName, Description, Price) 
VALUES ('Google Pixel 8', 'AI-powered smartphone with great camera', 79999);



DECLARE @OrderID INT = 6; -- Replace with actual OrderID
DECLARE @NewStatus NVARCHAR(20) = 'Shipped';

UPDATE Orders 
SET Status = @NewStatus 
WHERE OrderID = @OrderID;

ALTER TABLE Customers 
ADD OrdersPlaced INT DEFAULT 0;




UPDATE Customers
SET OrdersPlaced = (
    SELECT COUNT(*)
    FROM Orders
    WHERE Orders.CustomerID = Customers.CustomerID
);


--task3


SELECT O.OrderID, C.FirstName + ' ' + C.LastName AS CustomerName, O.OrderDate, O.TotalAmount
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;



SELECT P.ProductName, SUM(OD.Quantity * P.Price) AS TotalRevenue
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName;



SELECT DISTINCT C.CustomerID, C.FirstName, C.LastName, C.Email, C.Phone
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID;


SELECT TOP 1 P.ProductName, SUM(OD.Quantity) AS TotalQuantityOrdered
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TotalQuantityOrdered DESC;


ALTER TABLE Products ADD Category NVARCHAR(100);

SELECT ProductName, Category
FROM Products;



SELECT C.FirstName + ' ' + C.LastName AS CustomerName, AVG(O.TotalAmount) AS AvgOrderValue
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName;



SELECT TOP 1 O.OrderID, C.FirstName + ' ' + C.LastName AS CustomerName, O.TotalAmount
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID
ORDER BY O.TotalAmount DESC;



SELECT P.ProductName, COUNT(OD.OrderID) AS TimesOrdered
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName;



DECLARE @ProductName NVARCHAR(100);
SET @ProductName = 'Samsung Galaxy S23'; -- Change this as needed

SELECT DISTINCT C.CustomerID, C.FirstName, C.LastName, C.Email, C.Phone
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
WHERE P.ProductName = @ProductName;





DECLARE @StartDate DATE, @EndDate DATE;
SET @StartDate = '2025-03-01'; -- Change this as needed
SET @EndDate = '2025-03-10'; -- Change this as needed

SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders
WHERE OrderDate BETWEEN @StartDate AND @EndDate;




--task 4

SELECT c.CustomerID, c.FirstName, c.LastName, c.Email, c.Phone
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;



SELECT COUNT(*) AS TotalProducts FROM Products;



SELECT SUM(TotalAmount) AS TotalRevenue FROM Orders;



SELECT AVG(od.Quantity) AS AvgQuantityOrdered
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Category = 'CategoryName';



SELECT c.CustomerID, c.FirstName, c.LastName, SUM(o.TotalAmount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE c.CustomerID = 2
GROUP BY c.CustomerID, c.FirstName, c.LastName;



SELECT c.CustomerID, c.FirstName, c.LastName, COUNT(o.OrderID) AS OrderCount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY OrderCount DESC;



SELECT p.Category, SUM(od.Quantity) AS TotalQuantityOrdered
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY TotalQuantityOrdered DESC;




SELECT TOP 1 c.CustomerID, c.FirstName, c.LastName, SUM(o.TotalAmount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY TotalSpent DESC;



SELECT AVG(TotalAmount) AS AvgOrderValue FROM Orders;




