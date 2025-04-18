from util.db_property_util import DBPropertyUtil
import pyodbc
from exception.exceptions import DatabaseConnectionException

class DBConnUtil:
    @staticmethod
    def get_connection(config_file: str):
        try:
            config = DBPropertyUtil.get_connection_string(config_file)
            conn_str = (
                f"DRIVER={{{config['driver']}}};"
                f"SERVER={config['server']};"
                f"DATABASE={config['database']};"
                f"Trusted_Connection={config['trusted_connection']};"
            )
            return pyodbc.connect(conn_str)
        except Exception as e:
            raise DatabaseConnectionException(str(e))

