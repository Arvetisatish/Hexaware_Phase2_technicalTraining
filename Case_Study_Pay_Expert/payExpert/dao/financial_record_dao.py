from db_config import get_db_connection
from exception.financial_record_exception import FinancialRecordException
from exception.database_connection_exception import DatabaseConnectionException

class FinancialRecordDAO:
    @staticmethod
    def add_financial_record(employee_id, record_date, description, amount, record_type):
        """Insert a financial record into the database"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType)
                VALUES (?, ?, ?, ?, ?)
            """, (employee_id, record_date, description, amount, record_type))
            conn.commit()
            print("✅ Financial record added successfully!")
        except Exception as e:
            raise FinancialRecordException(f"❌ Error adding financial record: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_financial_records_for_employee(employee_id):
        """Retrieve all financial records for a specific employee"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,))
            records = cursor.fetchall()
            if not records:
                print(f"No financial records found for Employee ID {employee_id}!")
            return records
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error fetching financial records: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_financial_record(record_id, field, new_value):
        """Update financial record details"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"UPDATE FinancialRecord SET {field} = ? WHERE RecordID = ?"
            cursor.execute(query, (new_value, record_id))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No financial record found with ID {record_id}!")
            else:
                print("✅ Financial record updated successfully!")
        except Exception as e:
            raise FinancialRecordException(f"❌ Error updating financial record: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_financial_record(record_id):
        """Delete a financial record"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM FinancialRecord WHERE RecordID = ?", (record_id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No financial record found with ID {record_id}!")
            else:
                print("✅ Financial record deleted successfully!")
        except Exception as e:
            raise FinancialRecordException(f"❌ Error deleting financial record: {e}")
        finally:
            cursor.close()
            conn.close()
