from sklearn.metrics import mean_squared_error

class ModelEvaluator:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
    
    def evaluate(self):
        return mean_squared_error(self.y_true, self.y_pred)
