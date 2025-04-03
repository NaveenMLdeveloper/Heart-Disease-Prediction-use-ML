from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model_path = r"D:\AI&ML Only\ML\Heart diseases\best_model.pkl"
model = joblib.load(model_path)

# Load the scaler fitted on the training data
scaler_path = r"D:\AI&ML Only\ML\Heart diseases\scaler.pkl"
scaler = joblib.load(scaler_path)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Convert JSON to DataFrame
        input_data = pd.DataFrame([data])
        
        # Columns order based on the trained model
        input_data = input_data[['age', 'sex', 'chest pain type', 'resting bp s', 'cholesterol', 
                                 'fasting blood sugar', 'resting ecg', 'max heart rate', 
                                 'exercise angina', 'oldpeak', 'ST slope']]
        
        # Preprocess the data (scaling using the fitted scaler)
        input_data_preprocessed = scaler.transform(input_data)
        
        # Make predictions
        predictions = model.predict(input_data_preprocessed)
        
        # Return the predictions as JSON
        return jsonify({'predictions': int(predictions[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
