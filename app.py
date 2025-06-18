from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

with open('bmi_model.pkl', 'rb') as f_in:
    model = pickle.load(f_in)

with open('scaler.pkl', 'rb') as f_out:
    scaler = pickle.load(f_out)
print("Expected features:", model.feature_names_in_)

def predict_status(config, model, scaler ):
    df = pd.DataFrame([config]) if isinstance(config, dict) else config
    df = scaler.transform(df)
    y_pred = model.predict(df)[0]
    if y_pred == 0:
        return 'Very Underweight'
    elif y_pred == 1:
        return 'Underweight'
    elif y_pred == 2:
        return 'Normal'
    elif y_pred == 3:
        return 'Overweight'
    elif y_pred == 4:
        return 'Obese'
    elif y_pred == 5:
        return 'Extreme Obesity'

print("Model expects features:", model.feature_names_in_)
@app.route("/predict", methods = ["POST"])
def predict():
    config = request.get_json()
    try:
        if not all(key in config for key in model.feature_names_in_):
            return jsonify({'error': 'missing or invalid input features'}), 400
        prediction = predict_status(config, model, scaler)
        return jsonify({"prediction":prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug = True, host = "0.0.0.0", port = 5000)
