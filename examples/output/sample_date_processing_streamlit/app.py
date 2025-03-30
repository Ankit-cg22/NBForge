import streamlit as st
from data_processing import DataProcessor
from linear_regression import LinearRegressionModel

st.title("Mean Squared Error Calculator")

st.header("Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    file_path = uploaded_file.name
    st.header("Enter Target Column")
    target_column = st.text_input("Enter the target column name", value="target")
    if st.button("Calculate Mean Squared Error"):
        data_processor = DataProcessor(file_path)
        linear_regression_model = LinearRegressionModel(file_path, target_column)
        mse = linear_regression_model.run()
        st.write(f"Mean Squared Error: {mse}")