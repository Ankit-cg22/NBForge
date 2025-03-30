import pandas as pd

class DataPreprocessor:
    def __init__(self, df):
        self.df = df
    
    def clean_data(self):
        self.df.dropna(inplace=True)
        return self.df
    
    def split_data(self, target_column, test_size=0.2):
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        from sklearn.model_selection import train_test_split
        return train_test_split(X, y, test_size=test_size, random_state=42)
