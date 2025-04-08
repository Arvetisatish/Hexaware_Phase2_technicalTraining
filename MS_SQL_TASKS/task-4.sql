use TechShop;

--Find customers who have not placed any orders.
SELECT CustomerID, FirstName, LastName, Email 
FROM Customers 
WHERE CustomerID NOT IN (SELECT DISTINCT CustomerID FROM Orders);

-- Find the total number of products available for sale.
SELECT COUNT(*) AS TotalProducts FROM Products;

-- Calculate the total revenue generated by TechShop.
SELECT SUM(TotalAmount) AS TotalRevenue FROM Orders;

-- Calculate the average quantity ordered for products in a specific category.
SELECT AVG(OD.Quantity) AS AvgQuantityOrdered 
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
WHERE P.ProductName = 'Laptop';  

-- Calculate the total revenue generated by a specific customer.
SELECT C.CustomerID, C.FirstName, C.LastName, SUM(O.TotalAmount) AS TotalRevenue
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
WHERE C.CustomerID = 3  -- Change CustomerID as needed
GROUP BY C.CustomerID, C.FirstName, C.LastName;

-- Find the customers who have placed the most orders.
SELECT TOP 1 C.CustomerID, C.FirstName, C.LastName, COUNT(O.OrderID) AS TotalOrders
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName
ORDER BY TotalOrders DESC;

-- Find the most popular product category (highest total quantity ordered).
SELECT TOP 1 P.ProductName, SUM(OD.Quantity) AS TotalOrdered
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TotalOrdered DESC;

-- Find the customer who has spent the most money (highest total revenue).
SELECT TOP 1 C.CustomerID, C.FirstName, C.LastName, SUM(O.TotalAmount) AS TotalSpent
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName
ORDER BY TotalSpent DESC;

-- Calculate the average order value for all customers.
SELECT AVG(TotalAmount) AS AvgOrderValue FROM Orders;

-- Find the total number of orders placed by each customer.
SELECT C.CustomerID, C.FirstName, C.LastName, COUNT(O.OrderID) AS OrderCount
FROM Customers C
LEFT JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName;


