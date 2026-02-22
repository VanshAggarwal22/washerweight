import streamlit as st
import math

st.set_page_config(page_title="Washer Weight Calculator", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    font-size: 34px;
    font-weight: 700;
    color: #1f2937;
}
.subtitle {
    font-size: 16px;
    color: #4b5563;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.result-box {
    background-color: #e6f4ea;
    padding: 15px;
    border-radius: 8px;
    font-weight: 600;
    color: #065f46;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="title">Spring Washer & Flat Washer Weight Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Accurate industrial weight estimation based on dimensions and material density</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Material Selection ----------
material_options = {
    "Carbon Steel (7850 kg/m³)": 7850,
    "Stainless Steel (8000 kg/m³)": 8000,
    "Brass (8500 kg/m³)": 8500,
    "Aluminum (2700 kg/m³)": 2700
}

material = st.selectbox("Select Material", list(material_options.keys()))
density = material_options[material]

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Calculator Selection ----------
calc_type = st.radio("Choose Calculator", ["Spring Washer", "Flat Washer"])

st.markdown('<div class="card">', unsafe_allow_html=True)

outer_diameter = st.number_input("Outer Diameter (mm)", min_value=0.0, format="%.3f")
inner_diameter = st.number_input("Inner Diameter (mm)", min_value=0.0, format="%.3f")
thickness = st.number_input("Thickness (mm)", min_value=0.0, format="%.3f")
quantity = st.number_input("Quantity", min_value=1, step=1)

calculate = st.button("Calculate Weight")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Calculation ----------
if calculate:
    if outer_diameter > inner_diameter and thickness > 0:
        od = outer_diameter / 1000
        id_ = inner_diameter / 1000
        t = thickness / 1000

        volume = math.pi * t * ((od/2)**2 - (id_/2)**2)
        weight_one = volume * density
        total_weight = weight_one * quantity

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.write(f"Weight of One {calc_type}: {weight_one:.6f} kg")
        st.write(f"Total Weight for {quantity} Pieces: {total_weight:.6f} kg")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Outer diameter must be greater than inner diameter and thickness must be greater than zero.")
