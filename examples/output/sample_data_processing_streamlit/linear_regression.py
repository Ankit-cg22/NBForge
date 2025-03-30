# Linear regression
# - The below cell demonstrates how to use linear regression.

from data_processing import DataProcessor

class LinearRegressionModel:
    def __init__(self, file_path, target_column):
        self.data_processor = DataProcessor(file_path)
        self.target_column = target_column

    def run(self):
        self.data_processor.clean_data()
        X_train, X_test, y_train, y_test = self.data_processor.split_data(self.target_column)
        model = self.data_processor.train_model(X_train, y_train)
        predictions = self.data_processor.make_predictions(model, X_test)
        mse = self.data_processor.evaluate_model(y_test, predictions)
        return mse