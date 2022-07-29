import numpy as np
import pandas as pd

df = pd.read_csv('attendance.csv', delimiter=',')
df.columns = ['Name','Punch_in']
print(df)