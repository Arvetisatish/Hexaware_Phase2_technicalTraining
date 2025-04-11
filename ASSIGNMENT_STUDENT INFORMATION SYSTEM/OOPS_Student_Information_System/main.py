from datetime import date
from entity.student import Student
from entity.teacher import Teacher
from entity.course import Course
from dao.sis_manager import SISManager

def main():
    sis = SISManager()

    # Preload some sample data for testing
    sis.add_teacher(Teacher(1, "Anita", "Deshmukh", "anita.deshmukh@example.com"))
    sis.add_course(Course(1, "Introduction to Programming", "CS101", sis.teachers[1]))
    sis.add_student(Student(1, "Rahul", "Sharma", date(2000, 8, 15), "rahul.sharma@gmail.com", "9876543210"))

    while True:
        print("\n=== Student Information System ===")
        print("1. Enroll Student in Course")
        print("2. Assign Teacher to Course")
        print("3. Record Student Payment")
        print("4. Generate Enrollment Report")
        print("5. Generate Payment Report")
        print("6. View Course Statistics")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                student_id = int(input("Enter student ID: "))
                course_id = int(input("Enter course ID: "))
                enrollment_date = date.fromisoformat(input("Enter enrollment date (YYYY-MM-DD): "))
                sis.enroll_student_in_course(student_id, course_id, enrollment_date)

            elif choice == "2":
                teacher_id = int(input("Enter teacher ID: "))
                course_id = int(input("Enter course ID: "))
                sis.assign_teacher_to_course(teacher_id, course_id)

            elif choice == "3":
                student_id = int(input("Enter student ID: "))
                amount = float(input("Enter payment amount: "))
                payment_date = date.fromisoformat(input("Enter payment date (YYYY-MM-DD): "))
                sis.record_payment(student_id, amount, payment_date)

            elif choice == "4":
                course_id = int(input("Enter course ID for enrollment report: "))
                sis.generate_enrollment_report(course_id)

            elif choice == "5":
                student_id = int(input("Enter student ID for payment report: "))
                sis.generate_payment_report(student_id)

            elif choice == "6":
                course_id = int(input("Enter course ID for statistics: "))
                sis.calculate_course_statistics(course_id)

            elif choice == "0":
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
