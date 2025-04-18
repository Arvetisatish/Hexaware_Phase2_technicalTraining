from db_config import get_db_connection
from exception.tax_calculation_exception import TaxCalculationException
from exception.database_connection_exception import DatabaseConnectionException
from entity.tax import Tax
from decimal import Decimal

class TaxDAO:
    @staticmethod
    def add_tax(employee_id, tax_year, taxable_income):
        """Insert tax record into the database"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            tax_amount = TaxDAO.calculate_tax(taxable_income)
            cursor.execute("""
                INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
                VALUES (?, ?, ?, ?)
            """, (employee_id, tax_year, taxable_income, tax_amount))
            conn.commit()
            print(f"✅ Tax record added for Employee {employee_id}!")
        except Exception as e:
            raise TaxCalculationException(f"❌ Error adding tax record: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def calculate_tax(taxable_income):
        try:
            income = Decimal(str(taxable_income))
            if income <= Decimal('250000'):
                return Decimal('0.00')
            elif income <= Decimal('500000'):
                return income * Decimal('0.05')
            elif income <= Decimal('1000000'):
                return income * Decimal('0.2')
            else:
                return income * Decimal('0.3')
        except Exception as e:
            raise TaxCalculationException(f"❌ Error calculating tax: {e}")

    @staticmethod
    def get_taxes_for_employee(employee_id):
        """Retrieve tax records for a specific employee and return Tax objects"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE EmployeeID = ?", (employee_id,))
            rows = cursor.fetchall()
            if not rows:
                print(f"No tax records found for Employee ID {employee_id}!")
                return []
            return [Tax(*row) for row in rows]  # ✅ Convert to Tax objects
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Error fetching tax records: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_tax(tax_id, field, new_value):
        """Update tax details"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            query = f"UPDATE Tax SET {field} = ? WHERE TaxID = ?"
            cursor.execute(query, (new_value, tax_id))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No tax record found with ID {tax_id}!")
            else:
                print("✅ Tax record updated successfully!")
        except Exception as e:
            raise TaxCalculationException(f"❌ Error updating tax record: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_tax(tax_id):
        """Delete a tax record"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Tax WHERE TaxID = ?", (tax_id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No tax record found with ID {tax_id}!")
            else:
                print("✅ Tax record deleted successfully!")
        except Exception as e:
            raise TaxCalculationException(f"❌ Error deleting tax record: {e}")
        finally:
            cursor.close()
            conn.close()
