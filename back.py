import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
# Load your machine learning model from a .pkl file using pickle
with open('D:/Bankify/trained_model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('input.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        gender = float(request.form['gender'])
        married = float(request.form['married'])
        dependents = float(request.form['dependents'])
        education = float(request.form['education'])
        self_employed = float(request.form['self_employed'])
        applicant_income = float(request.form['applicant_income'])
        coapplicant_income = float(request.form['coapplicant_income'])
        loan_amount = float(request.form['loan_amount'])
        loan_amount_term = float(request.form['loan_amount_term'])
        credit_history = float(request.form['credit_history'])
        property_area = float(request.form['property_area'])

        # Create a dictionary with the input data
        input_data = {
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self_Employed': self_employed,
            'ApplicantIncome': applicant_income,
            'CoapplicantIncome': coapplicant_income,
            'LoanAmount': loan_amount,
            'Loan_Amount_Term': loan_amount_term,
            'Credit_History': credit_history,
            'Property_Area': property_area
        }

        # Make a prediction using the model
        prediction = model.predict([list(input_data.values())])

        # Convert the prediction to a user-friendly message
        if prediction[0] == 1:
            result = "Approved"
        else:
            result = "Not Approved"

        return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
# app.run()
