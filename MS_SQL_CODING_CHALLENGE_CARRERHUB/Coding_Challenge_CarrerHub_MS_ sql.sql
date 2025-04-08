-- Create CareerHub database
CREATE DATABASE CAREERHUB;

USE  CAREERHUB;

-- Create Companies table
CREATE TABLE Companies (
    CompanyID INT IDENTITY(1,1) PRIMARY KEY,
    CompanyName VARCHAR(255) NOT NULL,
    Location VARCHAR(255) NOT NULL
);



-- Create Jobs table
CREATE TABLE Jobs (
    JobID INT IDENTITY(1,1) PRIMARY KEY,
    CompanyID INT,
    JobTitle VARCHAR(255) NOT NULL,
    JobDescription TEXT,
    JobLocation VARCHAR(255),
    Salary DECIMAL(10,2),
    JobType VARCHAR(50),
    PostedDate DATETIME,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) 
);


-- Create Applicants table
CREATE TABLE Applicants (
    ApplicantID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Resume TEXT
);


-- Create Applications table
CREATE TABLE Applications (
    ApplicationID INT IDENTITY(1,1) PRIMARY KEY,
    JobID INT,
    ApplicantID INT,
    ApplicationDate DATETIME,
    CoverLetter TEXT,
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID) ,
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) 
);



-- Insert sample data into Companies table with Indian locations
INSERT INTO Companies (CompanyName, Location) VALUES
('TCS', 'Mumbai'),
('Infosys', 'Bangalore'),
('Wipro', 'Hyderabad');


-- Insert sample data into Jobs table with relevant Indian job details
INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES
(1, 'Software Engineer', 'Develop and maintain applications', 'Mumbai', 800000, 'Full-time', GETDATE()),
(2, 'Data Analyst', 'Analyze business data', 'Bangalore', 700000, 'Full-time', GETDATE()),
(3, 'Web Developer', 'Develop and manage web applications', 'Hyderabad', 600000, 'Contract', GETDATE());


-- Insert sample data into Applicants table with Indian names and details, including experience
INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume) VALUES
('Amit', 'Sharma', 'amit.sharma@example.com', '9876543210', '3 years experience in software development'),
('Priya', 'Rao', 'priya.rao@example.com', '9988776655', '5 years experience in data analysis'),
('Raj', 'Patel', 'raj.patel@example.com', '9876541230', '2 years experience in web development');


-- Insert sample data into Applications table
INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES
(1, 1, GETDATE(), 'I am excited to apply for this role at TCS.'),
(2, 2, GETDATE(), 'I have the skills required for this job at Infosys.'),
(3, 3, GETDATE(), 'I am passionate about web development and Wipro is a great fit.');


-- 5 Count the number of applications received for each job listing
SELECT j.JobTitle, COUNT(a.ApplicationID) AS ApplicationCount
FROM Jobs j
LEFT JOIN Applications a ON j.JobID = a.JobID
GROUP BY j.JobTitle;


--6  Get job listings where salary is between min and max
SELECT 
    JobTitle, 
    JobLocation, 
    Salary
FROM 
    Jobs
WHERE 
    Salary BETWEEN (SELECT MIN(Salary) FROM Jobs) AND (SELECT MAX(Salary) FROM Jobs);




-- 7 Retrieve job application history for a specific applicant
SELECT j.JobTitle, c.CompanyName, a.ApplicationDate
FROM Applications a
JOIN Jobs j ON a.JobID = j.JobID
JOIN Companies c ON j.CompanyID = c.CompanyID
WHERE a.ApplicantID = 1;



-- 8 Calculate the average salary of job listings, excluding zero salary
SELECT AVG(Salary) AS AverageSalary FROM Jobs WHERE Salary > 0;


-- 9 Identify the company with the most job listings
SELECT c.CompanyName, COUNT(j.JobID) AS JobCount
FROM Companies c
JOIN Jobs j ON c.CompanyID = j.CompanyID
GROUP BY c.CompanyName
ORDER BY JobCount DESC;



ALTER TABLE Applicants ADD Experience INT NOT NULL DEFAULT 0;

UPDATE Applicants SET Experience = 3 WHERE FirstName = 'Amit' AND LastName = 'Sharma';
UPDATE Applicants SET Experience = 5 WHERE FirstName = 'Priya' AND LastName = 'Rao';
UPDATE Applicants SET Experience = 2 WHERE FirstName = 'Raj' AND LastName = 'Patel';


UPDATE Jobs SET JobLocation = 'CityX' WHERE JobID = 1;

SELECT * FROM Applicants;

-- 10 Find applicants who applied to jobs in a specific city and have at least 3 years of experience
SELECT a.FirstName, a.LastName
FROM Applications app
JOIN Jobs j ON app.JobID = j.JobID
JOIN Applicants a ON app.ApplicantID = a.ApplicantID
WHERE j.JobLocation = 'CityX' AND a.Experience >= 3;

-- 11 Retrieve distinct job titles with salaries between $60,000 and $80,000
SELECT DISTINCT JobTitle FROM Jobs WHERE Salary BETWEEN 600000 AND 800000;

-- 12 Find jobs with no applications
SELECT j.JobTitle FROM Jobs j
LEFT JOIN Applications a ON j.JobID = a.JobID
WHERE a.ApplicationID IS NULL;

-- 13 Retrieve applicants and the companies and positions they applied for
SELECT a.FirstName, a.LastName, c.CompanyName, j.JobTitle
FROM Applications app
JOIN Applicants a ON app.ApplicantID = a.ApplicantID
JOIN Jobs j ON app.JobID = j.JobID
JOIN Companies c ON j.CompanyID = c.CompanyID;



-- 14 Retrieve companies with the count of jobs posted, even if they received no applications
SELECT c.CompanyName, COUNT(j.JobID) AS JobCount
FROM Companies c
LEFT JOIN Jobs j ON c.CompanyID = j.CompanyID
GROUP BY c.CompanyName;

-- 15 Retrieve applicants and the companies and positions they applied for, including those who have not applied
SELECT a.FirstName, a.LastName, c.CompanyName, j.JobTitle
FROM Applicants a
LEFT JOIN Applications app ON a.ApplicantID = app.ApplicantID
LEFT JOIN Jobs j ON app.JobID = j.JobID
LEFT JOIN Companies c ON j.CompanyID = c.CompanyID;

-- 16 Find companies that have posted jobs with a salary higher than the average salary of all jobs
SELECT DISTINCT c.CompanyName FROM Companies c
JOIN Jobs j ON c.CompanyID = j.CompanyID
WHERE j.Salary > (SELECT AVG(Salary) FROM Jobs);

-- 17 Display applicants with their names and a concatenated city-state string
SELECT FirstName, LastName, CONCAT(Email, ', ', Phone) AS ContactDetails FROM Applicants;

-- 18 Retrieve jobs with titles containing 'Developer' or 'Engineer'
SELECT * FROM Jobs WHERE JobTitle LIKE '%Developer%' OR JobTitle LIKE '%Engineer%';

--19  Retrieve all applicants and jobs they applied for, including unmatched applicants and jobs
SELECT a.FirstName, a.LastName, j.JobTitle FROM Applicants a
FULL OUTER JOIN Applications app ON a.ApplicantID = app.ApplicantID
FULL OUTER JOIN Jobs j ON app.JobID = j.JobID;


-- Insert a company in Chennai
INSERT INTO Companies (CompanyName, Location) VALUES ('HCL', 'Chennai');

-- Insert an applicant with more than 2 years of experience
INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume, Experience) 
VALUES ('Karthik', 'Reddy', 'karthik.reddy@example.com', '9876544321', 
        '4 years experience in software engineering', 4);


-- 20 List combinations of applicants and companies in a city where the applicant has >2 years experience
SELECT a.FirstName, a.LastName, c.CompanyName FROM Applicants a
CROSS JOIN Companies c WHERE c.Location = 'Chennai' AND a.Experience > 2;



