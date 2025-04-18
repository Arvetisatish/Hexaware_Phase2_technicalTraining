# util/db_conn_util.py

import pyodbc
from util.db_property_util import DBPropertyUtil
from exception.database_connection_exception import DatabaseConnectionException

class DBConnUtil:
    @staticmethod
    def get_db_connection():
        try:
            connection_string = DBPropertyUtil.get_connection_string()
            if not connection_string:
                raise DatabaseConnectionException("❌ Connection string could not be retrieved!")

            return pyodbc.connect(connection_string)
        except Exception as e:
            raise DatabaseConnectionException(f"❌ Database connection failed: {e}")
