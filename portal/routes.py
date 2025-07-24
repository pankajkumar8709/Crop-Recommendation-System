import pickle
import uuid
import numpy as np
from flask import render_template, request
from portal import app
import matplotlib.pyplot as plt

# Ensure the charts directory exists at app startup
import os
charts_dir = os.path.join('static', 'charts')
os.makedirs(charts_dir, exist_ok=True)


import os
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'model', 'crop_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)



import pandas as pd
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, '..', 'data', 'fertilizer_recommendation.csv')
fertilizer_data = pd.read_csv(csv_path)



def recommend_fertilizer(crop, current_n, current_p, current_k):
    row = fertilizer_data[fertilizer_data['Crop'].str.lower() == crop.lower()]
    if row.empty:
        return f"❌ Crop '{crop}' not found in fertilizer dataset."

    recommended_n = int(row['N'].values[0])
    recommended_p = int(row['P'].values[0])
    recommended_k = int(row['K'].values[0])

    result = []

    # Compare current values with recommended
    if current_n < recommended_n:
        result.append(f"Increase Nitrogen by {recommended_n - current_n} units.\n")
    elif current_n > recommended_n:
        result.append(f"Reduce Nitrogen by {current_n - recommended_n} units.\n")

    if current_p < recommended_p:
        result.append(f"Increase Phosphorus by {recommended_p - current_p} units.\n")
    elif current_p > recommended_p:
        result.append(f"Reduce Phosphorus by {current_p - recommended_p} units.\n")

    if current_k < recommended_k:
        result.append(f"Increase Potassium by {recommended_k - current_k} units.\n")
    elif current_k > recommended_k:
        result.append(f"Reduce Potassium by {current_k - recommended_k} units.\n")

    if not result:
        return "✅ Soil nutrients are optimal for this crop./n"
    return "Fertilizer Advice:\n" + "\n".join(result)
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/crop')
def index():
    return render_template("index.html")
    
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        import uuid
        import os
        import matplotlib.pyplot as plt
        import numpy as np

        # Get form data
        n = float(request.form['nitrogen'])
        p = float(request.form['phosphorus'])
        k = float(request.form['potassium'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Ensure chart directory exists
        chart_dir = os.path.join(app.root_path, 'portal', 'static', 'charts')
        os.makedirs(chart_dir, exist_ok=True)

        # === NPK Pie Chart ===
        npk_labels = ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)']
        npk_values = [n, p, k]
        npk_colors = ['#2E8B57', '#3CB371', '#1F6B47']

        npk_filename = f"npk_{uuid.uuid4().hex}.png"
        npk_path = os.path.join(chart_dir, npk_filename)

        plt.figure(figsize=(4, 4))
        plt.pie(npk_values, labels=npk_labels, colors=npk_colors, autopct='%1.1f%%', startangle=140)
        plt.title('Soil Nutrient Distribution')
        plt.tight_layout()
        plt.savefig(npk_path, transparent=True)
        plt.close()

        # === Weather Pie Chart ===
        weather_labels = ['Temperature (°C)', 'Humidity (%)', 'Rainfall (mm)']
        weather_values = [temp + 50, humidity, rainfall / 10]
        weather_colors = ['#4682B4', '#3A6D99', '#4B5EAA']

        weather_filename = f"weather_{uuid.uuid4().hex}.png"
        weather_path = os.path.join(chart_dir, weather_filename)

        plt.figure(figsize=(4, 4))
        plt.pie(weather_values, labels=weather_labels, colors=weather_colors, autopct='%1.1f%%', startangle=140)
        plt.title('Weather Conditions Distribution')
        plt.tight_layout()
        plt.savefig(weather_path, transparent=True)
        plt.close()

        # === Prediction & Fertilizer Suggestion ===
        data = np.array([[n, p, k, temp, humidity, ph, rainfall]], dtype=np.float32)
        try:
            prediction = model.predict(data)[0]
            fertilizer_advice = recommend_fertilizer(str(prediction).strip().lower(), n, p, k)
        except Exception as e:
            prediction = "Unknown"
            fertilizer_advice = f"❌ Error during prediction: {str(e)}"

        return render_template(
            "result.html",
            prediction_text=f"🌱 Suggested Crop: {prediction}",
            predicted_fertilizer=fertilizer_advice,
            npk_chart=f"/static/charts/{npk_filename}",
            weather_chart=f"/static/charts/{weather_filename}",
            request=request
        )

    


