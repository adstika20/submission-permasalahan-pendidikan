
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

# Fungsi untuk memastikan nilai berada dalam range yang benar
def clip_values(df):
    ranges = {
        'Marital_status': (1, 6),
        'Application_mode': (1, 57),
        'Application_order': (0, 9),
        'Course': (33, 9991),
        'Daytime_evening_attendance': (0, 1),
        'Previous_qualification': (1, 43),
        'Previous_qualification_grade': (-2.85, 4.35),
        'Nacionality': (1, 109),
        'Mothers_qualification': (1, 44),
        'Fathers_qualification': (1, 44),
        'Mothers_occupation': (0, 194),
        'Fathers_occupation': (0, 195),
        'Admission_grade': (-2.18, 4.37),
        'Displaced': (0, 1),
        'Educational_special_needs': (0, 1),
        'Debtor': (0, 1),
        'Tuition_fees_up_to_date': (0, 1),
        'Gender': (0, 1),
        'Scholarship_holder': (0, 1),
        'Age_at_enrollment': (17, 70),
        'International': (0, 1),
        'Curricular_units_1st_sem_credited': (0, 20),
        'Curricular_units_1st_sem_enrolled': (0, 26),
        'Curricular_units_1st_sem_evaluations': (0, 45),
        'Curricular_units_1st_sem_approved': (0, 26),
        'Curricular_units_1st_sem_grade': (-2.19, 1.64),
        'Curricular_units_1st_sem_without_evaluations': (0, 12),
        'Curricular_units_2nd_sem_credited': (0, 19),
        'Curricular_units_2nd_sem_enrolled': (0, 23),
        'Curricular_units_2nd_sem_evaluations': (0, 33),
        'Curricular_units_2nd_sem_approved': (0, 20),
        'Curricular_units_2nd_sem_grade': (-1.96, 1.60),
        'Curricular_units_2nd_sem_without_evaluations': (0, 12),
        'Unemployment_rate': (-1.47, 1.83),
        'Inflation_rate': (-0.89, 2.00),
        'GDP': (-1.94, 1.59)
    }
    for column, (min_val, max_val) in ranges.items():
        if column in df.columns:
            df[column] = df[column].clip(min_val, max_val)
    return df

# Input nilai variabel dari pengguna
st.subheader("Masukkan Nilai Variabel:")
user_inputs = {}
for variable in ranges.keys():
    user_inputs[variable] = st.number_input(f"{variable}:", min_value=ranges[variable][0], max_value=ranges[variable][1], value=(ranges[variable][0] + ranges[variable][1]) // 2)

# Clip nilai untuk memastikan berada dalam range yang valid
clipped_inputs = clip_values(user_inputs, ranges)

# Ubah input menjadi array untuk prediksi
X = np.array([list(clipped_inputs.values())])

# 3. Memuat model 
try:
    with open("gboost_model.pkl", "rb") as file:
        model = pickle.load(file)
    st.success("Model loaded successfully!")

    # 4. Prediksi dengan model
    if st.button("Predict"):
        prediction = model.predict(X)[0]
        result = {2: "Graduate", 0: "Dropout", 1: "Enrolled"}
        st.write(f"Prediction Result: {result[prediction]}")

except FileNotFoundError:
    st.error("Model file not found. Please train and save your model first.")
