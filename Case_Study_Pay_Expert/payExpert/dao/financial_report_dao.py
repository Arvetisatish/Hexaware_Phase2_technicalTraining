from db_config import get_db_connection
from exception.financial_record_exception import FinancialRecordException

class FinancialReportDAO:

    @staticmethod
    def generate_salary_summary():
        """Generate a summary of employee salaries"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("""
                SELECT e.EmployeeID, e.FirstName + ' ' + e.LastName AS Name,
       COALESCE(SUM(p.BasicSalary), 0) AS TotalSalary,
       COALESCE(SUM(p.OvertimePay), 0) AS Overtime,
       COALESCE(SUM(p.Deductions), 0) AS Deductions,
       COALESCE(SUM(p.BasicSalary + p.OvertimePay - p.Deductions), 0) AS NetPay
     FROM Employee e
        LEFT JOIN Payroll p ON e.EmployeeID = p.EmployeeID
        GROUP BY e.EmployeeID, e.FirstName, e.LastName
        """)
            return cursor.fetchall()
        except Exception as e:
            raise FinancialRecordException(f"❌ Error generating salary summary: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def generate_tax_summary(year=None):
        """Generate tax summary report per employee"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            if year:
                cursor.execute("""
                    SELECT e.EmployeeID, e.FirstName + ' ' + e.LastName AS Name,
                           COALESCE(SUM(t.TaxableIncome), 0) AS TotalTaxableIncome,
                           COALESCE(SUM(t.TaxAmount), 0) AS TotalTaxPaid
                    FROM Employee e
                    LEFT JOIN Tax t ON e.EmployeeID = t.EmployeeID
                    WHERE t.TaxYear = ?
                    GROUP BY e.EmployeeID, e.FirstName, e.LastName
                """, (year,))
            else:
                cursor.execute("""
                    SELECT e.EmployeeID, e.FirstName + ' ' + e.LastName AS Name,
                           COALESCE(SUM(t.TaxableIncome), 0) AS TotalTaxableIncome,
                           COALESCE(SUM(t.TaxAmount), 0) AS TotalTaxPaid
                    FROM Employee e
                    LEFT JOIN Tax t ON e.EmployeeID = t.EmployeeID
                    GROUP BY e.EmployeeID, e.FirstName, e.LastName
                """)
            return cursor.fetchall()
        except Exception as e:
            raise FinancialRecordException(f"❌ Error generating tax summary: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def generate_complete_financial_report():
        """Generate a complete financial report including Salary, Tax, and Payroll summary"""
        try:
            conn = get_db_connection("PayXpertDB")
            cursor = conn.cursor()
            cursor.execute("""
                SELECT e.EmployeeID, e.FirstName, e.LastName,
                       COALESCE(SUM(p.BasicSalary), 0) AS TotalSalary,
                       COALESCE(SUM(p.OvertimePay), 0) AS TotalOvertime,
                       COALESCE(SUM(p.Deductions), 0) AS TotalDeductions,
                       COALESCE(SUM(p.NetSalary), 0) AS NetPay,
                       COALESCE(SUM(t.TaxableIncome), 0) AS TotalTaxableIncome,
                       COALESCE(SUM(t.TaxAmount), 0) AS TotalTaxPaid
                FROM Employee e
                LEFT JOIN Payroll p ON e.EmployeeID = p.EmployeeID
                LEFT JOIN Tax t ON e.EmployeeID = t.EmployeeID
                GROUP BY e.EmployeeID, e.FirstName, e.LastName
            """)
            return cursor.fetchall()
        except Exception as e:
            raise FinancialRecordException(f"❌ Error generating financial report: {e}")
        finally:
            cursor.close()
            conn.close()
