# 🩺 Diabetes Prediction Machine Learning App

An interactive, end-to-end machine learning web application that predicts the likelihood of a patient having diabetes based on clinical diagnostic measurements. 

## 🎯 Project Overview
This project utilizes a Support Vector Machine (SVM) classifier to provide real-time risk assessments. It features a complete data pipeline, from data standardization using `StandardScaler` to a user-friendly frontend interface built with Streamlit.

## 📊 Dataset
The model is trained on the **PIMA Indians Diabetes Database**. It analyzes 8 specific medical predictor variables to determine the binary outcome (Diabetic / Non-Diabetic):
* **Pregnancies:** Number of times pregnant
* **Glucose:** Plasma glucose concentration 
* **Blood Pressure:** Diastolic blood pressure (mm Hg)
* **Skin Thickness:** Triceps skinfold thickness (mm)
* **Insulin:** 2-Hour serum insulin (mu U/ml)
* **BMI:** Body mass index (weight in kg/(height in m)^2)
* **DPF:** Diabetes Pedigree Function (genetic risk score)
* **Age:** Age in years

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-learn (SVM)
* **Data Processing:** Pandas, NumPy
* **Frontend Framework:** Streamlit
* **Serialization:** Pickle

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/lakshayaAswal/Diabetes-Prediction.git](https://github.com/lakshayaAswal/Diabetes-Prediction.git)