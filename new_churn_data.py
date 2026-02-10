

import pandas as pd
import pickle
from pycaret.classification import load_model, predict_model


def load_data(filepath):

    df = pd.read_csv(filepath)
    return df


def make_predictions(df):
   
    model = load_model("pycaret_model_simplified")
    predictions = predict_model(model, data=df)
    return predictions


if __name__ == "__main__":
    df = load_data('new_churn_data.csv')
    predictions = make_predictions(df)
    print('predictions:')
    print(predictions)