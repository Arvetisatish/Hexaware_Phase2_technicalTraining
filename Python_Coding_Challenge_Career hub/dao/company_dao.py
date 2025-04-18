from util.db_conn_util import DBConnUtil
from entity.company import Company
import pyodbc

class CompanyDAO:
    def insert_company(self, company, config_file):
        cursor = None
        try:
            conn = DBConnUtil.get_connection(config_file)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Companies (CompanyID, CompanyName, Location)
                VALUES (?, ?, ?)
            """, (company.company_id, company.name, company.location))
            conn.commit()
            print("✅ Company inserted successfully.")
        except pyodbc.Error as e:
            print("❌ Error inserting company:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
