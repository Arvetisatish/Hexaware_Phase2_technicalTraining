--Create Database--
CREATE DATABASE StudentInformationSystemDB;

--Use Database--
USE StudentInformationSystemDB;


--Table Creations--

--Student table

CREATE TABLE Students (
    student_id INT PRIMARY KEY IDENTITY(1,1),
    first_name NVARCHAR(50),
    last_name NVARCHAR(50),
    date_of_birth DATE,
    email NVARCHAR(100),
    phone_number NVARCHAR(20)
);

--Teachers table

CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY IDENTITY(1,1),
    first_name NVARCHAR(50),
    last_name NVARCHAR(50),
    email NVARCHAR(100)
);



--Course table

CREATE TABLE Courses (
    course_id INT PRIMARY KEY IDENTITY(1,1),
    course_name NVARCHAR(100),
    credits INT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);



--Enrollments table

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);



--payments table

CREATE TABLE Payments (
    payment_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);


--inserting sample data--

--Students data--

INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
VALUES 
('Rahul', 'Sharma', '2000-08-15', 'rahul.sharma@gmail.com', '9876543210'),
('Priya', 'Mehta', '2001-07-12', 'priya.mehta@yahoo.com', '8765432109'),
('Amit', 'Verma', '2002-01-21', 'amit.verma@outlook.com', '7654321098'),
('Sneha', 'Reddy', '2003-11-11', 'sneha.reddy@gmail.com', '9543210987'),
('Karan', 'Patel', '2000-05-09', 'karan.patel@gmail.com', '9988776655'),
('Neha', 'Singh', '2001-03-28', 'neha.singh@gmail.com', '9123456780'),
('Ravi', 'Kumar', '2002-09-14', 'ravi.kumar@gmail.com', '8899776655'),
('Pooja', 'Nair', '2003-12-19', 'pooja.nair@gmail.com', '9345678901'),
('Anil', 'Yadav', '2001-06-06', 'anil.yadav@gmail.com', '9001234567'),
('Divya', 'Joshi', '2000-02-23', 'divya.joshi@gmail.com', '8888888888');


--Teachers data

INSERT INTO Teachers (first_name, last_name, email)
VALUES 
('Anita', 'Deshmukh', 'anita.deshmukh@college.edu.in'),
('Rajeev', 'Nair', 'rajeev.nair@college.edu.in'),
('Sonal', 'Kapoor', 'sonal.kapoor@college.edu.in'),
('Arjun', 'Iyer', 'arjun.iyer@college.edu.in'),
('Meena', 'Rao', 'meena.rao@college.edu.in'),
('Sunil', 'Mishra', 'sunil.mishra@college.edu.in'),
('Swati', 'Shah', 'swati.shah@college.edu.in'),
('Nitin', 'Chowdhury', 'nitin.chowdhury@college.edu.in'),
('Rekha', 'Saxena', 'rekha.saxena@college.edu.in'),
('Vikram', 'Sen', 'vikram.sen@college.edu.in');


--course data

INSERT INTO Courses (course_name, credits, teacher_id)
VALUES 
('Introduction to Programming', 4, 1),
('Mathematics 101', 3, 2),
('Computer Science 101', 4, 3),
('English Literature', 3, 4),
('Physics Fundamentals', 4, 5),
('Chemistry Basics', 4, 6),
('Indian History', 3, 7),
('Environmental Studies', 2, 8),
('Web Technologies', 4, 9),
('Database Management Systems', 4, 10);



--enrollement data

INSERT INTO Enrollments (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2024-01-10'),
(2, 2, '2024-01-11'),
(3, 3, '2024-01-12'),
(4, 4, '2024-01-13'),
(5, 5, '2024-01-14'),
(6, 6, '2024-01-15'),
(7, 7, '2024-01-16'),
(8, 8, '2024-01-17'),
(9, 9, '2024-01-18'),
(10, 10, '2024-01-19');


--payment data

INSERT INTO Payments (student_id, amount, payment_date)
VALUES 
(1, 5000.00, '2024-02-01'),
(2, 4500.00, '2024-02-02'),
(3, 6000.00, '2024-02-03'),
(4, 3000.00, '2024-02-04'),
(5, 4000.00, '2024-02-05'),
(6, 7000.00, '2024-02-06'),
(7, 3500.00, '2024-02-07'),
(8, 2000.00, '2024-02-08'),
(9, 5500.00, '2024-02-09'),
(10, 6500.00, '2024-02-10');

-- ✅ TASK 2: Basic SQL Operations

-- 1. Insert a new student (John Doe)
INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
VALUES ('John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890');

-- 2. Enroll an existing student in a course
INSERT INTO Enrollments (student_id, course_id, enrollment_date)
VALUES (1, 1, '2025-04-09');

-- 3. Update the email address of a specific teacher
UPDATE Teachers
SET email = 'anita.deshmukh@updatedcollege.edu.in'
WHERE teacher_id = 1;

-- 4. Delete a specific enrollment record
DELETE FROM Enrollments
WHERE student_id = 1 AND course_id = 1;

-- 5. Assign a specific teacher to a course
UPDATE Courses
SET teacher_id = 2
WHERE course_id = 1;

-- 6. Delete a student and remove their enrollments and payments
DELETE FROM Enrollments
WHERE student_id = 3;

DELETE FROM Payments
WHERE student_id = 3;

DELETE FROM Students
WHERE student_id = 3;

-- 7. Update the payment amount for a specific payment record
UPDATE Payments
SET amount = 7000.00
WHERE payment_id = 1;


-- ✅ TASK 3: Joins, Aggregates, Group By, Having, etc.

-- 1. Calculate total payments made by a specific student
SELECT s.first_name, s.last_name, SUM(p.amount) AS total_payment
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
WHERE s.student_id = 1
GROUP BY s.first_name, s.last_name;

-- 2. List courses with the number of students enrolled in each
SELECT c.course_name, COUNT(e.student_id) AS enrolled_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- 3. Find names of students not enrolled in any course
SELECT s.first_name, s.last_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

-- 4. Retrieve student names and the courses they are enrolled in
SELECT s.first_name, s.last_name, c.course_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

-- 5. List teacher names and the courses they are assigned to
SELECT t.first_name, t.last_name, c.course_name
FROM Teachers t
JOIN Courses c ON t.teacher_id = c.teacher_id;

-- 6. List students and their enrollment dates for a specific course (e.g., course_id = 2)
SELECT s.first_name, s.last_name, e.enrollment_date
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 2;

-- 7. Find students who have not made any payments
SELECT s.first_name, s.last_name
FROM Students s
LEFT JOIN Payments p ON s.student_id = p.student_id
WHERE p.payment_id IS NULL;

-- 8. Identify courses that have no enrollments
SELECT c.course_name
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;

-- 9. List students enrolled in more than one course
SELECT s.first_name, s.last_name, COUNT(e.course_id) AS course_count
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
GROUP BY s.first_name, s.last_name
HAVING COUNT(e.course_id) > 0;

-- 10. Find teachers not assigned to any courses
SELECT t.first_name, t.last_name
FROM Teachers t
LEFT JOIN Courses c ON t.teacher_id = c.teacher_id
WHERE c.course_id IS NULL;


-- ✅ TASK 4: Subqueries

-- 1. Calculate the average number of students per course
SELECT AVG(student_count) AS avg_enrollments
FROM (
    SELECT COUNT(*) AS student_count
    FROM Enrollments
    GROUP BY course_id
) AS sub;

-- 2. Find the student(s) who made the highest payment
SELECT s.first_name, s.last_name, p.amount
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
WHERE p.amount = (
    SELECT MAX(amount) FROM Payments
);

-- 3. List courses with the highest number of enrollments
SELECT c.course_name, COUNT(e.enrollment_id) AS total_enrollments
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
HAVING COUNT(e.enrollment_id) = (
    SELECT MAX(enrollment_count)
    FROM (
        SELECT COUNT(*) AS enrollment_count
        FROM Enrollments
        GROUP BY course_id
    ) AS sub
);

-- 4. Total payments received for courses taught by each teacher
SELECT t.first_name, t.last_name, SUM(p.amount) AS total_payment
FROM Teachers t
JOIN Courses c ON t.teacher_id = c.teacher_id
JOIN Enrollments e ON c.course_id = e.course_id
JOIN Payments p ON e.student_id = p.student_id
GROUP BY t.first_name, t.last_name;

-- 5. Students enrolled in all available courses
SELECT s.student_id, s.first_name, s.last_name
FROM Students s
WHERE NOT EXISTS (
    SELECT course_id
    FROM Courses
    EXCEPT
    SELECT course_id
    FROM Enrollments e
    WHERE e.student_id = s.student_id
);

-- 6. Teachers not assigned to any courses
SELECT first_name, last_name
FROM Teachers
WHERE teacher_id NOT IN (
    SELECT DISTINCT teacher_id FROM Courses WHERE teacher_id IS NOT NULL
);

-- 7. Calculate the average age of all students
SELECT AVG(DATEDIFF(YEAR, date_of_birth, GETDATE())) AS average_age
FROM Students;

-- 8. Identify courses with no enrollments (using subquery)
SELECT course_name
FROM Courses
WHERE course_id NOT IN (
    SELECT DISTINCT course_id FROM Enrollments
);

-- 9. Total payments made by each student for each course
SELECT s.first_name, s.last_name, c.course_name, SUM(p.amount) AS total_payment
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
GROUP BY s.first_name, s.last_name, c.course_name;

-- 10. Students who made more than two payments
SELECT s.first_name, s.last_name, COUNT(p.payment_id) AS payment_count
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
GROUP BY s.first_name, s.last_name
HAVING COUNT(p.payment_id) > 2;

-- 11. Total payments made by each student
SELECT s.first_name, s.last_name, SUM(p.amount) AS total_payment
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
GROUP BY s.first_name, s.last_name;

-- 12. Count of students enrolled in each course
SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- 13. Average payment amount made by students
SELECT AVG(p.amount) AS avg_payment
FROM Students s
JOIN Payments p ON s.student_id = p.student_id;
