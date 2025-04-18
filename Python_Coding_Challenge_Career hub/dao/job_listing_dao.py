
from util.db_conn_util import DBConnUtil
from entity.job_listing import jobListing
import pyodbc
from exception.exceptions import SalaryException

class JobListingDAO:
    def insert_job_listing(self, job):
        try:
            if job.salary < 0:
                raise SalaryException("❌ Salary cannot be negative.")

            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO JobListings 
                (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                job.company_id,
                job.title,
                job.description,
                job.location,
                job.salary,
                job.job_type,
                job.posted_date
            ))
            conn.commit()
        except SalaryException as se:
            print(se)
        except pyodbc.Error as e:
            print("❌ Error inserting job listing:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def get_all_job_listings(self):
        jobs = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT JobID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate
                FROM JobListings
            """)
            rows = cursor.fetchall()
            for row in rows:
                job = jobListing(
                    job_id=row[0],
                    company_id=row[1],
                    title=row[2],
                    description=row[3],
                    location=row[4],
                    salary=row[5],
                    job_type=row[6],
                    posted_date=row[7]
                )
                jobs.append(job)
        except pyodbc.Error as e:
            print("❌ Error retrieving job listings:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return jobs
