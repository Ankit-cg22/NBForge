# Data cleaning function
# Clean data
import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    return df
