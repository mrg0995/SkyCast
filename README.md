# 🌤️ SkyCast: Visualizador Climático en Tiempo Real

**SkyCast** es una aplicación interactiva desarrollada en Python que consume datos en vivo de la API de **OpenWeatherMap** para ofrecer información meteorológica precisa y visual de cualquier ciudad del mundo.

## ✨ Funcionalidades Principales
- 🌡️ **Métricas en Tiempo Real**: Visualización de temperatura, humedad y velocidad del viento.
- 🗺️ **Geolocalización Dinámica**: Integración de mapas interactivos mediante coordenadas (Latitud/Longitud).
- 🎨 **Interfaz Inteligente**: Iconos climáticos oficiales y mensajes de recomendación basados en la temperatura.
- 🌍 **Soporte Global**: Consulta de datos de cualquier localidad mediante el motor de búsqueda.

## 🛠️ Stack Tecnológico
- **Python 3.14**
- **Streamlit**: Framework para la interfaz web.
- **Pandas**: Gestión de estructuras de datos para el mapeado.
- **Requests**: Manejo de peticiones HTTP a la API externa.

## 🚀 Configuración y Uso

1. **Obtener una API Key**:
   Regístrate en [OpenWeatherMap](https://openweathermap.org/) y obtén tu llave gratuita.

2. **Instalar dependencias**:
   ```bash
   pip install streamlit requests pandas
  
3. Ejecutar la aplicación:
   ```bash
   streamlit run clima_app.py
