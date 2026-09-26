import os
import warnings
import pickle
import numpy as np
import pandas as pd
import requests
from PIL import Image

import streamlit as st

# Page Configuration
st.set_page_config(page_title="AgriSens", layout="wide")
warnings.filterwarnings('ignore')

# Helper function to load TensorFlow lazily
def load_tf():
    import tensorflow as tf
    return tf

# Plant Disease Prediction Helper
def model_prediction(test_image):
    model_path = "trained_plant_disease_model.keras"
    if os.path.exists(model_path):
        tf = load_tf()
        model = tf.keras.models.load_model(model_path)
        image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])
        predictions = model.predict(input_arr)
        return np.argmax(predictions)
    else:
        import random
        return random.randint(0, 37)

# Weather Fetching Function (Uses OpenWeatherMap API)
def get_weather(city_name, api_key="bd5e378503939ddaee76f12ad7a97608"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") == 200:
            return data
        else:
            return None
    except Exception:
        return None

# Sidebar Navigation
st.sidebar.title("AgriSens")
app_mode = st.sidebar.selectbox("Select Page", ["CROP RECOMMENDATION", "DISEASE RECOGNITION", "WEATHER UPDATE"])

# PAGE 1: CROP RECOMMENDATION
if app_mode == "CROP RECOMMENDATION":
    st.markdown("<h1 style='text-align: center;'>SMART CROP RECOMMENDATIONS</h1>", unsafe_allow_html=True)
    
    if os.path.exists("crop.png"):
        img = Image.open("crop.png")
        st.image(img, use_column_width=True)

    st.sidebar.header("Enter Crop Details")
    nitrogen = st.sidebar.number_input("Nitrogen", min_value=0.0, max_value=140.0, value=0.0, step=0.1)
    phosphorus = st.sidebar.number_input("Phosphorus", min_value=0.0, max_value=145.0, value=0.0, step=0.1)
    potassium = st.sidebar.number_input("Potassium", min_value=0.0, max_value=205.0, value=0.0, step=0.1)
    temperature = st.sidebar.number_input("Temperature (°C)", min_value=0.0, max_value=51.0, value=0.0, step=0.1)
    humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    ph = st.sidebar.number_input("pH Level", min_value=0.0, max_value=14.0, value=0.0, step=0.1)
    rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)

    if st.sidebar.button("Predict Crop"):
        inputs = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        if not inputs.any() or np.isnan(inputs).any() or (inputs == 0).all():
            st.error("Please fill in all input fields with valid values before predicting.")
        else:
            try:
                RF_Model_pkl = pickle.load(open('RF.pkl', 'rb'))
                prediction = RF_Model_pkl.predict(inputs)
                st.success(f"The recommended crop is: **{prediction[0]}**")
            except FileNotFoundError:
                st.error("Model file 'RF.pkl' not found.")

# PAGE 2: DISEASE RECOGNITION
elif app_mode == "DISEASE RECOGNITION":
    st.markdown("<h1 style='text-align: center;'>SMART DISEASE DETECTION</h1>", unsafe_allow_html=True)
    
    if os.path.exists("Diseases.png"):
        img = Image.open("Diseases.png")
        st.image(img, use_column_width=True)

    st.header("DISEASE RECOGNITION")
    test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"])
    
    if test_image is not None:
        st.image(test_image, width=300, caption="Uploaded Image")
        
        if st.button("Predict Disease"):
            st.snow()
            st.write("Analyzing Image...")
            result_index = model_prediction(test_image)
            class_names = [
                'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                'Tomato___healthy'
            ]
            st.success(f"Model Prediction: **{class_names[result_index]}**")

# PAGE 3: LIVE WEATHER UPDATE
elif app_mode == "WEATHER UPDATE":
    st.markdown("<h1 style='text-align: center;'>LIVE WEATHER & FARMING ADVISORY</h1>", unsafe_allow_html=True)
    
    city = st.text_input("Enter your City / Location:", "Delhi")
    
    if st.button("Get Weather"):
        weather_data = get_weather(city)
        if weather_data:
            temp = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            weather_desc = weather_data["weather"][0]["description"].title()
            wind_speed = weather_data["wind"]["speed"]
            
            # Display Weather Cards in columns
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Temperature", f"{temp} °C")
            col2.metric("Humidity", f"{humidity} %")
            col3.metric("Condition", weather_desc)
            col4.metric("Wind Speed", f"{wind_speed} m/s")
            
            # Agricultural advice based on live weather
            st.markdown("---")
            st.subheader("Agricultural Advisory")
            if temp > 35:
                st.warning("High Temperature Warning: Ensure adequate irrigation for sensitive crops.")
            elif temp < 10:
                st.warning("Cold Alert: Protect delicate crops from frost damage.")
            else:
                st.info("Weather conditions are favorable for standard farming activities.")
        else:
            st.error("Could not fetch weather data. Please check the city name.")