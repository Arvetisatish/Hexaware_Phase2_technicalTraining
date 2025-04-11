class TeacherNotFoundException(Exception):
    def __init__(self , message="Teacher not found"):
        super().__init__(message)