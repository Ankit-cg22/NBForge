from data_loader import DataLoader
from data_splitter import DataSplitter
from model_trainer import ModelTrainer
from model_evaluator import ModelEvaluator
import pandas as pd

# Load data
file_path = 'data.csv'
data_loader = DataLoader(file_path)
df = data_loader.load_data()

df = data_loader.clean_data(df)

target_column = 'target'
data_splitter = DataSplitter(df, target_column)
X_train, X_test, y_train, y_test = data_splitter.split_data()

# Train model
model_trainer = ModelTrainer(X_train, y_train)
model = model_trainer.train_model()

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
model_evaluator = ModelEvaluator(y_test, predictions)
mse = model_evaluator.evaluate_model()
print(f'Mean Squared Error: {mse}')
