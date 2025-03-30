import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_data(self):
        # Load data
        df = pd.read_csv(self.file_path)
        return df
    
    def clean_data(self, df):
        # Clean data
        df.dropna(inplace=True)
        return df
