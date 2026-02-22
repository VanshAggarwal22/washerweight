import streamlit as st
import math

st.set_page_config(page_title="Washer Weight Calculator", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
<style>

/* Adaptive Background */
.main {
    background-color: var(--background-color);
}

/* Adaptive Heading */
.title {
    font-size: 36px;
    font-weight: 700;
    color: var(--text-color);
    letter-spacing: 0.5px;
}

/* Subtitle */
.subtitle {
    font-size: 16px;
    color: var(--text-color);
    opacity: 0.75;
}

/* Card Styling */
.card {
    background-color: var(--secondary-background-color);
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Result Box */
.result-box {
    background-color: rgba(0, 200, 120, 0.1);
    padding: 18px;
    border-radius: 10px;
    font-weight: 600;
    color: var(--text-color);
    border: 1px solid rgba(0, 200, 120, 0.4);
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="title">Spring Washer Weight Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Industrial weight estimation based on dimensions and material density</div>', unsafe_allow_html=True)

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
calc_type = st.radio("Choose Calculator Type", ["Spring Washer", "Plain Washer"])

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
        weight_one_kg = volume * density
        total_weight_kg = weight_one_kg * quantity

        weight_one_g = weight_one_kg * 1000
        total_weight_g = total_weight_kg * 1000

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.write(f"Weight of One {calc_type}: {weight_one_kg:.6f} kg  |  {weight_one_g:.2f} g")
        st.write(f"Total Weight for {quantity} Pieces: {total_weight_kg:.6f} kg  |  {total_weight_g:.2f} g")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Outer diameter must be greater than inner diameter and thickness must be greater than zero.")
