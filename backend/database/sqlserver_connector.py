import pyodbc
from config import Config
import pandas as pd

class SQLServerConnector:
    def __init__(self):
        self.config = Config.SQL_SERVER_CONFIG
    
    def get_connection(self):
        connection_string = (
            f"DRIVER={self.config['driver']};"
            f"SERVER={self.config['server']};"
            f"DATABASE={self.config['database']};"
            f"UID={self.config['username']};"
            f"PWD={self.config['password']}"
        )
        return pyodbc.connect(connection_string)
    
    def get_hospital_metrics(self):
        try:
            conn = self.get_connection()
            query = """
            SELECT 
                region,
                department,
                month,
                patient_volume,
                avg_wait_time,
                satisfaction_score,
                readmission_rate
            FROM hospital_performance 
            WHERE month >= DATEADD(MONTH, -6, GETDATE())
            ORDER BY region, month, department
            """
            df = pd.read_sql(query, conn)
            conn.close()
            return df.to_dict('records')
        except Exception as e:
            print(f"SQL Server Error: {e}")
            # Return sample data for demo with Ethiopian regions
            regions = ["Addis Ababa", "Amhara", "Oromia", "SNNPR", "Tigray", "Dire Dawa"]
            departments = ["Emergency", "Pediatrics", "Maternity", "General Medicine"]
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
            data = []
            
            for region in regions:
                for i, month in enumerate(months):
                    for department in departments:
                        # Regional performance variations
                        base_volume = {
                            "Addis Ababa": 1200, "Amhara": 800, "Oromia": 950, 
                            "SNNPR": 700, "Tigray": 600, "Dire Dawa": 400
                        }
                        
                        volume_factor = {
                            "Emergency": 1.2, "Pediatrics": 0.8, 
                            "Maternity": 0.9, "General Medicine": 1.1
                        }
                        
                        wait_time_base = {
                            "Addis Ababa": 35, "Amhara": 50, "Oromia": 45,
                            "SNNPR": 55, "Tigray": 40, "Dire Dawa": 38
                        }
                        
                        satisfaction_base = {
                            "Addis Ababa": 4.2, "Amhara": 3.8, "Oromia": 4.0,
                            "SNNPR": 3.7, "Tigray": 4.1, "Dire Dawa": 4.0
                        }
                        
                        data.append({
                            "region": region,
                            "department": department,
                            "month": f"2023-{month}",
                            "patient_volume": int(base_volume[region] * volume_factor[department] * (1 + i * 0.1)),
                            "avg_wait_time": wait_time_base[region] * (0.9 if department == "General Medicine" else 1.1),
                            "satisfaction_score": round(satisfaction_base[region] + (0.1 if department == "Pediatrics" else 0), 1),
                            "readmission_rate": round(8.5 - (i * 0.5) - (0.5 if region == "Addis Ababa" else 0), 1)
                        })
            return data