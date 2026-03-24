# 🌤️ SkyCast: Real-Time Weather Dashboard

**SkyCast** is a modern weather application that provides accurate, real-time meteorological data for any location on Earth. By integrating the **OpenWeatherMap API** and **Folium maps**, it offers a comprehensive visual experience for tracking global weather conditions.

## ✨ Key Features
- 🌍 **Global Coverage**: Search for current weather data in any city or country.
- 🗺️ **Interactive Mapping**: Automatically generates a map centered on the searched location using **Folium**.
- 📊 **Detailed Metrics**: Real-time display of Temperature (°C), Humidity (%), Wind Speed (m/s), and visual status icons.
- 💡 **Smart Recommendations**: Dynamic UI alerts that provide travel or safety tips based on current temperature.
- 🎨 **Visual UI**: Clean, responsive design with custom CSS footer and weather-appropriate icons.

## 🛠️ Technologies Used
- **Python 3.10+**
- **Streamlit** (Web framework)
- **Requests** (API handling)
- **Folium & Streamlit-Folium** (Geospatial visualization)
- **OpenWeatherMap API** (Data source)

## 🚀 Installation and Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mrg0995/skycast-weather.git](https://github.com/mrg0995/skycast-weather.git)

2. Install dependencies:
   ```bash
   pip install streamlit requests folium streamlit-folium
  
3. Run the application:
   ```bash
   streamlit run sky_cast.py
