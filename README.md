
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

  ## Project Structure

- `akilli_sulama.py` - Streamlit application and user interface
- `model.py` - Random Forest model training and evaluation
- `veri_olusturucu.py` - Synthetic dataset generation
- `bitki_verisi.csv` - Dataset used for model training
- `requirements.txt` - Python dependencies

## Dataset

The model is trained on a synthetically generated dataset created with Python. Predictions are intended for demonstration and educational purposes, not validated agricultural recommendations.


## Model Performance

The Random Forest Regressor was evaluated using an 80/20 train-test split on a synthetically generated dataset.

| Evaluation Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 3.40 |
| Root Mean Squared Error (RMSE) | 4.29 |
| R² Score | 0.9390 |

The model explains approximately 93.9% of the variance in the synthetic test dataset. These results demonstrate performance on simulated data and do not represent validated real-world agricultural accuracy.
  
## Installation

1. Clone the repository:

```bash
git clone https://github.com/NilAkcay/akilli-sulama.git
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
  
