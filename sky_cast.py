import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SkyCast", 
    page_icon="🌤️", 
    layout="centered"
)

# OpenWeatherMap API Key
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

# Custom CSS for the footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: grey;
        text-align: center;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. USER INTERFACE ---
st.title("🌤️ SkyCast: Real-Time Weather")
st.write("Check weather conditions for any city in the world.")

city = st.text_input(
    "Enter a city name:", 
    placeholder="e.g., London, UK / New York, US / Tokyo, JP"
)

if city:
    # URL Construction (Metric units and English language)
    # Changed 'lang=es' to 'lang=en'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            # Data extraction
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]
            wind = data["wind"]["speed"]
            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]

            st.divider()
            
            # Metrics block
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperature", f"{temp} °C")
                st.write(f"**Conditions:** {description.capitalize()}")
                st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")

            with col2:
                st.metric("Humidity", f"{humidity} %")
                st.metric("Wind Speed", f"{wind} m/s")

            # Map block with Folium
            st.subheader(f"📍 Detected Location")
            m = folium.Map(location=[lat, lon], zoom_start=12)
            folium.Marker(
                [lat, lon], 
                popup=f"{city.capitalize()}", 
                icon=folium.Icon(color="red", icon="info-sign")
            ).add_to(m)
            
            st_folium(m, width=700, height=400)

            # Dynamic tips
            if temp > 25:
                st.info("☀️ It's hot outside. Stay hydrated!")
            elif temp < 10:
                st.info("❄️ It's cold. Don't forget your coat.")
            
        else:
            st.error("⚠️ City not found. Please try adding the country code (e.g., 'London, GB').")
            
    except Exception as e:
        st.error("❌ Connection error with the weather service.")

# Footer
st.markdown('<div class="footer">Data provided by OpenWeatherMap API • Built with Streamlit</div>', unsafe_allow_html=True)
