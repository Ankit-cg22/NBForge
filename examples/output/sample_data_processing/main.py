from data_loader import load_data
from data_cleaner import clean_data
from data_splitter import split_data
from model_trainer import train_model
from model_evaluator import evaluate_model

# Data processing
# - This notebook demonstrates how to do data processing to find mean squared error.
if __name__ == "__main__":
    file_path = 'data.csv'
    df = load_data(file_path)
    df = clean_data(df)
    X_train, X_test, y_train, y_test = split_data(df, 'target')
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    mse = evaluate_model(y_test, predictions)
    print(f'Mean Squared Error: {mse}')