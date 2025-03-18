import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('titanic_model.pkl')

st.title("🚢 Titanic Survival Prediction Web App")

# --- User Inputs ---
pclass = st.selectbox("Ticket Class (1 = First, 2 = Second, 3 = Third)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.slider("Fare Paid", 0.0, 300.0, 50.0)

# --- Feature Engineering ---
sex_val = 1 if sex == "male" else 0
class_obj = {1: 'First', 2: 'Second', 3: 'Third'}[pclass]
who = "man" if sex_val == 1 and age >= 18 else "woman" if sex_val == 0 and age >= 18 else "child"
adult_male = sex_val == 1 and age >= 18
alone = sibsp == 0 and parch == 0

# --- Create Input DataFrame ---
input_data = pd.DataFrame([{
    'pclass': pclass,
    'sex': sex_val,
    'age': age,
    'sibsp': sibsp,
    'parch': parch,
    'fare': fare,
    'class': class_obj,
    'who': who,
    'adult_male': adult_male,
    'alone': alone
}])

# --- Prediction ---
if st.button("Predict Survival"):
    prediction = model.predict(input_data)[0]
    result = "🟢 Survived" if prediction == 1 else "🔴 Did Not Survive"
    st.subheader(f"Prediction: {result}")
