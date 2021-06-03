import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib as pt

# Select the relevant dataset, which in this case, is C02 Emissions
# Data cleaning

data = pd.read_excel(r'.\\Goal13.xlsx')

clean = pd.DataFrame(data, columns=['SeriesCode', 'SeriesDescription', 'GeoAreaCode', 'GeoAreaName', 'Value', 'Time_Detail'])

nonemdata = clean.groupby(["SeriesCode"]).get_group('EN_ATM_GHGT_NAIP').sort_values(by=['GeoAreaCode'], ascending='False')
anemdata = clean.groupby(["SeriesCode"]).get_group('EN_ATM_GHGT_AIP').sort_values(by=['GeoAreaCode'], ascending='False')

emdata = [anemdata, nonemdata]

emdata = pd.concat(emdata)

mtc02 = []
year = []
j = 0

for i in range(len(emdata)):

    mtc02.insert(j, emdata.iloc[i]['Value'])
    year.insert(j, emdata.iloc[i]['Time_Detail'])

    # Run linear regression per country
    if i == range(len(emdata)): # For when it reaches the end of the table
        print(emdata.iloc[i]["GeoAreaName"])

        model = LinearRegression().fit(np.reshape(year, (-1,1)), np.reshape(mtc02, (-1,1)))

        r_sq = model.score(np.reshape(year, (-1,1)), np.reshape(mtc02, (-1,1)))
        coef = model.coef_

        print('R-squared:', r_sq, 'Slope: ', coef)
        print(' ')
        continue

    elif emdata.iloc[i]["GeoAreaCode"] != emdata.iloc[i + 1]["GeoAreaCode"]: # For the next area code that is not the same
        # Run linear regression
        print(emdata.iloc[i]["GeoAreaName"])

        model = LinearRegression().fit(np.reshape(year, (-1,1)), np.reshape(mtc02, (-1,1)))

        r_sq = model.score(np.reshape(year, (-1,1)), np.reshape(mtc02, (-1,1)))
        coef = model.coef_

        print('R-squared:', r_sq, 'Slope: ', coef)
        print(' ')

        # Clear the array for new region
        mtc02.clear()
        year.clear()
        j = 0

        continue
    else:
        j += 1