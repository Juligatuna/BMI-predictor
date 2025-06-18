# 🧮 BMI Weight Status Predictor

This is a simple Flask web application that predicts a person's weight status (e.g., Normal, Overweight, Obese) using a machine learning model. Users input their gender, height (cm), and weight (kgs) through a browser interface.

## 🚀 Features
- Web interface built with HTML and JavaScript  
- Flask-based backend for model prediction  
- Uses a pre-trained machine learning model (`bmi_model.pkl`)  
- Scales input with `scaler.pkl`  
- Predicts categories including:  
  - Very Underweight  
  - Underweight  
  - Normal  
  - Overweight  
  - Obese  
  - Extreme Obesity  

## 📂 Project Structure

BMI_Model/
├── app.py # Flask application
├── bmi_model.pkl # Trained ML model
├── scaler.pkl # Pre-fitted scaler
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # HTML frontend
└── README.md # This file


## ⚙️ How to Run Locally

 1. Clone the repo  
   ```bash
   git clone https://github.com/Juligatuna/BMI-predictor.git
   cd BMI-predictor

## Create a virtual environment (recommended)

python -m venv venv
Activate the virtual environment:

## Windows:

venv\Scripts\activate

## macOS/Linux:

source venv/bin/activate

## Install dependencies

pip install -r requirements.txt

## Run the Flask app

python app.py

## Open your browser and go to:

http://127.0.0.1:5000