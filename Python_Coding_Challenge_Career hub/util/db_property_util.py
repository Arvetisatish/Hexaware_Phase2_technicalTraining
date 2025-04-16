import configparser

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(config_file: str) -> dict:
        config = configparser.ConfigParser()
        config.read(config_file)

        return {
            'driver': config.get('database', 'driver'),
            'server': config.get('database', 'server'),
            'database': config.get('database', 'database'),
            'trusted_connection': config.get('database', 'trusted_connection')
        }
