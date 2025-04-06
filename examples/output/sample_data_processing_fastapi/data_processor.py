# Data processing
# - This notebook demonstrates how to do data processing to find mean squared error.
# Linear regression
# - The below cell demonstrates how to use linear regression.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class DataProcessor:
    def __init__(self, df):
        self.df = df
    
    def clean_data(self):
        self.df.dropna(inplace=True)
    
    def split_data(self):
        target_column = 'target'
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    
    def make_predictions(self, model, X_test):
        predictions = model.predict(X_test)
        return predictions
    
    def evaluate_model(self, y_test, predictions):
        mse = mean_squared_error(y_test, predictions)
        return mse
    
    def calculate_mse(self):
        self.clean_data()
        X_train, X_test, y_train, y_test = self.split_data()
        model = self.train_model(X_train, y_train)
        predictions = self.make_predictions(model, X_test)
        mse = self.evaluate_model(y_test, predictions)
        return mse
