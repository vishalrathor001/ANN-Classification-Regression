# ANN Customer Churn Prediction

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_APP_URL)

🔗 **Live Demo:** [Customer Churn Prediction App](YOUR_STREAMLIT_APP_URL)

An Artificial Neural Network (ANN) based machine learning application that predicts whether a bank customer is likely to churn. The trained model is integrated with a Streamlit web application to provide an interactive customer churn prediction interface.

## Project Overview

Customer churn prediction helps banks identify customers who are likely to leave their services. This project uses an Artificial Neural Network trained on the Churn Modelling dataset to predict customer churn based on customer information.

The application takes the following customer details as input:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Status
- Active Membership Status
- Estimated Salary

The trained ANN model then calculates the probability of customer churn.

## Technologies Used

- Python
- TensorFlow
- Keras
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Jupyter Notebook

## Machine Learning Workflow

    Churn Modelling Dataset
              ↓
       Data Preprocessing
              ↓
       Feature Encoding
              ↓
        Train-Test Split
              ↓
        Feature Scaling
              ↓
    Artificial Neural Network
              ↓
        Model Training
              ↓
        Model Evaluation
              ↓
       Save Trained Model
              ↓
    Streamlit Web Application
              ↓
     Customer Churn Prediction

## ANN Model Architecture

The Artificial Neural Network consists of:

- Input Layer
- Dense Hidden Layer with 64 neurons and ReLU activation
- Dense Hidden Layer with 32 neurons and ReLU activation
- Output Layer with 1 neuron and Sigmoid activation

The sigmoid output provides the probability of customer churn.

## Project Structure

    ANN-Classification-churn/
    │
    ├── app.py
    ├── Churn_Modelling.csv
    ├── experiments.ipynb
    ├── prediction.ipynb
    ├── model.h5
    ├── scaler.pkl
    ├── label_encoder_gender.pkl
    ├── onehot_encoder_geo.pkl
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## Important Files

### app.py

The main Streamlit application that collects customer information and performs churn prediction.

### model.h5

The trained Artificial Neural Network model used for making predictions.

### scaler.pkl

The saved StandardScaler used to scale input features before passing them to the ANN.

### label_encoder_gender.pkl

The saved LabelEncoder used to convert Gender values into numerical values.

### onehot_encoder_geo.pkl

The saved OneHotEncoder used to convert Geography values into one-hot encoded features.

### experiments.ipynb

Jupyter Notebook containing the model development, preprocessing, training, and experimentation steps.

### prediction.ipynb

Jupyter Notebook containing prediction-related experiments and testing.

### requirements.txt

Contains the Python libraries required to run the project.

## Installation

Clone the repository:

    git clone https://github.com/vishalrathor001/ANN-Classification-churn.git

Navigate to the project directory:

    cd ANN-Classification-churn

Create a virtual environment:

    python -m venv venv

Activate the virtual environment on Windows:

    venv\Scripts\activate

Install the required dependencies:

    pip install -r requirements.txt

## Run the Application

Run the Streamlit application:

    streamlit run app.py

The application will open in your browser at:

    http://localhost:8501

## Prediction

The application displays the predicted churn probability for the entered customer information.

If the predicted probability is greater than 0.5:

    The customer is likely to churn.

Otherwise:

    The customer is not likely to churn.

## Dataset

The project uses the Churn Modelling dataset, which contains customer information and a target variable indicating whether a customer exited the bank.

## Deployment

The application can be deployed using Streamlit Community Cloud directly from this GitHub repository.

## Author

Vishal Rathor

## Purpose

This project demonstrates the complete machine learning workflow, including:

- Data preprocessing
- Feature encoding
- Feature scaling
- Artificial Neural Network development
- Model training
- Model evaluation
- Model serialization
- Streamlit application development
- Machine learning deployment

## License

This project is intended for educational and academic purposes.