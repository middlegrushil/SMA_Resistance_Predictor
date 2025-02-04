# SMA_Resistance_Predictor
**📌 Theoretical Explanation of the SMA Electrical Resistance Predictor**

### **Introduction**
This project aims to predict the **electrical resistance** of **Shape Memory Alloy (SMA) wires** based on key factors such as **temperature, applied stress, and phase fraction**. The integration of **machine learning, web technologies, and data processing** allows for real-time predictions, making it valuable for research and industrial applications.

---

## **1️⃣ Machine Learning Model (Training & Prediction)**

### **📌 Concept**
The electrical resistance of SMA wires is influenced by:
- **Temperature (°C)** – Determines phase transformation between Martensite and Austenite.
- **Stress (MPa)** – External force affects phase transition and resistance.
- **Phase Fraction** – Represents the fraction of material in the Austenitic phase.

A **Random Forest Regressor** is trained on synthetic data generated based on these parameters. The model learns the relationships and can predict resistance for new input values.

### **📌 Workflow**
1. **Synthetic Data Generation:** The dataset is created using simplified physics-based equations incorporating temperature, stress, and phase fraction.
2. **Model Training:** The dataset is split into training and testing sets, and a **Random Forest Regressor** is trained to map input features to electrical resistance.
3. **Model Evaluation:** Performance is measured using **Mean Squared Error (MSE)** and **R² score**.
4. **Model Storage:** The trained model is saved as `sma_rf_model.pkl` for later use in the backend.

---

## **2️⃣ Backend (Flask API - Model Deployment)**

### **📌 Concept**
The backend acts as a bridge between the machine learning model and the user interface. It:
- Loads the pre-trained **Random Forest** model.
- Accepts **user inputs** via API requests.
- Passes inputs to the **model** for prediction.
- Returns the **predicted resistance value** in JSON format.

### **📌 Workflow**
1. **Flask API Setup:** Flask is used to create an API endpoint (`/predict`).
2. **Model Integration:** The API loads the pre-trained model (`sma_rf_model.pkl`).
3. **User Input Handling:** The API accepts temperature, stress, and phase fraction as JSON data.
4. **Prediction Process:** The model processes input values and returns predicted resistance.
5. **API Response:** The result is sent back to the frontend in JSON format.

---

## **3️⃣ Frontend (Streamlit UI - User Interaction)**

### **📌 Concept**
A **Streamlit-based graphical user interface (GUI)** enables users to input parameters and get real-time predictions.

### **📌 Workflow**
1. **User Input Collection:** Users enter values for **Temperature, Stress, and Phase Fraction**.
2. **API Communication:** The frontend sends data to the Flask API using **HTTP requests**.
3. **Result Display:** The response (predicted resistance) is displayed in the UI.
4. **Error Handling:** Ensures users receive appropriate messages if the API is down or incorrect inputs are provided.

---

## **📌 How the System Works Together**
1. **User enters values** in the **Streamlit UI**.
2. **Streamlit sends input data** to the **Flask API**.
3. **Flask API forwards the input** to the **trained ML model**.
4. **ML model predicts electrical resistance** and returns the result.
5. **Flask sends the result** back to **Streamlit UI**.
6. **Streamlit displays the predicted resistance (Ω) to the user**.

---

## **🚀 Summary & Applications**
✔ **Machine Learning Model:** Learns relationships between SMA parameters and resistance.
✔ **Flask API:** Deploys the trained model and serves predictions.
✔ **Streamlit UI:** Provides an interactive interface for users to enter inputs and view results.

### **Applications:**
- **Material Science Research:** Predicting resistance of SMA materials in different conditions.
- **Robotics & Aerospace:** Optimizing SMA-based actuators.
- **Biomedical Devices:** Designing SMA-based prosthetics with adaptive electrical properties.

This is a **fully functional ML-powered web app** for **SMA resistance prediction**, integrating **machine learning, web APIs, and user-friendly UI**! 🚀😎

