from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

# test results page data
patient_info = {
    'name': 'John Doe',
    'age': 23,
    'gender': 'M',
    'test_date': '2023-10-05',
    'test_results': [
        {
            'Test_name': 'Complete Blood Count',
            'Result': '13.4 g/dL',
            'Normal Range': '12.0–16.0 g/dL'
        },
        {
            'Test_name': 'Cholesterol (Total)',
            'Result': '190 mg/dL',
            'Normal Range': '< 200 mg/dL'
        },
        {
            'Test_name': 'Blood Glucose (Fasting)',
            'Result': '95 mg/dL',
            'Normal Range': '70–99 mg/dL'
        }
    ]
}

# perscriptions info page data
medication_info = {
    'Current Medications': [
        {
            'Medication_Name': 'Lisinopril',
            'dosage': '10 mg',
            'Instructions': 'Take once daily',
            'Perscribed By': 'Dr. Smith'
        },
        {
            'Medication_Name': 'Metformin',
            'Instructions': 'Take twice daily with meals',
            'Perscribed By': 'Dr. Patel'
        },
        {
            'Medication_Name': 'Atorvastatin',
            'Instructions': 'Take once daily at bedtime',
            'Perscribed By': 'Dr. Lee'
        }
    ],

    'Previous Medications': [
        {
            'Medication_Name': 'Amoxicillin',
            'dosage': '500 mg',
            'Instructions': 'Take three times daily for 7 days',
            'Perscribed By': 'Dr. Brown',
            'Status': 'Completed'
        },
        {
            'Medication_Name': 'Ibuprofen',
            'dosage': '200 mg',
            'Instructions': 'Take as needed for pain',
            'Perscribed By': 'Dr. Green',
            'Status': 'Discontinued'
        },
        {
            'Medication_Name': 'Omeprazole',
            'dosage': '20 mg',
            'Instructions': 'Take once daily before breakfast',
            'Perscribed By': 'Dr. White',
            'Status': 'Completed'

        }
    ]
}

# Billing info page data
Current_billing_info = {
    'Current billing summary': [
        {
            'Date': '2025-10-01',
            'Description': 'Office Visit',
            'Amount': '$150.00',
            'Status': 'Unpaid'
        },
        {
            'Date': '2025-10-08',
            'Description': 'Office Visit',
            'Amount': '$85.00',
            'Status': 'Unpaid'
        }
    ],

    'Payment History': [
        {
            'Date': '2025-09-15',
            'Payment Method': 'Credit Card - Visa',
            'Amount': '$120.00',
            'Status': 'Paid'
        },
        {
            'Date': '2025-09-22',
            'Payment Method': 'Insurance',
            'Amount': '$200.00',
            'Status': 'Paid'
        }
    ]

}


# App routes
@app.route('/get_patient_info')
def load_test_results():
    print('Load Patient Info')
    return patient_info

@app.route('/get_medication_info')
def load_medication_info():
    print('Load Medication Info')
    return medication_info

@app.route('/get_billing_info')
def load_billing_info():
    print('Load Billing Info')
    return Current_billing_info




if __name__ == '__main__':
    app.run(debug=True)