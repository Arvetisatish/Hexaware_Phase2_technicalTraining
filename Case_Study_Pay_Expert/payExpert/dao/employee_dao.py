from db_config import get_db_connection
from exception.employee_not_found_exception import EmployeeNotFoundException
from exception.database_connection_exception import DatabaseConnectionException


class EmployeeDAO:

    @staticmethod
    def get_employee_by_id(employee_id):
        """Retrieve an employee by ID, raise exception if not found"""
        conn = None
        cursor = None
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?", (employee_id,))
            employee = cursor.fetchone()
            if not employee:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found!")
            return employee
        except EmployeeNotFoundException as e:
            raise e
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error fetching employee: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def get_all_employees():
        """Retrieve all employees from the database"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employee")
            employees = cursor.fetchall()
            if not employees:
                print("No employees found!")
            return employees
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error fetching employees: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def add_employee(employee):
        """Insert a new employee into the database"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (employee.first_name, employee.last_name, employee.dob, employee.gender,
                  employee.email, employee.phone, employee.address, employee.position,
                  employee.joining_date, employee.termination_date))
            conn.commit()
            print("✅ Employee added successfully!")
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error adding employee: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_employee(employee_id, field, new_value):
        """Update employee details"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            query = f"UPDATE Employee SET {field} = ? WHERE EmployeeID = ?"
            cursor.execute(query, (new_value, employee_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found!")
            print("✅ Employee updated successfully!")
        except EmployeeNotFoundException as e:
            print(f"❌ {e}")
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error updating employee: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_employee(employee_id):
        """Delete an employee from the database after removing dependent records."""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()

            # Delete dependent records first
            cursor.execute("DELETE FROM Payroll WHERE EmployeeID = ?", (employee_id,))
            cursor.execute("DELETE FROM Tax WHERE EmployeeID = ?", (employee_id,))
            cursor.execute("DELETE FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,))

            # Now delete employee
            cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,))
            conn.commit()

            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found!")

            print("✅ Employee deleted successfully!")

        except EmployeeNotFoundException as e:
            print(f"❌ {e}")
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error deleting employee: {e}")
        finally:
            cursor.close()
            conn.close()
