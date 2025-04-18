from db_config import get_db_connection
from exception.payroll_generation_exception import PayrollGenerationException
from exception.database_connection_exception import DatabaseConnectionException

class PayrollDAO:
    @staticmethod
    def add_payroll(payroll):
        """Insert a new payroll entry into the database"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (payroll.employee_id, payroll.start_date, payroll.end_date, payroll.basic_salary,
                  payroll.overtime_pay, payroll.deductions, payroll.net_salary))
            conn.commit()
            print("✅ Payroll entry added successfully!")
        except Exception as e:
            raise PayrollGenerationException(f"❌ Error generating payroll: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_payroll_for_employee(employee_id):
        """Retrieve payroll records for a specific employee"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
            payroll_records = cursor.fetchall()
            if not payroll_records:
                print(f"No payroll records found for Employee ID {employee_id}!")
            return payroll_records
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error fetching payroll records: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_payroll(payroll_id, field, new_value):
        """Update payroll details"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            query = f"UPDATE Payroll SET {field} = ? WHERE PayrollID = ?"
            cursor.execute(query, (new_value, payroll_id))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No payroll found with ID {payroll_id}!")
            else:
                print("✅ Payroll updated successfully!")
        except Exception as e:
            raise PayrollGenerationException(f"❌ Error updating payroll: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_payroll(payroll_id):
        """Delete a payroll record"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Payroll WHERE PayrollID = ?", (payroll_id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No payroll found with ID {payroll_id}!")
            else:
                print("✅ Payroll deleted successfully!")
        except Exception as e:
            raise PayrollGenerationException(f"❌ Error deleting payroll: {e}")
        finally:
            cursor.close()
            conn.close()
