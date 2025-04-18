import configparser

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(config_file: str) -> str:
        config = configparser.ConfigParser()
        config.read(config_file)

        try:
            server = config['database']['server']
            database = config['database']['database']
            username = config['database']['username']
            password = config['database']['password']
            driver = config['database'].get('driver', '{ODBC Driver 17 for SQL Server}')

            return f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        except KeyError as e:
            raise Exception(f"Missing key in config file: {e}")
