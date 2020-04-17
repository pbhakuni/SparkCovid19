# Using Pandas Dataframe to rename columns

import pandas as pd
import glob
import os

filelist = glob.glob("/home/hduser/Desktop/Spark/Covid19Datasets/csse_covid_19_daily_reports/*.csv")

# Getting list of filenames
for filename in filelist:
    cereal_df = pd.read_csv(filename)
    cereal_df.columns = cereal_df.columns.str.strip().str.replace('Province_State', 'Province/State') \
        .str.replace('Country_Region', 'Country/Region').str.replace('Last_Update', 'Last Update') \
        .str.replace('Lat', 'Latitude').str.replace('Long_', 'Longitude')\
        .str.replace('Latitudeitude', 'Latitude')
    head, tail = os.path.split(filename)
    cereal_df.to_csv('/home/hduser/Desktop/Spark/Covid19Datasets/New_covid_reports/%s' %tail, index=False)
