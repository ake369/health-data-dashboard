import mysql.connector
from config import Config
import pandas as pd

class MySQLConnector:
    def __init__(self):
        self.config = Config.MYSQL_CONFIG
    
    def get_connection(self):
        return mysql.connector.connect(**self.config)
    
    def get_patient_demographics(self):
        try:
            conn = self.get_connection()
            query = """
            SELECT 
                region,
                age_group,
                gender,
                COUNT(*) as patient_count,
                AVG(bmi) as avg_bmi,
                AVG(blood_pressure_systolic) as avg_bp
            FROM patient_demographics 
            GROUP BY region, age_group, gender
            ORDER BY region, age_group, gender
            """
            df = pd.read_sql(query, conn)
            conn.close()
            return df.to_dict('records')
        except Exception as e:
            print(f"MySQL Error: {e}")
            # Return sample data for demo with Ethiopian regions
            return [
                {"region": "Addis Ababa", "age_group": "18-30", "gender": "Male", "patient_count": 450, "avg_bmi": 23.5, "avg_bp": 118},
                {"region": "Addis Ababa", "age_group": "18-30", "gender": "Female", "patient_count": 520, "avg_bmi": 22.8, "avg_bp": 116},
                {"region": "Addis Ababa", "age_group": "31-45", "gender": "Male", "patient_count": 380, "avg_bmi": 25.2, "avg_bp": 122},
                {"region": "Addis Ababa", "age_group": "31-45", "gender": "Female", "patient_count": 420, "avg_bmi": 24.1, "avg_bp": 120},
                {"region": "Amhara", "age_group": "18-30", "gender": "Male", "patient_count": 680, "avg_bmi": 21.8, "avg_bp": 115},
                {"region": "Amhara", "age_group": "18-30", "gender": "Female", "patient_count": 720, "avg_bmi": 21.2, "avg_bp": 113},
                {"region": "Amhara", "age_group": "31-45", "gender": "Male", "patient_count": 550, "avg_bmi": 23.5, "avg_bp": 120},
                {"region": "Amhara", "age_group": "31-45", "gender": "Female", "patient_count": 580, "avg_bmi": 22.8, "avg_bp": 118},
                {"region": "Oromia", "age_group": "18-30", "gender": "Male", "patient_count": 890, "avg_bmi": 22.1, "avg_bp": 117},
                {"region": "Oromia", "age_group": "18-30", "gender": "Female", "patient_count": 930, "avg_bmi": 21.5, "avg_bp": 115},
                {"region": "Oromia", "age_group": "31-45", "gender": "Male", "patient_count": 720, "avg_bmi": 24.2, "avg_bp": 123},
                {"region": "Oromia", "age_group": "31-45", "gender": "Female", "patient_count": 680, "avg_bmi": 23.4, "avg_bp": 121},
                {"region": "SNNPR", "age_group": "18-30", "gender": "Male", "patient_count": 620, "avg_bmi": 21.5, "avg_bp": 116},
                {"region": "SNNPR", "age_group": "18-30", "gender": "Female", "patient_count": 670, "avg_bmi": 20.9, "avg_bp": 114},
                {"region": "SNNPR", "age_group": "31-45", "gender": "Male", "patient_count": 480, "avg_bmi": 23.1, "avg_bp": 121},
                {"region": "SNNPR", "age_group": "31-45", "gender": "Female", "patient_count": 520, "avg_bmi": 22.3, "avg_bp": 119},
                {"region": "Tigray", "age_group": "18-30", "gender": "Male", "patient_count": 420, "avg_bmi": 22.8, "avg_bp": 119},
                {"region": "Tigray", "age_group": "18-30", "gender": "Female", "patient_count": 460, "avg_bmi": 22.1, "avg_bp": 117},
                {"region": "Tigray", "age_group": "31-45", "gender": "Male", "patient_count": 350, "avg_bmi": 24.5, "avg_bp": 124},
                {"region": "Tigray", "age_group": "31-45", "gender": "Female", "patient_count": 320, "avg_bmi": 23.7, "avg_bp": 122},
                {"region": "Dire Dawa", "age_group": "18-30", "gender": "Male", "patient_count": 180, "avg_bmi": 23.2, "avg_bp": 118},
                {"region": "Dire Dawa", "age_group": "18-30", "gender": "Female", "patient_count": 210, "avg_bmi": 22.6, "avg_bp": 116},
                {"region": "Dire Dawa", "age_group": "31-45", "gender": "Male", "patient_count": 150, "avg_bmi": 24.8, "avg_bp": 123},
                {"region": "Dire Dawa", "age_group": "31-45", "gender": "Female", "patient_count": 140, "avg_bmi": 24.0, "avg_bp": 121}
            ]