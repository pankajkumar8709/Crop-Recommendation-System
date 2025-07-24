# 🌱 Data-Driven Crop Advisory System

An AI-powered decision support system for small farm holders that recommends the most suitable crops and fertilizers based on soil and environmental conditions.

---

## 👥 Team (SC1)_5

- **Pankaj Kumar Mahto**  
  Roll No: 24CSE394 | Regd No: 24UG010451  
- **Hemalatanaram**  
  Roll No: 24BCA070 | Regd No: 24UG040070  
- **Jada Leela Prasanth**  
  Roll No: 24CSE394 | Regd No: 24UG010179  

---

## 📌 Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Input Parameters](#input-parameters)  
- [How It Works](#how-it-works)  
- [Directory Structure](#directory-structure)  
- [Sample Data](#sample-data)  
- [Future Scope](#future-scope)  
- [Contact](#contact)  

---

## 📖 Project Overview

The **Data-Driven Crop Advisory System** helps farmers choose the best crop and suitable fertilizer based on:

- 🌾 Soil Nutrients (N, P, K)  
- 🧪 Soil pH  
- 🌤️ Temperature, Humidity, Rainfall  

Using machine learning, it delivers accurate and personalized recommendations for sustainable farming.

---

## 🚀 Features

- ✅ Crop recommendation using ML  
- ✅ Fertilizer advisory based on NPK levels  
- ✅ User-friendly Flask web interface  
- ✅ Data visualizations (charts)  
- ✅ Local/offline-capable system  

---

## 🧰 Tech Stack

| Category     | Tools/Technologies         |
|-------------|-----------------------------|
| Frontend     | HTML, CSS, JavaScript       |
| Backend      | Python, Flask               |
| ML/AI        | scikit-learn, pandas        |
| Database     | SQLite, CSV                 |
| Visualization| Matplotlib                  |

---

## 🧪 Input Parameters

- **N**: Nitrogen (kg/ha)  
- **P**: Phosphorus (kg/ha)  
- **K**: Potassium (kg/ha)  
- **pH**: Soil pH  
- **Temperature**: in °C  
- **Humidity**: in %  
- **Rainfall**: in mm  

---

## 🔄 How It Works

1. User enters soil and weather data  
2. ML model predicts best crop  
3. Fertilizer recommendation based on crop and NPK  
4. Results shown using charts  

---

## 📁 Directory Structure

CROP_RECOMMENDATION/
│
├── data/
│ ├── Crop_recommendation.csv
│ └── fertilizer_recommendation.csv
│
├── myenv/ # (Virtual environment - optional)
│
├── notebooks/
│ └── model_training.ipynb
│
├── portal/
│ ├── model/
│ │ └── crop_model.pkl
│ ├── portal/
│ │ └── routes.py
│ ├── templates/
│ │ ├── index.html
│ │ └── result.html
│ └── static/
│ └── charts/
│
├── .gitignore
├── requirements.txt
├── README.md
└── run.py

----

## 📊 Sample Data

| N  | P  | K  | Temp (°C) | Humidity (%) | pH  | Rainfall (mm) | Label |
|----|----|----|-----------|---------------|-----|----------------|--------|
| 90 | 42 | 43 | 20.87     | 82.00         | 6.50| 202.93         | rice   |
| 85 | 58 | 41 | 21.77     | 80.31         | 7.03| 226.65         | rice   |
| 60 | 55 | 44 | 23.00     | 82.32         | 7.84| 263.96         | rice   |
| 74 | 35 | 40 | 26.49     | 80.15         | 6.98| 242.86         | rice   |

---

## 🔮 Future Scope

- 🔗 **Real-Time Weather API Integration**  
  Use APIs like OpenWeatherMap to fetch live weather data.

- 🌱 **IoT-Based Soil Sensor Integration**  
  Connect sensors (Raspberry Pi, Arduino) for real-time NPK, moisture, and pH.

- 💬 **Farmer Feedback Loop**  
  Collect feedback to improve model performance via retraining.

---

## 📞 Contact

**Pankaj Kumar Mahto**  
📱 6201511552  
📧 24cse394.pankajkumarmahto@giet.edu  
