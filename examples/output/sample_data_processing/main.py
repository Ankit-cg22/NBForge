from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
from model_trainer import ModelTrainer
from model_evaluator import ModelEvaluator

# Example Usage
data_loader = DataLoader('data.csv')
df = data_loader.load_data()

preprocessor = DataPreprocessor(df)
df_clean = preprocessor.clean_data()
X_train, X_test, y_train, y_test = preprocessor.split_data(target_column='target')

trainer = ModelTrainer()
trainer.train(X_train, y_train)
predictions = trainer.predict(X_test)

evaluator = ModelEvaluator(y_test, predictions)
mse = evaluator.evaluate()
print(f'Mean Squared Error: {mse}')
