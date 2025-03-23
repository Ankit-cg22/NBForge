# This is the main module.
import numpy as np
from greet import greet
from data_operations import create_dataframe

name = "Alice"
message = greet(name)
print(message)

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = create_dataframe(data)
print(df)
