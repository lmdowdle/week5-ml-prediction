# Customer Churn Prediction Using PyCaret

This repository contains the work completed for the Week 5 assignment in my Data Science course. The project demonstrates a full machine learning workflow using PyCaret, including model training in a Jupyter Notebook, model simplification to match the structure of new incoming data, and deployment of a standalone Python script that generates churn predictions.

---

## Project Overview

The goal of this assignment was to build a machine learning model capable of predicting customer churn and then apply that model to a new dataset. The workflow included:

- Loading and preparing the original churn dataset
- Training multiple classification models using PyCaret’s automated machine learning tools
- Selecting the best-performing model
- Simplifying the model to use only the features available in the new prediction dataset
- Saving the final model for deployment
- Creating a Python script (`new_churn_data.py`) that loads the model and generates predictions on new data

## Model Training Process

Model training was performed in a Jupyter Notebook using PyCaret’s `setup()` and `compare_models()` functions. PyCaret automatically evaluated several algorithms and selected the best-performing one based on default metrics.

During the prediction phase, I discovered that the new dataset did not contain all engineered features created during training. To resolve this, I retrained the model using only the raw features that appeared in both datasets:

- `customerID`
- `tenure`
- `PhoneService`
- `Contract`
- `PaymentMethod`
- `MonthlyCharges`
- `TotalCharges`

This ensured that the final model could successfully process the new CSV file without modification.

The simplified model was saved as `pycaret_model_simplified`.

---

## Prediction Script

The file `new_churn_data.py` contains the code used to generate predictions on the new dataset. The script:

1. Loads the new customer data (`new_churn_data.csv`)
2. Loads the simplified PyCaret model
3. Uses `predict_model()` to generate churn predictions
4. Prints the results to the console

The script can be executed in Jupyter using:
%run new_churn_data.py


All Python dependencies used in this project are listed in `requirements.txt`.  

---

## Summary of Results

The final simplified model successfully predicts customer churn using the features available in the new dataset.
