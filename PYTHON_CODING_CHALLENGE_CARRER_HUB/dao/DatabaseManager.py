from util.db_conn_util import DBConnUtil
from entity.company import Company
from entity.applicant import Applicant
from entity.job_listing import JobListing
from entity.job_application import JobApplication
from exception.exceptions import DatabaseConnectionException
import pyodbc

class DatabaseManager:

    @staticmethod
    def initialize_database(config_file: str):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()

            cursor.execute('''
                IF OBJECT_ID('Companies', 'U') IS NULL
                CREATE TABLE Companies (
                    CompanyID INT PRIMARY KEY,
                    CompanyName VARCHAR(100),
                    Location VARCHAR(100)
                )
            ''')

            cursor.execute('''
                IF OBJECT_ID('Applicants', 'U') IS NULL
                CREATE TABLE Applicants (
                    ApplicantID INT PRIMARY KEY,
                    FirstName VARCHAR(50),
                    LastName VARCHAR(50),
                    Email VARCHAR(100),
                    Phone VARCHAR(15),
                    Resume VARCHAR(255)
                )
            ''')

            cursor.execute('''
                IF OBJECT_ID('Jobs', 'U') IS NULL
                CREATE TABLE Jobs (
                    JobID INT PRIMARY KEY,
                    CompanyID INT,
                    JobTitle VARCHAR(100),
                    JobDescription TEXT,
                    JobLocation VARCHAR(100),
                    Salary DECIMAL(10, 2),
                    JobType VARCHAR(50),
                    PostedDate DATETIME,
                    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
                )
            ''')

            cursor.execute('''
                IF OBJECT_ID('Applications', 'U') IS NULL
                CREATE TABLE Applications (
                    ApplicationID INT PRIMARY KEY,
                    JobID INT,
                    ApplicantID INT,
                    ApplicationDate DATETIME,
                    CoverLetter TEXT,
                    FOREIGN KEY (JobID) REFERENCES Jobs(JobID),
                    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
                )
            ''')

            conn.commit()
            print("✅ Database and tables initialized successfully.")
        except Exception as e:
            raise DatabaseConnectionException(f"Failed to initialize database: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def insert_company(config_file, company: Company):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Companies (CompanyID, CompanyName, Location)
                VALUES (?, ?, ?)
            ''', (company.company_id, company.name, company.location))
            conn.commit()
            print("✅ Company inserted successfully.")
        except pyodbc.Error as e:
            print("❌ Error inserting company:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def insert_applicant(config_file, applicant: Applicant):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Applicants (ApplicantID, FirstName, LastName, Email, Phone, Resume)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (applicant.applicant_id, applicant.first_name, applicant.last_name, applicant.email, applicant.phone, applicant.resume))
            conn.commit()
            print("✅ Applicant inserted successfully.")
        except pyodbc.Error as e:
            print("❌ Error inserting applicant:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def insert_job(config_file, job: JobListing):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Jobs (JobID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (job.job_id, job.company_id, job.job_title, job.job_description, job.job_location, job.salary, job.job_type, job.posted_date))
            conn.commit()
            print("✅ Job inserted successfully.")
        except pyodbc.Error as e:
            print("❌ Error inserting job:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def insert_application(config_file, application: JobApplication):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Applications (ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter)
                VALUES (?, ?, ?, ?, ?)
            ''', (application.application_id, application.job_id, application.applicant_id, application.application_date, application.cover_letter))
            conn.commit()
            print("✅ Application inserted successfully.")
        except pyodbc.Error as e:
            print("❌ Error inserting application:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def get_all_companies(config_file):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Companies")
            rows = cursor.fetchall()
            print("Company ID | Company Name        | Location")
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("❌ Error retrieving companies:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def get_all_applicants(config_file):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Applicants")
            rows = cursor.fetchall()
            print("\n--- Applicants ---")
            print("Applicant ID | First Name | Last Name | Email             | Phone      | Resume")
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("❌ Error retrieving applicants:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def get_all_jobs(config_file):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Jobs")
            rows = cursor.fetchall()
            print("Job ID | Company ID | Job Title           | Job Location | Salary  | Job Type | Posted Date")
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("❌ Error retrieving jobs:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def get_all_applications(config_file):
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Applications")
            rows = cursor.fetchall()
            print("\n--- Applications ---")
            print("Application ID | Job ID | Applicant ID | Application Date        | Cover Letter")
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("❌ Error retrieving applications:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
