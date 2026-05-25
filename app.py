import streamlit as st
import joblib
import pandas as pd

model = joblib.load(
    "model/decision_tree.pkl"
)

st.title("Pokemon Power Prediction")

attack = st.number_input("Attack")
defense = st.number_input("Defense")
speed = st.number_input("Speed")
height = st.number_input("Height")
weight = st.number_input("Weight")
base_experience = st.number_input("Base Experience")

pokemon_type = st.selectbox(
    "Primary Type",
    [
        "dark",
        "dragon",
        "electric",
        "fairy",
        "fighting",
        "fire",
        "ghost",
        "grass",
        "ground",
        "ice",
        "normal",
        "poison",
        "psychic",
        "rock",
        "water"
    ]
)

if st.button("Predict"):

    input_data = {
        'attack': attack,
        'defense': defense,
        'speed': speed,
        'height': height,
        'weight': weight,
        'base_experience': base_experience,

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

    column_name = f'primary_type_{pokemon_type}'

    if column_name in input_data:
        input_data[column_name] = 1

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    st.success(
        f"Prediction if high so 1 and low so 0: {prediction[0]}"
    )