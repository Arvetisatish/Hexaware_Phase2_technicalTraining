from util.db_conn_util import DBConnUtil
from entity.job_application import JobApplication
import pyodbc
from exception.exceptions import ApplicationDeadlineException
import datetime

class JobApplicationDAO:
    def insert_application(self, application, config_file):
        conn = None
        cursor = None
        try:
            # Get the current date for validation (if needed)
            current_date = datetime.datetime.now()


            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()

            # Adjust this query to exclude ApplicationID, assuming it auto-increments
            cursor.execute("""
                INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter)
                VALUES (?, ?, ?, ?)
            """, (
                application.job_id,  # JobID
                application.applicant_id,  # ApplicantID
                current_date,  # ApplicationDate
                application.cover_letter  # CoverLetter
            ))
            conn.commit()

        except ApplicationDeadlineException as ade:
            print(ade)
        except ValueError as ve:
            print(ve)
        except pyodbc.Error as e:
            print("❌ Error inserting job application:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
