import numpy as np
import pandas as pd

# Select the relevant dataset, which in this case, is C02 Emissions
# Data cleaning

data = pd.read_excel(r'.\\Goal13.xlsx')

clean = pd.DataFrame(data, columns=['SeriesCode', 'SeriesDescription', 'GeoAreaName', 'Value', 'Time_Detail'])

# Hardcoding oof
# NOTE: Find a non-hardcoded version of separating the data
emdata = clean.iloc[7292:7959, :]
