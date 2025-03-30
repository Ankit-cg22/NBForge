# Data processing
# - This notebook demonstrates how to do data processing to find mean squared error.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def clean_data(self):
        self.df.dropna(inplace=True)

    def split_data(self, target_column):
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, y_train):
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model

    def make_predictions(self, model, X_test):
        return model.predict(X_test)

    def evaluate_model(self, y_test, predictions):
        return mean_squared_error(y_test, predictions)