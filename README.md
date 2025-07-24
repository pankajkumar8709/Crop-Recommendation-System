Team(SC1)_5

Team Members: 
Pankaj Kumar Mahto (Rollno: 24CSE394) (Regd No : 24UG010451)
Hemalatanaram  (Roll no : 24BCA070)  (Regd No: 24UG040070)
Jada. Leela Prasanth (Roll No: 24CSE394 ) (Regd No: 24UG010179)



# 🌱 Data-Driven Crop Advisory System

An AI-powered decision support system for small farm holders that recommends the most suitable crops and fertilizers based on soil and environmental conditions.

---

# Table of Contents

 Project Overview
 Features
 Tech Stack
 Input Parameters
 How It Works
 Directory Structure
 Sample Data
 Future Scope
 Contact

---

# Project Overview

The Data-Driven Crop Advisory System is a smart web-based tool designed to help farmers choose the best crop to grow and the right fertilizer to use, based on:

- Soil nutrients: Nitrogen (N), Phosphorus (P), Potassium (K)
- Soil pH level
- Weather: Temperature, Humidity, Rainfall

Using machine learning, it delivers personalized recommendations that promote better yield and sustainable farming.


# Features

 Crop recommendation using ML
 Fertilizer advisory based on NPK levels
 User-friendly Flask web interface
 Environmental parameter input via form
 Data visualizations (charts)
 Local and offline-capable

---

# Tech Stack

| Category      | Tools / Languages        

 Frontend       HTML, CSS, JavaScript     
 Backend        Python, Flask             
 ML/AI          scikit-learn, pandas      
 Database       SQLite, CSV               
 Visualization  Matplotlib                  


# Input Parameters

N: Nitrogen content (kg/ha)
P:Phosphorus content (kg/ha)
K: Potassium content (kg/ha)
pH: Soil pH level
Temperature**: (°C)
Humidity: (%)
Rainfall: (mm)

# How It Works

1. User enters soil data and weather data.
2. ML model predicts the best-suited crop.
3. Based on selected crop and NPK levels, a fertilizer is recommended.
4. Results are visualized using charts.




# Directory
CROP_RECOMMENDATION/
│
├── data/                           # CSV files for crop & fertilizer
│   ├── Crop_recommendation.csv
│   └── fertilizer_recommendation.csv
│
├── myenv/                          # Virtual environment (optional to track)
│
├── notebooks/
│   └── model_training.ipynb        # Jupyter notebook for training ML model
│
├── portal/                         # Flask application
│   ├── __pycache__/
│   ├── model/
│   │   └── crop_model.pkl          # Trained ML model
│   ├── portal/
│   │   ├── __init__.py
│   │   └── routes.py               # Main Flask routes
│   ├── templates/                  # HTML templates
│   │   ├── home.html
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│       └── charts/                 # JS/CSS/chart assets
│
|                        
│
├── .gitignore                      # Git ignore file
├── README.md                       # Project README
├── requirements.txt                # Python dependencies
└── run.py                          # App entry point


# Sample Data

	N	P	K	temperature	humidity	ph	rainfall	label
0	90	42	43	20.879744	82.002744	6.502985	202.935536	rice
1	85	58	41	21.770462	80.319644	7.038096	226.655537	rice
2	60	55	44	23.004459	82.320763	7.840207	263.964248	rice
3	74	35	40	26.491096	80.158363	6.980401	242.864034	rice
4	78	42	42	20.130175	81.604873	7.628473	262.717340	rice
...	...	...	...	...	...	...	...	...
2195	107	34	32	26.774637	66.413269	6.780064	177.774507	coffee
2196	99	15	27	27.417112	56.636362	6.086922	127.924610	coffee


# Future Scope
. Real-Time Weather API Integration

Fetch live weather data (temperature, humidity, rainfall) using APIs (like OpenWeatherMap, WeatherStack).
Automatically fill weather fields to reduce manual input and increase accuracy.

. IoT-Based Soil Sensor Integration

Connect physical sensors to fetch real-time soil NPK, moisture, and pH data.
Use Raspberry Pi or Arduino to send data directly to your app.

.Farmer Feedback Loop

Let users rate crop recommendations or suggest corrections.
Use feedback to retrain models and improve over time.


# Contact

Pankaj Kumar Mahto 
Phone: 6201511552
Email: 24cse394.pankajkumarmahto@giet.edu