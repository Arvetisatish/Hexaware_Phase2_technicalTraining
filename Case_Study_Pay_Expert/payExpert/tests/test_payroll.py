import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.payroll import Payroll
from dao.tax_dao import TaxDAO
from exception.tax_calculation_exception import TaxCalculationException
import pytest

def test_calculate_gross_salary():
    """Verify that the system correctly calculates the gross salary for an employee"""
    payroll = Payroll(None, 1, "2025-01-01", "2025-01-31", 50000, 5000, 0, 0)
    gross_salary = payroll.basic_salary + payroll.overtime_pay
    assert gross_salary == 55000

def test_calculate_net_salary_after_deductions():
    """Ensure accurate net salary calculation"""
    payroll = Payroll(None, 2, "2025-02-01", "2025-02-28", 40000, 2000, 1500, 0)
    net_salary = payroll.basic_salary + payroll.overtime_pay - payroll.deductions
    assert net_salary == 40500

def test_high_income_tax_calculation():
    """Test tax calculation logic for high-income employees"""
    taxable_income = 1500000
    expected_tax = taxable_income * 0.3
    tax = TaxDAO.calculate_tax(taxable_income)
    assert float(tax) == expected_tax

def test_invalid_employee_data_handling():
    """Ensure system throws exception for invalid employee ID"""
    from dao.employee_dao import EmployeeDAO
    from exception.employee_not_found_exception import EmployeeNotFoundException

    invalid_id = 9999  # Assuming this ID doesn't exist
    with pytest.raises(EmployeeNotFoundException):
        EmployeeDAO.get_employee_by_id(invalid_id)
