from sklearn.model_selection import train_test_split

class DataSplitter:
    def __init__(self, df, target_column):
        self.df = df
        self.target_column = target_column
    
    def split_data(self):
        # Split data
        X = self.df.drop(columns=[self.target_column])
        y = self.df[self.target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
