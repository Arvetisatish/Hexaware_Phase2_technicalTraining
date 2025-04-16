from dao.DatabaseManager  import DatabaseManager
from dao.application_dao import JobApplicationDAO
from dao.company_dao import CompanyDAO
from entity.company import Company
from entity.applicant import Applicant
from entity.job_listing import JobListing
from entity.job_application import JobApplication
from datetime import datetime
from exception.exceptions import InvalidEmailException, SalaryException, FileUploadException, ApplicationDeadlineException, DatabaseConnectionException
import os
import re


CONFIG_FILE = "dbconfig.ini"


def main():
    while True:
        print("\n===== CareerHub Menu =====")
        print("1. Initialize Database")
        print("2. Insert Company")
        print("3. Insert Applicant")
        print("4. Insert Job")
        print("5. Insert Application")
        print("6. View All Companies")
        print("7. View All Applicants")
        print("8. View All Jobs")
        print("9. View All Applications")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            DatabaseManager.initialize_database(CONFIG_FILE)


        elif choice == "2":
            cid = int(input("Enter Company ID: "))
            name = input("Enter Company Name: ")
            location = input("Enter Location: ")
            company = Company(cid, name, location)
            company_dao = CompanyDAO()
            company_dao.insert_company(company, CONFIG_FILE)

        elif choice == "3":
            aid = int(input("Enter Applicant ID: "))
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            email = input("Enter Email: ")
            try:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise InvalidEmailException("❌ Invalid email format. Please enter a valid email address.")
                phone = input("Enter Phone: ")
                resume = input("Enter Resume File Path: ")
                if not os.path.isfile(resume):
                    raise FileUploadException("❌ Resume file not found or unsupported format.")
                applicant = Applicant(aid, fname, lname, email, phone, resume)
                DatabaseManager.insert_applicant(CONFIG_FILE, applicant)
            except InvalidEmailException as ie:
                print(ie)
            except FileUploadException as fe:
                print(fe)

        elif choice == "4":
            jid = int(input("Enter Job ID: "))
            cid = int(input("Enter Company ID: "))
            title = input("Enter Job Title: ")
            desc = input("Enter Description: ")
            loc = input("Enter Location: ")

            while True:
                salary_input = input("Enter Salary: ")
                try:
                    salary = float(salary_input)
                    if salary <= 0:
                        raise SalaryException("❌ Salary cannot be negative or zero.")
                    break
                except ValueError:
                    print("❌ Invalid salary input. Please enter a valid number.")
                except SalaryException as se:
                    print(se)

            jtype = input("Enter Job Type (Full-time/Part-time): ")
            posted = datetime.now()
            job = JobListing(jid, cid, title, desc, loc, salary, jtype)
            try:
                DatabaseManager.insert_job(CONFIG_FILE, job)
            except DatabaseConnectionException as dbce:
                print(dbce)

        elif choice == "5":

                try:
                    apid = int(input("Enter Application ID: "))
                    jid = int(input("Enter Job ID: "))
                    aid = int(input("Enter Applicant ID: "))
                    date = datetime.now()
                    cover = input("Enter Cover Letter: ")

                    # Ensure the cover letter is not empty
                    if not cover:
                        raise ValueError("❌ Cover Letter cannot be empty.")

                    # Specify the config file path
                    config_file = "dbconfig.ini"

                    # Create the JobApplication object with the given inputs
                    application = JobApplication(apid, jid, aid, date, cover)

                    # Instantiate the DAO and insert the application
                    job_application_dao = JobApplicationDAO()
                    job_application_dao.insert_application(application, config_file)

                except ApplicationDeadlineException as ade:
                    print(ade)
                except ValueError as ve:
                    print(ve)


        elif choice == "6":
            DatabaseManager.get_all_companies(CONFIG_FILE)

        elif choice == "7":
            DatabaseManager.get_all_applicants(CONFIG_FILE)

        elif choice == "8":
            DatabaseManager.get_all_jobs(CONFIG_FILE)

        elif choice == "9":
            DatabaseManager.get_all_applications(CONFIG_FILE)

        elif choice == "0":
            print("👋 Exiting CareerHub. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
