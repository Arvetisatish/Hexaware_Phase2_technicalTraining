from entity.employee import Employee
from dao.employee_dao import EmployeeDAO
from entity.payroll import Payroll
from dao.payroll_dao import PayrollDAO
from entity.tax import Tax
from dao.tax_dao import TaxDAO
from dao.financial_report_dao import FinancialReportDAO

# Custom Exceptions
from exception.employee_not_found_exception import EmployeeNotFoundException
from exception.database_connection_exception import DatabaseConnectionException
from exception.payroll_generation_exception import PayrollGenerationException
from exception.tax_calculation_exception import TaxCalculationException
from exception.financial_record_exception import FinancialRecordException

def menu():
    while True:
        print("\n=== PayXpert Management System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Add Payroll")
        print("6. View Payroll for Employee")
        print("7. Update Payroll")
        print("8. Delete Payroll")
        print("9. Add Tax Record")
        print("10. View Tax for Employee")
        print("11. Update Tax")
        print("12. Delete Tax")
        print("13. Generate Salary Summary Report")
        print("14. Generate Tax Summary Report")
        print("15. Generate Complete Financial Report")
        print("16. Exit")

        choice = input("Enter your choice: ").strip()

        if not choice.isdigit() or not (1 <= int(choice) <= 16):
            print("❌ Invalid choice! Please enter a number between 1-16.")
            continue

        choice = int(choice)

        try:
            if choice == 1:
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                gender = input("Gender: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                position = input("Position: ")
                joining_date = input("Joining Date (YYYY-MM-DD): ")
                termination_date = input("Termination Date (YYYY-MM-DD) or leave empty: ") or None

                employee = Employee(None, first_name, last_name, dob, gender, email, phone, address, position, joining_date, termination_date)
                EmployeeDAO.add_employee(employee)

            elif choice == 2:
                employees = EmployeeDAO.get_all_employees()
                if employees:
                    print("\n=== Employee List ===")
                    print(
                        "EmployeeID| First Name |Last Name | DOB | Gender | Email | Phone | Address | Position | Joining Date | Termination Date")

                    for emp in employees:
                        print(emp)
                else:
                    print("No employees found!")

            elif choice == 3:
                emp_id = int(input("Enter Employee ID to update: "))
                field = input("Enter field to update (FirstName, LastName, Email, etc.): ")
                new_value = input(f"Enter new value for {field}: ")
                EmployeeDAO.update_employee(emp_id, field, new_value)

            elif choice == 4:
                emp_id = int(input("Enter Employee ID to delete: "))
                EmployeeDAO.delete_employee(emp_id)

            elif choice == 5:
                emp_id = int(input("Enter Employee ID: "))
                EmployeeDAO.get_employee_by_id(emp_id)  # validate
                start_date = input("Pay Period Start Date (YYYY-MM-DD): ")
                end_date = input("Pay Period End Date (YYYY-MM-DD): ")
                basic_salary = float(input("Basic Salary: "))
                overtime_pay = float(input("Overtime Pay: "))
                deductions = float(input("Deductions: "))
                net_salary = basic_salary + overtime_pay - deductions

                payroll = Payroll(None, emp_id, start_date, end_date, basic_salary, overtime_pay, deductions, net_salary)
                PayrollDAO.add_payroll(payroll)

            elif choice == 6:
                emp_id = int(input("Enter Employee ID: "))
                records = PayrollDAO.get_payroll_for_employee(emp_id)
                if records:
                    print("\n=== Payroll Records ===")
                    for r in records:
                        print(r)
                else:
                    print("No payroll records found!")

            elif choice == 7:
                payroll_id = int(input("Enter Payroll ID to update: "))
                field = input("Enter field to update (BasicSalary, OvertimePay, etc.): ")
                new_value = input(f"Enter new value for {field}: ")
                PayrollDAO.update_payroll(payroll_id, field, new_value)

            elif choice == 8:
                payroll_id = int(input("Enter Payroll ID to delete: "))
                PayrollDAO.delete_payroll(payroll_id)

            elif choice == 9:
                emp_id = int(input("Enter Employee ID: "))
                EmployeeDAO.get_employee_by_id(emp_id)  # validate
                year = int(input("Enter Tax Year: "))
                taxable_income = float(input("Enter Taxable Income: "))
                TaxDAO.add_tax(emp_id, year, taxable_income)

            elif choice == 10:
                emp_id = int(input("Enter Employee ID: "))
                taxes = TaxDAO.get_taxes_for_employee(emp_id)
                if taxes:
                    print("\n=== Tax Records ===")
                    for t in taxes:
                        print(t)
                else:
                    print("No tax records found!")

            elif choice == 11:
                tax_id = int(input("Enter Tax ID to update: "))
                field = input("Enter field to update (TaxableIncome, TaxAmount): ")
                new_value = input(f"Enter new value for {field}: ")
                TaxDAO.update_tax(tax_id, field, new_value)

            elif choice == 12:
                tax_id = int(input("Enter Tax ID to delete: "))
                TaxDAO.delete_tax(tax_id)

            elif choice == 13:
                report = FinancialReportDAO.generate_salary_summary()
                if report:
                    print("\n=== Employee Salary Summary ===")
                    print("EmployeeID | Name | Total Salary | Overtime | Deductions | Net Pay")
                    for row in report:
                        print(row)
                else:
                    print("No salary data available!")

            elif choice == 14:
                year_input = input("Enter tax year (or press Enter for all years): ")
                year = int(year_input) if year_input else None
                report = FinancialReportDAO.generate_tax_summary(year)
                if report:
                    print("\n=== Tax Summary Report ===")
                    print("EmployeeID | Name | Total Taxable Income | Total Tax Paid")
                    for row in report:
                        print(row)
                else:
                    print("No tax data available!")

            elif choice == 15:
                report = FinancialReportDAO.generate_complete_financial_report()
                if report:
                    print("\n=== Complete Financial Report ===")
                    print("EmployeeID | Name | Total Salary | Overtime | Deductions | Net Pay | Taxable Income | Tax Paid")
                    for row in report:
                        print(row)
                else:
                    print("No financial data available!")

            elif choice == 16:
                print("Exiting...")
                break

        except EmployeeNotFoundException as e:
            print(f"❌ {e}")
        except DatabaseConnectionException as e:
            print(f"❌ Database Error: {e}")
        except PayrollGenerationException as e:
            print(f"❌ Payroll Error: {e}")
        except TaxCalculationException as e:
            print(f"❌ Tax Error: {e}")
        except FinancialRecordException as e:
            print(f"❌ Financial Report Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    menu()
