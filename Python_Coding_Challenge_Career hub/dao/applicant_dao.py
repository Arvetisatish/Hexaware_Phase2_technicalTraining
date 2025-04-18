from util.db_conn_util import DBConnUtil
from entity.applicant import Applicant
import pyodbc
import re
from exception.exceptions import InvalidEmailException

class ApplicantDAO:
    def insert_applicant(self, applicant):
        try:
            # Validate email format
            if not re.match(r"[^@]+@[^@]+\.[^@]+", applicant.email):
                raise InvalidEmailException("❌ Invalid email format.")

            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
                VALUES (?, ?, ?, ?, ?)
            """, (
                applicant.first_name,
                applicant.last_name,
                applicant.email,
                applicant.phone,
                applicant.resume
            ))
            conn.commit()
        except InvalidEmailException as ie:
            print(ie)
        except pyodbc.Error as e:
            print("❌ Error inserting applicant:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def get_all_applicants(self):
        applicants = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT ApplicantID, FirstName, LastName, Email, Phone, Resume
                FROM Applicants
            """)
            rows = cursor.fetchall()
            for row in rows:
                applicant = Applicant(
                    applicant_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    phone=row[4],
                    resume=row[5]
                )
                applicants.append(applicant)
        except pyodbc.Error as e:
            print("❌ Error retrieving applicants:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return applicants
