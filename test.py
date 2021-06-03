import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Select the relevant dataset, which in this case, is C02 Emissions
# Data cleaning

data = pd.read_excel(r'.\\Goal13.xlsx')

clean = pd.DataFrame(data, columns=['SeriesCode', 'SeriesDescription', 'GeoAreaCode', 'GeoAreaName', 'Value', 'Time_Detail'])

nonemdata = clean.groupby(["SeriesCode"]).get_group('EN_ATM_GHGT_NAIP').sort_values(by=['GeoAreaCode'], ascending='False')
anemdata = clean.groupby(["SeriesCode"]).get_group('EN_ATM_GHGT_AIP').sort_values(by=['GeoAreaCode'], ascending='False')

print(anemdata.head())
print(nonemdata.head())