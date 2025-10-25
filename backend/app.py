from flask import Flask, jsonify
from flask_cors import CORS
from database.mysql_connector import MySQLConnector
from database.oracle_connector import OracleConnector
from database.sqlserver_connector import SQLServerConnector
from database.data_processor import CSVProcessor
import os

app = Flask(__name__)
CORS(app)

# Initialize connectors
mysql_connector = MySQLConnector()
oracle_connector = OracleConnector()
sqlserver_connector = SQLServerConnector()
csv_processor = CSVProcessor('sample_data/health_survey_data.csv')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Health Data API is running"})

@app.route('/api/data/mysql/demographics', methods=['GET'])
def get_mysql_data():
    data = mysql_connector.get_patient_demographics()
    return jsonify({
        "source": "MySQL",
        "data": data,
        "record_count": len(data)
    })

@app.route('/api/data/oracle/diseases', methods=['GET'])
def get_oracle_data():
    data = oracle_connector.get_disease_statistics()
    return jsonify({
        "source": "Oracle",
        "data": data,
        "record_count": len(data)
    })

@app.route('/api/data/sqlserver/performance', methods=['GET'])
def get_sqlserver_data():
    data = sqlserver_connector.get_hospital_metrics()
    return jsonify({
        "source": "SQL Server",
        "data": data,
        "record_count": len(data)
    })

@app.route('/api/data/csv/survey', methods=['GET'])
def get_csv_data():
    data = csv_processor.load_survey_data()
    return jsonify({
        "source": "CSV File",
        "data": data,
        "record_count": len(data)
    })

@app.route('/api/data/consolidated', methods=['GET'])
def get_all_data():
    """Consolidate data from all sources"""
    mysql_data = mysql_connector.get_patient_demographics()
    oracle_data = oracle_connector.get_disease_statistics()
    sqlserver_data = sqlserver_connector.get_hospital_metrics()
    csv_data = csv_processor.load_survey_data()
    
    consolidated = {
        "demographics": mysql_data,
        "disease_stats": oracle_data,
        "hospital_metrics": sqlserver_data,
        "survey_data": csv_data,
        "summary": {
            "total_patients": sum(item['patient_count'] for item in mysql_data),
            "total_cases": sum(item['case_count'] for item in oracle_data),
            "total_surveys": len(csv_data)
        }
    }
    return jsonify(consolidated)

if __name__ == '__main__':
    # Create sample data directory
    os.makedirs('sample_data', exist_ok=True)
    app.run(debug=True, port=5000)