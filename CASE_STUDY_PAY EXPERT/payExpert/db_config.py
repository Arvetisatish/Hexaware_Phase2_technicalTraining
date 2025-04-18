from util.db_conn_util import DBConnUtil

def get_db_connection(database="master"):
    """Establish a connection to SQL Server using DBConnUtil."""
    try:
        conn = DBConnUtil.get_db_connection()
        return conn
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None


def create_database():
    """Create PayXpertDB if it doesn't exist."""
    conn = get_db_connection()
    conn.autocommit = True  # Required for CREATE DATABASE
    cursor = conn.cursor()

    try:
        cursor.execute(
            "IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'PayXpertDB') CREATE DATABASE PayXpertDB;")
        print("✅ Database 'PayXpertDB' is ready!")
    except Exception as e:
        print(f"❌ Error creating database: {e}")
    finally:
        cursor.close()
        conn.close()


def create_tables():
    """Create required tables in PayXpertDB."""
    conn = get_db_connection()  # Connect to PayXpertDB
    conn.autocommit = True
    cursor = conn.cursor()

    try:
        # Employee Table
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Employee')
        CREATE TABLE Employee (
            EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            DateOfBirth DATE,
            Gender VARCHAR(10),
            Email VARCHAR(100),
            PhoneNumber VARCHAR(15),
            Address VARCHAR(255),
            Position VARCHAR(50),
            JoiningDate DATE,
            TerminationDate DATE NULL
        );
        """)

        # Payroll Table
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Payroll')
        CREATE TABLE Payroll (
            PayrollID INT IDENTITY(1,1) PRIMARY KEY,
            EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
            PayPeriodStartDate DATE,
            PayPeriodEndDate DATE,
            BasicSalary DECIMAL(10,2),
            OvertimePay DECIMAL(10,2),
            Deductions DECIMAL(10,2),
            NetSalary DECIMAL(10,2)
        );
        """)

        # Tax Table
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Tax')
        CREATE TABLE Tax (
            TaxID INT IDENTITY(1,1) PRIMARY KEY,
            EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
            TaxYear INT,
            TaxableIncome DECIMAL(10,2),
            TaxAmount DECIMAL(10,2)
        );
        """)

        # FinancialRecord Table
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'FinancialRecord')
        CREATE TABLE FinancialRecord (
            RecordID INT IDENTITY(1,1) PRIMARY KEY,
            EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
            RecordDate DATE,
            Description VARCHAR(255),
            Amount DECIMAL(10,2),
            RecordType VARCHAR(50)
        );
        """)

        print("✅ Tables created successfully!")

    except Exception as e:
        print(f"❌ Error creating tables: {e}")

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    create_database()
    create_tables()
