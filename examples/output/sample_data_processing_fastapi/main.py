from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from data_processor import DataProcessor

app = FastAPI()

class Data(BaseModel):
    file: str

@app.post("/mse")
def calculate_mse(file: UploadFile = File(...)):
    # Read the uploaded CSV file
    df = pd.read_csv(file.file)
    data_processor = DataProcessor(df)
    mse = data_processor.calculate_mse()
    return JSONResponse(content={"mse": mse}, media_type="application/json")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
