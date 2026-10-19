
# Smart Irrigation Decision Support System 🌱

A machine learning-based irrigation decision support application developed with Python and Streamlit. The system estimates irrigation water requirements using plant type, temperature, soil moisture, and light conditions.

## Features

- Water requirement prediction using Random Forest Regression
- Weather data integration with OpenWeather API
- Support for 10 different plant types
- Irrigation cost and estimated water savings calculations
- Irrigation history tracking using SQLite
- Interactive dashboard built with Streamlit

## Technologies

- Python
- Streamlit
- Scikit-learn (Random Forest Regressor)
- Pandas & NumPy
- SQLite
- OpenWeather API

## Dataset

The model is trained on a synthetically generated dataset created with Python. Predictions are intended for demonstration and educational purposes, not validated agricultural recommendations.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/akilli-sulama.git
cd akilli-sulama
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your OpenWeather API key as the `OPENWEATHER_API_KEY` environment variable (optional for manual input mode).

4. Run the application:

```bash
streamlit run akilli_sulama.py
```

## Notes

Water savings and cost estimates are based on illustrative assumptions. Actual irrigation requirements depend on crop conditions and local agricultural factors.
  