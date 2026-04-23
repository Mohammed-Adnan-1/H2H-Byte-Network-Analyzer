# 🚀 AURA-X WiFi Intelligence Engine

## 📌 Overview

AURA-X is an AI-powered WiFi analysis system that detects network issues, identifies root causes, and provides solutions to improve user experience (QoE).

Instead of showing only technical data, AURA-X explains problems in a simple and understandable way.

---

## 🎯 Problem Statement

Most WiFi tools:

* Show raw metrics (latency, signal strength)
* Do not explain the actual problem
* Do not suggest fixes
* Are difficult for normal users to understand

---

## 💡 Our Solution

AURA-X:

* Collects WiFi metrics (latency, packet loss, signal strength)
* Processes data using intelligent logic
* Detects root causes of issues
* Suggests solutions
* Displays results in a modern dashboard

---

## 🧠 Key Features

* 📊 Real-time WiFi analysis
* 🎯 QoE (Quality of Experience) classification
* 🔍 Root cause detection
* 💡 Smart recommendations
* 📈 Graph visualization
* 🎨 Modern UI dashboard

---

## 🏗️ System Architecture

Client (Frontend UI)
↓
Flask Backend API
↓
Processing Engine
↓
QoE + Root Cause + Recommendation
↓
Dashboard Output

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Backend

* Python
* Flask
* Flask-CORS

### Database

* SQLite

---

## 📂 Project Structure

aura-x-wifi-analyzer/

frontend/

* dashboard.html
* app.js
* styles.css

backend/

* app.py
* routes.py
* database.py

core/

* normalization.py
* feature_engineering.py
* root_cause_engine.py
* qoe_engine.py
* recommendation_engine.py

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

pip install flask flask-cors scikit-learn pandas joblib pyyaml

---

### 2. Run Backend

python -m backend.app

---

### 3. Open Frontend

Open this file in browser:
frontend/dashboard.html

---

## 🚀 How It Works

1. User clicks "Analyze Network"
2. Data is sent to backend
3. Backend processes:

   * Normalization
   * Feature extraction
   * Root cause detection
   * QoE calculation
4. Results are returned
5. UI displays results and graph

---

## 📊 Sample Output

QoE: Poor
Root Cause: Distance from router
Recommendation: Move closer to router
Explanation: Weak signal and packet loss detected

---

## 🔥 Unique Points

* Focus on QoE instead of raw data
* Gives explanation + solution
* Easy to understand UI
* Modular design

---

## 🚀 Future Improvements

* Machine Learning integration
* Real WiFi data collection
* Mobile app version
* Cloud deployment

---

## 👨‍💻 Author

Mohammed Adnan and Nithya U

---

## 🏆 Conclusion

AURA-X converts complex WiFi data into simple insights and helps users fix network issues easily.
