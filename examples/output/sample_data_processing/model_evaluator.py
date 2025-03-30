from sklearn.metrics import mean_squared_error

class ModelEvaluator:
    def __init__(self, y_test, predictions):
        self.y_test = y_test
        self.predictions = predictions
    
    def evaluate_model(self):
        # Evaluate model
        mse = mean_squared_error(self.y_test, self.predictions)
        return mse
