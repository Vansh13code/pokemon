import streamlit as st
import pandas as pd
import joblib

regression_model = joblib.load(
    "model/linear_regression.pkl"
)

classification_model = joblib.load(
    "model/decision_tree.pkl"
)


columns = joblib.load(
    "model/model_columns.pkl"
)


st.title("Pokémon Power Prediction App")

st.write("Enter Pokémon stats")

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

    type_column = f"primary_type_{pokemon_type}"

    if type_column in input_data:
        input_data[type_column] = 1

    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(
        columns=columns,
        fill_value=0
    )

    

    total_power_prediction = regression_model.predict(
        input_df
    )[0]

   
   
   
    class_prediction = classification_model.predict(
        input_df
    )[0]

    
    st.success(
        f"Predicted Total Power: {round(total_power_prediction, 2)}"
    )

    if class_prediction == 1:
        st.success("High Power Pokémon")
    else:
        st.warning("Low Power Pokémon")