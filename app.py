# 1. Library
import streamlit as st
import numpy as np
import pickle

# 2. Judul dan Deskripsi Aplikasi dengan Emoji
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟 Prediksi Status Mahasiswa 🌟</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style="text-align: center; font-size: 18px; color: #555;">
    Aplikasi ini menggunakan model <b>Gradient Boosting</b> untuk memprediksi status mahasiswa:
    <span style="color: green;">Graduate 🎓</span>, 
    <span style="color: red;">Dropout ❌</span>, atau 
    <span style="color: blue;">Enrolled 📘</span>.
    </p>
    """, unsafe_allow_html=True
)

# Fungsi untuk memastikan nilai berada dalam range yang benar
def clip_values(values, ranges):
    clipped_values = {}
    for column, (min_val, max_val) in ranges.items():
        if column in values:
            clipped_values[column] = np.clip(values[column], min_val, max_val)
    return clipped_values

# Range untuk setiap variabel
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

# Input nilai variabel dari pengguna
st.markdown("### 🔢 Masukkan Nilai Variabel:")
user_inputs = {}
for variable in ranges.keys():
    user_inputs[variable] = st.number_input(
        f"{variable.replace('_', ' ').capitalize()} 📊:",
        min_value=ranges[variable][0],
        max_value=ranges[variable][1],
        value=(ranges[variable][0] + ranges[variable][1]) // 2,
        step=1 if isinstance(ranges[variable][0], int) else 0.01
    )

# Clip nilai untuk memastikan berada dalam range yang valid
clipped_inputs = clip_values(user_inputs, ranges)

# Ubah input menjadi array untuk prediksi
X = np.array([list(clipped_inputs.values())])

# 3. Memuat model
try:
    with open("gboost_model.pkl", "rb") as file:
        model = pickle.load(file)
    st.success("🎉 Model loaded successfully!")

    # 4. Prediksi dengan model
    if st.button("🔮 Predict"):
        prediction = model.predict(X)[0]
        result = {
            2: "<span style='color: green;'>🎓 Graduate</span>",
            0: "<span style='color: red;'>❌ Dropout</span>",
            1: "<span style='color: blue;'>📘 Enrolled</span>"
        }
        st.markdown(f"### Hasil Prediksi: {result[prediction]}", unsafe_allow_html=True)

except FileNotFoundError:
    st.error("⚠️ Model file not found. Please train and save your model first.")
