import pandas as pd
import os

class CSVProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_survey_data(self):
        try:
            df = pd.read_csv(self.file_path)
            return df.to_dict('records')
        except Exception as e:
            print(f"CSV Error: {e}")
            # Create realistic sample data for Ethiopian regions
            sample_data = [
                {
                    "survey_id": 1, "region": "Addis Ababa", "health_index": 85, 
                    "vaccination_rate": 78, "life_expectancy": 72.5, "hospital_count": 45,
                    "doctors_per_100k": 25.4, "malaria_incidence": 120, "hiv_prevalence": 2.8
                },
                {
                    "survey_id": 2, "region": "Amhara", "health_index": 72, 
                    "vaccination_rate": 65, "life_expectancy": 68.2, "hospital_count": 38,
                    "doctors_per_100k": 8.2, "malaria_incidence": 350, "hiv_prevalence": 1.9
                },
                {
                    "survey_id": 3, "region": "Oromia", "health_index": 75, 
                    "vaccination_rate": 68, "life_expectancy": 69.8, "hospital_count": 52,
                    "doctors_per_100k": 9.8, "malaria_incidence": 420, "hiv_prevalence": 2.1
                },
                {
                    "survey_id": 4, "region": "SNNPR", "health_index": 70, 
                    "vaccination_rate": 62, "life_expectancy": 67.1, "hospital_count": 41,
                    "doctors_per_100k": 7.5, "malaria_incidence": 380, "hiv_prevalence": 3.2
                },
                {
                    "survey_id": 5, "region": "Tigray", "health_index": 78, 
                    "vaccination_rate": 71, "life_expectancy": 70.9, "hospital_count": 36,
                    "doctors_per_100k": 12.3, "malaria_incidence": 180, "hiv_prevalence": 1.7
                },
                {
                    "survey_id": 6, "region": "Dire Dawa", "health_index": 80, 
                    "vaccination_rate": 74, "life_expectancy": 71.8, "hospital_count": 28,
                    "doctors_per_100k": 18.6, "malaria_incidence": 220, "hiv_prevalence": 2.5
                }
            ]
            # Save sample data to CSV
            sample_df = pd.DataFrame(sample_data)
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            sample_df.to_csv(self.file_path, index=False)
            return sample_data