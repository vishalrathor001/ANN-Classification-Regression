
import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle


# -----------------------------------
# Load models, encoders and scalers
# -----------------------------------
@st.cache_resource
def load_resources():
    classification_model = tf.keras.models.load_model("model.h5")
    regression_model = tf.keras.models.load_model("regression_model.h5")

    with open("label_encoder_gender.pkl", "rb") as file:
        label_encoder_gender = pickle.load(file)

    with open("onehot_encoder_geo.pkl", "rb") as file:
        onehot_encoder_geo = pickle.load(file)

    with open("scaler_class.pkl", "rb") as file:
        classification_scaler = pickle.load(file)

    with open("scaler.pkl", "rb") as file:
        regression_scaler = pickle.load(file)

    return (
        classification_model,
        regression_model,
        label_encoder_gender,
        onehot_encoder_geo,
        classification_scaler,
        regression_scaler,
    )


(
    classification_model,
    regression_model,
    label_encoder_gender,
    onehot_encoder_geo,
    classification_scaler,
    regression_scaler,
) = load_resources()


# -----------------------------------
# Streamlit interface
# -----------------------------------
st.title("ANN Customer Prediction System")
st.write("Choose a model to make a prediction.")

prediction_type = st.selectbox(
    "Select Prediction Type",
    ["Classification - Customer Churn",
     "Regression - Estimated Salary"]
)

st.subheader("Customer Details")

geography = st.selectbox(
    "Geography",
    onehot_encoder_geo.categories_[0]
)

gender = st.selectbox(
    "Gender",
    label_encoder_gender.classes_
)

age = st.slider("Age", 18, 92, 35)
credit_score = st.number_input(
    "Credit Score", min_value=0, value=650
)
balance = st.number_input(
    "Balance", min_value=0.0, value=0.0
)
tenure = st.slider("Tenure", 0, 10, 5)
num_of_products = st.slider("Number of Products", 1, 4, 1)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])


# -----------------------------------
# Encode common inputs
# -----------------------------------
gender_encoded = label_encoder_gender.transform([gender])[0]

geo_encoded = onehot_encoder_geo.transform([[geography]])

if hasattr(geo_encoded, "toarray"):
    geo_encoded = geo_encoded.toarray()

geo_columns = onehot_encoder_geo.get_feature_names_out(["Geography"])

geo_encoded_df = pd.DataFrame(
    geo_encoded,
    columns=geo_columns
)



# -----------------------------------
# Classification prediction
# -----------------------------------
if prediction_type == "Classification - Customer Churn":

    st.subheader("Customer Churn Prediction")

    estimated_salary = st.number_input(
        "Estimated Salary",
        min_value=0.0,
        value=50000.0
    )

    input_data = pd.DataFrame({
        "CreditScore": [credit_score],
        "Gender": [gender_encoded],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_of_products],
        "HasCrCard": [has_cr_card],
        "IsActiveMember": [is_active_member],
        "EstimatedSalary": [estimated_salary],
    })

    input_data = pd.concat(
        [input_data, geo_encoded_df],
        axis=1
    )

    input_scaled = classification_scaler.transform(input_data)
    prediction = classification_model.predict(
        input_scaled, verbose=0
    )

    churn_probability = float(prediction[0][0])

    st.metric("Churn Probability", f"{churn_probability:.2%}")

    if churn_probability >= 0.5:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is not likely to churn.")



# -----------------------------------
# Regression prediction
# -----------------------------------

# -----------------------------------
# Regression prediction
# -----------------------------------
else:

    st.subheader("Estimated Salary Prediction")

    exited = st.selectbox(
        "Has the Customer Exited?", [0, 1]
    )

    input_data = pd.DataFrame({
        "CreditScore": [credit_score],
        "Gender": [gender_encoded],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_of_products],
        "HasCrCard": [has_cr_card],
        "IsActiveMember": [is_active_member],
        "Exited": [exited],
    })

    input_data = pd.concat(
        [input_data, geo_encoded_df],
        axis=1
    )

    input_scaled = regression_scaler.transform(input_data)
    prediction = regression_model.predict(
        input_scaled, verbose=0
    )

    predicted_salary = float(prediction[0][0])

    st.metric(
        "Predicted Estimated Salary",
        f"${predicted_salary:,.2f}"
    )

