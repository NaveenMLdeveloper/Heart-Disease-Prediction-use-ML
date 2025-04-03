# ❤️ Heart Disease Prediction Using Machine Learning

## 📝 Objective
This project aims to predict the likelihood of heart disease based on patient data using machine learning models. The dataset, sourced from Kaggle, includes various medical attributes that help assess cardiovascular health risks.

## 📂 Dataset
The dataset contains the following features:
- 👤 **Age** - Patient's age
- ⚧️ **Sex** - Gender of the patient
- ❤️ **Chest Pain Type** - Types of chest pain experienced
- ⏱️ **Resting Blood Pressure** - Blood pressure during rest
- 🩸 **Cholesterol** - Cholesterol levels
- 💓 **Fasting Blood Sugar** - Blood sugar levels after fasting
- 📈 **Resting ECG** - Electrocardiogram results
- 🏃 **Max Heart Rate** - Maximum achieved heart rate
- 🩺 **Exercise-Induced Angina** - Chest pain during physical activity
- 🩸 **ST Depression** - Depression of ST segment in ECG
- 📊 **Slope of ST Segment** - Slope of peak exercise ST segment
- 🩻 **Number of Major Vessels** - Number of major vessels colored by fluoroscopy
- 🏥 **Thalassemia** - Blood disorder type
- ✅ **Target** - 0 (No Heart Disease) / 1 (Heart Disease) [Target Variable]

## 🚀 Steps Involved
1️⃣ **Data Collection & Preprocessing:**
   - Load and explore the dataset
   - Handle missing values and perform feature selection
   - Encode categorical features and standardize numerical values

2️⃣ **Data Splitting:**
   - Split the dataset into training and testing sets
   - Save test data for manual testing

3️⃣ **Model Building & Training:**
   - Train various ML models (Logistic Regression, Random Forest, SVM, etc.)
   - Evaluate models using accuracy, precision, recall, and F1-score

4️⃣ **Model Selection:**
   - Choose the best-performing model based on evaluation metrics
   - Save the trained model as `.pkl` for future use

5️⃣ **Manual Testing:**
   - Load the saved model
   - Preprocess new patient data and make predictions

6️⃣ **API Integration (Flask Web App):**
   - Build a simple web interface using Flask
   - Allow users to input medical details and get heart disease predictions

## 🛠️ Technologies Used
- 🐍 **Python**
- 🤖 **Scikit-learn**
- 🔢 **Pandas & NumPy**
- 📊 **Matplotlib & Seaborn**
- 🌐 **Flask (for web app integration)**
- 🏗️ **Machine Learning Algorithms**

## ⚙️ Installation & Setup
### Prerequisites
Ensure you have Python installed and install dependencies:
```sh
pip install -r requirements.txt
```

### ▶️ Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction
   ```
2. Run the Jupyter Notebook for model training:
   ```sh
   jupyter notebook Heart.ipynb
   ```
3. Run the Flask web app (if integrated):
   ```sh
   python app.py
   ```



