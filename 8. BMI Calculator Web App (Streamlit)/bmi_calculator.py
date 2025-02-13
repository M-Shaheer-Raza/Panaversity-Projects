import streamlit as st 

st.title("BMI Calculator")
st.write("Use the sliders below to select your weight (in kg) and height (in feet), then click the button to calculate your BMI.")

weight = st.slider("Select your weight in kilograms (kg):", min_value=20.0, max_value=200.0, value=70.0, step=0.5)
height_feet = st.slider("Select your height in feet:", min_value=3.0, max_value=7.0, value=5.5, step=0.1)

height_m = height_feet * 0.3048

if st.button("Calculate BMI"):
    if height_m > 0:
        bmi = weight / (height_m ** 2)
        st.write(f"Your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            st.write("**Interpretation:** Underweight")
        elif 18.5 <= bmi < 25:
            st.write("**Interpretation:** Normal weight")
        elif 25 <= bmi < 30:
            st.write("**Interpretation:** Overweight")
        else:
            st.write("**Interpretation:** Obese")
    else:
        st.error("Height must be greater than zero!")