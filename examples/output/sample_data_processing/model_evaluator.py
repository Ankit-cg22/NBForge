# Evaluate model - This function evaluates the model using mean squared error.

from sklearn.metrics import mean_squared_error

def evaluate_model(y_test, predictions):
    return mean_squared_error(y_test, predictions)
