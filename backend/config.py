import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configurations
    MYSQL_CONFIG = {
        'host': os.getenv('MYSQL_HOST', 'localhost'),
        'user': os.getenv('MYSQL_USER', 'root'),
        'password': os.getenv('MYSQL_PASSWORD', ''),
        'database': os.getenv('MYSQL_DB', 'health_data')
    }
    
    ORACLE_CONFIG = {
        'user': os.getenv('ORACLE_USER', 'system'),
        'password': os.getenv('ORACLE_PASSWORD', ''),
        'dsn': os.getenv('ORACLE_DSN', 'localhost:1521/xe')
    }
    
    SQL_SERVER_CONFIG = {
        'server': os.getenv('SQL_SERVER', 'localhost'),
        'database': os.getenv('SQL_SERVER_DB', 'health_metrics'),
        'username': os.getenv('SQL_SERVER_USER', 'sa'),
        'password': os.getenv('SQL_SERVER_PASSWORD', ''),
        'driver': os.getenv('SQL_SERVER_DRIVER', 'ODBC Driver 17 for SQL Server')
    }