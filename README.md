# ANN Classification and Regression

🔗 **Live Demo:** [ANN Prediction System](https://ann-classification-churn-jfott3cmp8fqhtfgtmnifo.streamlit.app/)

An Artificial Neural Network (ANN)-based machine learning project that integrates **Classification and Regression** into a single Streamlit web application. The application uses trained neural network models to predict customer churn and estimate customer salary based on customer information.

## Project Overview

This project demonstrates two machine learning tasks using the Bank Churn Modelling dataset:

- **Classification:** Predicts whether a bank customer is likely to leave the bank.
- **Regression:** Predicts a customer's estimated salary.

Users can select the prediction type from the Streamlit interface. Predictions update automatically when input values change.

## Features

### 1. Customer Churn Classification

The classification model predicts the probability that a customer will leave the bank.

Input features include:

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

The model uses a sigmoid output to produce a churn probability. A threshold of 0.5 is used to classify the prediction as likely or unlikely to churn.

### 2. Estimated Salary Regression

The regression model predicts the estimated salary of a customer based on the following features:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Status
- Active Membership Status
- Customer Exit Status

The regression model produces a continuous numerical salary estimate.

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

1. Load the Churn Modelling dataset.
2. Perform data preprocessing.
3. Encode categorical features.
4. Split the data into training and testing sets.
5. Scale numerical features.
6. Build and train ANN models.
7. Evaluate model performance.
8. Save trained models and preprocessing objects.
9. Integrate both models into a Streamlit application.
10. Deploy the application using Streamlit Community Cloud.

## ANN Model Architecture

The neural network architecture used for the classification model consists of:

- Input Layer
- Hidden Layer with 64 neurons and ReLU activation
- Hidden Layer with 32 neurons and ReLU activation
- Output Layer with 1 neuron and Sigmoid activation

The regression model uses a separate trained ANN with a single numerical output for salary prediction.

## Project Structure

```text
ANN-Classification-Regression/
│
├── app.py
├── Churn_Modelling.csv
├── experiments.ipynb
├── prediction.ipynb
├── model.h5
├── regression_model.h5
├── scaler_class.pkl
├── scaler.pkl
├── label_encoder_gender.pkl
├── onehot_encoder_geo.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## Important Files

### `app.py`

The main Streamlit application that provides both classification and regression prediction modes.

### `model.h5`

The trained ANN model used for customer churn classification.

### `regression_model.h5`

The trained ANN model used for estimated salary regression.

### `scaler_class.pkl`

The fitted StandardScaler used to preprocess input features for the classification model.

### `scaler.pkl`

The fitted StandardScaler used to preprocess input features for the regression model.

### `label_encoder_gender.pkl`

The saved LabelEncoder used to transform gender values into numerical values.

### `onehot_encoder_geo.pkl`

The saved OneHotEncoder used to transform geography values into one-hot encoded features.

### `experiments.ipynb`

The Jupyter Notebook containing model development, preprocessing, training, and experimentation.

### `prediction.ipynb`

The Jupyter Notebook containing prediction-related experiments and testing.

### `requirements.txt`

Contains the Python libraries required to run the application.

## Installation

Clone the repository:

```bash
git clone https://github.com/vishalrathor001/ANN-Classification-Regression.git
```

Navigate to the project directory:

```bash
cd ANN-Classification-Regression
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

Select either **Customer Churn Classification** or **Estimated Salary Regression** from the application menu. Enter the customer details, and the prediction will update automatically when the inputs change.

## Prediction Outputs

**Classification:** Displays the churn probability and indicates whether the customer is likely to leave the bank using a 0.5 threshold.

**Regression:** Displays the predicted estimated salary as a continuous numerical value.

## Dataset

The project uses the Churn Modelling dataset, which contains customer information and an `Exited` target variable indicating whether a customer left the bank.

For classification, `Exited` is the target variable. For regression, `EstimatedSalary` is the target variable, and `Exited` is used as an input feature.

## Deployment

The application is deployed using Streamlit Community Cloud and connected to this GitHub repository.

The same Streamlit application provides access to both trained ANN models through a single interface.

## Author

**Vishal Kumar**

## Purpose

This project demonstrates the practical implementation of:

- Data preprocessing
- Categorical feature encoding
- Feature scaling
- Artificial Neural Network development
- Classification and regression
- Model training and evaluation
- Model serialization
- Streamlit application development
- Machine learning deployment

## License

This project is intended for educational and academic purposes.