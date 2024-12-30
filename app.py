
# 1. Library
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
# gradientboost
from sklearn.ensemble import GradientBoostingClassifier
#metric
import pickle


# 2. Judul dan deskripsi aplikasi
st.title("Menyelesaikan Permasalahan Institusi Pendidikan")
st.write("Aplikasi ini menggunakan model Gradient Boosting untuk prediksi Permasalahan Institusi Pendidikan.")

# 3. File uploader untuk dataset
uploaded_file = st.file_uploader("dataset_standarized.csv", type=["csv"])

if uploaded_file is not None:
    if uploaded_file.name != "dataset_standarized.csv":
        st.error("Please upload a file named 'dataset_standarized.csv'")
    else:
        data = pd.read_csv(uploaded_file)
        st.write("Dataset preview:")
        st.write(data.head())

    # 4. Validasi dataset
    required_columns = [
        'Marital_status', 'Application_mode', 'Application_order', 'Course',
        'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
        'Nacionality', 'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation',
        'Fathers_occupation', 'Admission_grade', 'Displaced', 'Educational_special_needs',
        'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'Age_at_enrollment',
        'International', 'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
        'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
        'Unemployment_rate', 'Inflation_rate', 'GDP'
        ]  # Ganti sesuai dengan kolom dataset Anda
    if all(col in data.columns for col in required_columns):
        X = data[required_columns]
        # Menangani missing values
        X = X.fillna(0)  # Atau gunakan dropna() sesuai kebutuhan

    else:
        st.error(f"Dataset must contain columns: {', '.join(required_columns)}")

    # 5. Memuat model 
    try:
        with open("gboost_model.pkl", "rb") as file:
            model = pickle.load(file)
        st.success("Model loaded successfully!")

        # 6. Prediksi dengan model
        if st.button("Predict"):
            predictions = model.predict(X)
            st.write("Predictions:")
            st.write(predictions)

    except FileNotFoundError:
        st.error("Model file not found. Please train and save your model first.")


