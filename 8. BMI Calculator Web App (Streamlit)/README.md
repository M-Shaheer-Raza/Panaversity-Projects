# BMI Calculator Web App  

## Overview  
The **BMI Calculator Web App** is a simple tool built using **Streamlit** that allows users to calculate their **Body Mass Index (BMI)**. Users can input their **weight in kilograms** and **height in feet**, and the app will compute their BMI and provide a health interpretation.  

## Features  
- **User-friendly sliders** to select weight and height  
- **Automatic height conversion** from feet to meters  
- **Instant BMI calculation** with a single click  
- **Health interpretation** based on BMI categories  

## Project Structure  
```
BMI_Calculator/
│── bmi_calculator.py  # Main Streamlit app file
│── README.md          # Project documentation
```

## How It Works  
1. Users select their **weight (kg)** and **height (ft)** using sliders.  
2. The app **converts height** from feet to meters.  
3. Clicking the **"Calculate BMI"** button computes the BMI using:  
   \[
   BMI = \frac{\text{weight (kg)}}{\text{height (m)}^2}
   \]
4. The app **displays the BMI** and provides a health interpretation:  
   - **BMI < 18.5** → Underweight  
   - **BMI 18.5 - 24.9** → Normal weight  
   - **BMI 25 - 29.9** → Overweight  
   - **BMI ≥ 30** → Obese  

## Installation & Usage  

### 1. Install Dependencies  
Make sure **Python** is installed, then install **Streamlit**:  
```bash
pip install streamlit
```

### 2. Run the Web App  
```bash
streamlit run bmi_calculator.py
```

### 3. Use the App  
Adjust the sliders for **weight and height**, click **Calculate BMI**, and view the result!  

## Technologies Used  
- Python  
- Streamlit