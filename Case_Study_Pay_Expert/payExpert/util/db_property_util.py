

import configparser
import os

class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        try:
            config = configparser.ConfigParser()
            prop_file_path = os.path.join(os.path.dirname(__file__), '..', 'db.properties')
            config.read(prop_file_path)

            server = config.get("Database", "server")
            database = config.get("Database", "database")
            username = config.get("Database", "username")
            password = config.get("Database", "password")

            if username and password:
                return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
            else:
                return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
        except Exception as e:
            print(f"❌ Error reading properties file: {e}")
            return None
