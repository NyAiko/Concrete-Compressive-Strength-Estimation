import streamlit as st
import joblib
import pandas as pd
from log import log_func
# Load the pre-trained model
model = joblib.load("gbr.p")


def predict(input_data):
    # Make predictions
    prediction = model.predict(input_data)
    
    return prediction

# Streamlit app
def main():
    st.title("Concrete Strength Prediction App")

    # User input for Cement
    cement = st.slider("Cement (kg/m^3)", min_value=100, max_value=540, value=320)

    # User input for BlastFurenace
    bf = st.slider("BlastFurenace", min_value=0, max_value=359, value=180)

    # Additional input variables
    fa = st.slider("FlyAsh", min_value=0, max_value=200, value=100)
    w = st.slider("Water", min_value=115, max_value=250, value=182)
    sp = st.slider("Super Plasticier", min_value=0, max_value=32, value=16)
    ca = st.slider("Coase Aggregate", min_value=800, max_value=1145, value=972)
    fagg = st.slider("Fine Aggregate", min_value=590, max_value=1000, value=795)
    age = st.slider("Age", min_value=1, max_value=365, value=28)

    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'Cement': [cement],
        'BF': [bf],
        'FA': [fa],
        'W': [w],
        'SP': [sp],
        'CA': [ca],
        'FAgg': [fagg],
        'Age': [age]
    })
    result = predict(input_data)
    st.success(f"Predicted Concrete Strength: {result[0]} MPa")
    # Button to make predictions
    #if st.button("Predict"):
    #    result = predict(input_data)
    #    st.success(f"Predicted Concrete Strength: {result[0]} MPa")

if __name__ == "__main__":
    main()
