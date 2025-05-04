# Clean data - This function cleans the data by dropping NA values.

import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    return df
