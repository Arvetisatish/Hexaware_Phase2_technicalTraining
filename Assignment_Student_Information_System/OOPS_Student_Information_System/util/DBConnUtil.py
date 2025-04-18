import pyodbc
from util.DBPropertyUtill import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(config_file: str):
        try:
            conn_str = DBPropertyUtil.get_connection_string(config_file)
            connection = pyodbc.connect(conn_str)
            return connection
        except pyodbc.Error as e:
            raise Exception(f"Database connection failed: {e}")
