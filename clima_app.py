import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SkyCast: Tu App del Clima", 
    page_icon="🌤️", 
    layout="centered"
)

# API Key de OpenWeatherMap
API_KEY = "TU_API_KEY_AQUI"

# Estilos CSS personalizados para el pie de página
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

# --- 2. INTERFAZ DE USUARIO ---
st.title("🌤️ SkyCast: El tiempo en tiempo real")
st.write("Consulta las condiciones climáticas de cualquier ciudad del mundo.")

ciudad = st.text_input(
    "Escribe el nombre de una ciudad:", 
    placeholder="Ej: Madrid, ES / Jaén, ES / Tokyo, JP"
)

if ciudad:
    # Construcción de la URL (Métrica y Español)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()

        if datos.get("cod") == 200:
            # Extracción de datos
            temp = datos["main"]["temp"]
            humedad = datos["main"]["humidity"]
            descripcion = datos["weather"][0]["description"]
            icono = datos["weather"][0]["icon"]
            viento = datos["wind"]["speed"]
            lat = datos["coord"]["lat"]
            lon = datos["coord"]["lon"]

            st.divider()
            
            # Bloque de métricas
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperatura", f"{temp} °C")
                st.write(f"**Estado:** {descripcion.capitalize()}")
                st.image(f"http://openweathermap.org/img/wn/{icono}@2x.png")

            with col2:
                st.metric("Humedad", f"{humedad} %")
                st.metric("Viento", f"{viento} m/s")

            # Bloque de Mapa con Folium
            st.subheader(f"📍 Ubicación detectada")
            m = folium.Map(location=[lat, lon], zoom_start=12)
            folium.Marker(
                [lat, lon], 
                popup=f"{ciudad.capitalize()}", 
                icon=folium.Icon(color="red", icon="info-sign")
            ).add_to(m)
            
            st_folium(m, width=700, height=400)

            # Consejos dinámicos
            if temp > 25:
                st.info("☀️ Hace calor. ¡Mantente hidratado!")
            elif temp < 10:
                st.info("❄️ Hace frío. No olvides tu abrigo.")
            
        else:
            st.error("⚠️ No se pudo encontrar la ciudad. Intenta añadir el código del país (ej: 'Jaén, ES').")
            
    except Exception as e:
        st.error("❌ Error de conexión con el servicio meteorológico.")

# Pie de página
st.markdown('<div class="footer">Datos proporcionados por OpenWeatherMap API • Desarrollado con Streamlit</div>', unsafe_allow_html=True)
