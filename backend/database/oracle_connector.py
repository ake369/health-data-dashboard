import cx_Oracle
from config import Config
import pandas as pd

class OracleConnector:
    def __init__(self):
        self.config = Config.ORACLE_CONFIG
    
    def get_connection(self):
        return cx_Oracle.connect(**self.config)
    
    def get_disease_statistics(self):
        try:
            conn = self.get_connection()
            query = """
            SELECT 
                region,
                disease_type,
                diagnosis_year,
                COUNT(*) as case_count,
                AVG(treatment_cost) as avg_cost,
                AVG(recovery_days) as avg_recovery_days
            FROM disease_records 
            WHERE diagnosis_year >= EXTRACT(YEAR FROM SYSDATE) - 3
            GROUP BY region, disease_type, diagnosis_year
            ORDER BY region, diagnosis_year, disease_type
            """
            df = pd.read_sql(query, conn)
            conn.close()
            return df.to_dict('records')
        except Exception as e:
            print(f"Oracle Error: {e}")
            # Return sample data for demo with Ethiopian regions
            regions = ["Addis Ababa", "Amhara", "Oromia", "SNNPR", "Tigray", "Dire Dawa"]
            diseases = ["Malaria", "Respiratory", "Gastrointestinal", "Cardiovascular"]
            data = []
            
            for region in regions:
                for year in [2021, 2022, 2023]:
                    for disease in diseases:
                        # Regional variations in disease prevalence
                        base_cases = {
                            "Addis Ababa": {"Malaria": 25, "Respiratory": 45, "Gastrointestinal": 30, "Cardiovascular": 40},
                            "Amhara": {"Malaria": 65, "Respiratory": 35, "Gastrointestinal": 45, "Cardiovascular": 25},
                            "Oromia": {"Malaria": 70, "Respiratory": 40, "Gastrointestinal": 50, "Cardiovascular": 30},
                            "SNNPR": {"Malaria": 60, "Respiratory": 30, "Gastrointestinal": 40, "Cardiovascular": 20},
                            "Tigray": {"Malaria": 35, "Respiratory": 50, "Gastrointestinal": 35, "Cardiovascular": 35},
                            "Dire Dawa": {"Malaria": 45, "Respiratory": 35, "Gastrointestinal": 25, "Cardiovascular": 30}
                        }
                        
                        case_count = base_cases[region][disease] + (year - 2021) * 5
                        cost_factors = {"Malaria": 1200, "Respiratory": 800, "Gastrointestinal": 600, "Cardiovascular": 3500}
                        recovery_factors = {"Malaria": 14, "Respiratory": 10, "Gastrointestinal": 7, "Cardiovascular": 30}
                        
                        data.append({
                            "region": region,
                            "disease_type": disease,
                            "diagnosis_year": year,
                            "case_count": case_count,
                            "avg_cost": cost_factors[disease] * (1.1 if region in ["Addis Ababa", "Dire Dawa"] else 0.9),
                            "avg_recovery_days": recovery_factors[disease] * (0.9 if region == "Addis Ababa" else 1.1)
                        })
            return data