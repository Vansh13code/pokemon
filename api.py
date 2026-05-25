from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

model = joblib.load(
    "model/linear_regression.pkl"
)

app = FastAPI()

class PokemonInput(BaseModel):

    attack: float
    defense: float
    speed: float
    height: float
    weight: float
    base_experience: float
    primary_type: str


@app.get("/")
def home():

    return {
        "message": "Pokemon Total Power Prediction API"
    }


@app.post("/predict_power")
def predict_power(data: PokemonInput):

    input_data = {
        'attack': data.attack,
        'defense': data.defense,
        'speed': data.speed,
        'height': data.height,
        'weight': data.weight,
        'base_experience': data.base_experience,

        'primary_type_dark': 0,
        'primary_type_dragon': 0,
        'primary_type_electric': 0,
        'primary_type_fairy': 0,
        'primary_type_fighting': 0,
        'primary_type_fire': 0,
        'primary_type_ghost': 0,
        'primary_type_grass': 0,
        'primary_type_ground': 0,
        'primary_type_ice': 0,
        'primary_type_normal': 0,
        'primary_type_poison': 0,
        'primary_type_psychic': 0,
        'primary_type_rock': 0,
        'primary_type_water': 0
    }

    type_column = f"primary_type_{data.primary_type}"

    if type_column in input_data:
        input_data[type_column] = 1

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_total_power": round(float(prediction), 2)
    }