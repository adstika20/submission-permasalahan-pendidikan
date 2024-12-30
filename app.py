import streamlit as st
import numpy as np
import pickle

# Custom CSS untuk styling
st.markdown("""
    <style>
    .main-header {
        font-family: 'Helvetica', sans-serif;
        background: linear-gradient(to right, #1a472a, #2e7d32);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        color: white;
        text-align: center;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .status-box {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        border-radius: 5px;
        font-weight: bold;
    }
    .graduate {
        background-color: #e8f5e9;
        color: #2e7d32;
    }
    .dropout {
        background-color: #ffebee;
        color: #c62828;
    }
    .enrolled {
        background-color: #e3f2fd;
        color: #1565c0;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="main-header">
        <h1>🎓 Prediksi Status Mahasiswa</h1>
        <p>Menggunakan Model Gradient Boosting</p>
    </div>
    """, unsafe_allow_html=True)

# Information Section
st.markdown("""
    <div class="info-box">
        <h3>📊 Tentang Aplikasi</h3>
        <p>Aplikasi ini membantu memprediksi status akademik mahasiswa berdasarkan berbagai faktor. 
        Status yang dapat diprediksi:</p>
        <div class="status-box graduate">Graduate 🎓</div>
        <div class="status-box dropout">Dropout ❌</div>
        <div class="status-box enrolled">Enrolled 📘</div>
    </div>
    """, unsafe_allow_html=True)

# Organize variables into logical groups
variable_groups = {
    "Data Pribadi": [
        "Marital_status", "Age_at_enrollment", "Gender", "Nacionality",
        "International", "Displaced", "Educational_special_needs"
    ],
    "Data Akademik": [
        "Application_mode", "Application_order", "Course", "Previous_qualification",
        "Previous_qualification_grade", "Admission_grade"
    ],
    "Data Keluarga": [
        "Mothers_qualification", "Fathers_qualification",
        "Mothers_occupation", "Fathers_occupation"
    ],
    "Data Keuangan": [
        "Debtor", "Tuition_fees_up_to_date", "Scholarship_holder"
    ],
    "Data Akademik Semester 1": [
        "Curricular_units_1st_sem_credited", "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_evaluations", "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_grade", "Curricular_units_1st_sem_without_evaluations"
    ],
    "Data Akademik Semester 2": [
        "Curricular_units_2nd_sem_credited", "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_evaluations", "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_grade", "Curricular_units_2nd_sem_without_evaluations"
    ],
    "Data Ekonomi": [
        "Unemployment_rate", "Inflation_rate", "GDP"
    ]
}

# Fungsi untuk memastikan nilai berada dalam range yang benar
def clip_values(values, ranges):
    clipped_values = {}
    for column, (min_val, max_val) in ranges.items():
        if column in values:
            clipped_values[column] = np.clip(values[column], min_val, max_val)
    return clipped_values

# Range untuk setiap variabel
ranges = {
    # ... (ranges sama seperti sebelumnya)
}

# Input Form dengan Tabs
user_inputs = {}
tabs = st.tabs(list(variable_groups.keys()))

for tab, (group_name, variables) in zip(tabs, variable_groups.items()):
    with tab:
        st.markdown(f"### {group_name}")
        col1, col2 = st.columns(2)
        for i, var in enumerate(variables):
            with col1 if i % 2 == 0 else col2:
                # Add help text for each input
                help_text = f"Range: {ranges[var][0]} - {ranges[var][1]}"
                user_inputs[var] = st.number_input(
                    f"{var}:",
                    min_value=float(ranges[var][0]),
                    max_value=float(ranges[var][1]),
                    value=float((ranges[var][0] + ranges[var][1]) / 2),
                    help=help_text
                )

# Clip nilai untuk memastikan berada dalam range yang valid
clipped_inputs = clip_values(user_inputs, ranges)

# Convert input menjadi array untuk prediksi
X = np.array([list(clipped_inputs.values())])

# Load model dan prediksi
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        with open("gboost_model.pkl", "rb") as file:
            model = pickle.load(file)
        
        if st.button("🔍 Prediksi Status", use_container_width=True):
            prediction = model.predict(X)[0]
            result = {
                2: """<div class="status-box graduate">Graduate 🎓</div>""",
                0: """<div class="status-box dropout">Dropout ❌</div>""",
                1: """<div class="status-box enrolled">Enrolled 📘</div>"""
            }
            st.markdown("<h3 style='text-align: center;'>Hasil Prediksi:</h3>", unsafe_allow_html=True)
            st.markdown(result[prediction], unsafe_allow_html=True)
            
    except FileNotFoundError:
        st.error("⚠️ Model file not found. Please train and save your model first.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Developed with ❤️ for Educational Purposes</p>
    </div>
    """, unsafe_allow_html=True)
