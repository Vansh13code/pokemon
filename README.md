# Pokémon Power Prediction & Analysis

A complete Machine Learning project built using Pokémon data from the PokéAPI.  
This project includes:

- Data Collection using API
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Regression & Classification Models
- Streamlit Deployment
- FastAPI Deployment

---

# Live Deployments

## Streamlit App

https://pokemonanalysis.streamlit.app/

Features:
- Predict Pokémon Total Power
- Predict High Power / Low Power Pokémon

---

## FastAPI Swagger Docs

https://pokemonapi-7m1z.onrender.com/docs

Endpoint:
POST /predict_power

Predicts Pokémon total power using Linear Regression.

---

# Project Structure

```bash
pokemon_ml_assessment/
│
├── data/
├── exported_dataset/
├── model/
│   ├── decision_tree.pkl
│   ├── linear_regression.pkl
│   ├── logistic_regression.pkl
│   ├── tuned_decision_tree.pkl
│   └── model_columns.pkl
│
├── visualise/
├── report/
│
├── app.py
├── api.py
├── requirements.txt
└── main.ipynb
```

---

# Dataset Source

API Used:
https://pokeapi.co/

Data collected using REST API requests in Python.

---

# Features Used

| Feature | Description |
|---|---|
| name | Pokémon name |
| height | Height |
| weight | Weight |
| base_experience | Base experience |
| hp | Health points |
| attack | Attack power |
| defense | Defense points |
| special_attack | Special attack |
| special_defense | Special defense |
| speed | Speed |
| primary_type | Main Pokémon type |

---

# Feature Engineering

## Total Power

```python
total_power = hp + attack + defense + special_attack + special_defense + speed
```

## High Power Classification

Rules:
- 1 → High Power Pokémon
- 0 → Low Power Pokémon

Threshold applied on total power.

---

# Data Preprocessing

Performed:
- Null value handling
- Duplicate removal
- Data type conversion
- One-hot encoding
- Feature scaling
- Train-test split

---

# Exploratory Data Analysis (EDA)

Visualizations Created:
- Distribution Plot
- Correlation Heatmap
- Pokémon Type Frequency Chart
- Speed vs Attack Scatterplot
- Confusion Matrices
- Regression Comparison Graphs

Insights:
- Strong correlations between combat stats
- Detection of outliers
- Powerful Pokémon categories
- Type-based performance patterns

---

# Machine Learning Models

## Regression

- Linear Regression

Target:
- total_power

## Classification

- Logistic Regression
- Decision Tree Classifier
- Tuned Decision Tree Classifier

Target:
- is_high_power

---

# Model Evaluation

## Regression Metrics

- R² Score
- RMSE
- MAE

## Classification Metrics

- Accuracy
- Confusion Matrix
- Classification Report

---

# Streamlit App

Run locally:

```bash
streamlit run app.py
```

---

# FastAPI

Run locally:

```bash
uvicorn api:app --reload
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- FastAPI
- Uvicorn
- Joblib
- Git & GitHub

---

# Installation

Clone repository:

```bash
git clone https://github.com/Vansh13code/pokemon.git
```

Go to project folder:

```bash
cd pokemon
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# API Example Request

```json
{
  "attack": 90,
  "defense": 80,
  "speed": 100,
  "height": 15,
  "weight": 200,
  "base_experience": 250,
  "primary_type": "fire"
}
```

---

# API Example Response

```json
{
  "predicted_total_power": 512.67
}
```

---

# Deployment Platforms

| Service | Platform |
|---|---|
| Streamlit App | Streamlit Community Cloud |
| FastAPI API | Render |
| Source Code | GitHub |

---

# Future Improvements

- Add more Pokémon generations
- Hyperparameter tuning
- Docker deployment
- CI/CD pipeline
- Cloud database integration
- Advanced model optimization

---

# Author

## Vansh Batra
## Animesh Garg

GitHub:
https://github.com/Vansh13code

Project Repository:
https://github.com/Vansh13code/pokemon
