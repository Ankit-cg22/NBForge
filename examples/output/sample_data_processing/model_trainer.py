from sklearn.linear_model import LinearRegression

class ModelTrainer:
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    
    def train_model(self):
        # Train model
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        return model
