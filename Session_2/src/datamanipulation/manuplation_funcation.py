import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

def Load_data(data):
    import csv
    with open("/Users/himswamy0/Desktop/Python_practice/Session_2/data/flights.csv") as f:
        data_new = pd.read_csv(f, delimiter=',')
        data_new.drop('DAY_OF_WEEK',axis=1, inplace=True)
        data_new.rename(columns={'WHEELS_OFF': 'HAS_WHEELS'}, inplace=True)
        df_split = np.array_split(data_new, 4)
        data_new1 = pd.concat([df_split[0],df_split[1],df_split[2],df_split[3]])

        data_new1 = data_new1.reset_index(drop=True)
        data_new1 = data_new1.loc[data_new['AIRLINE'] == 'AA']
        data_new2 = data_new1[(data_new1['DEPARTURE_DELAY']<10) & (data_new1['DESTINATION_AIRPORT']=='PBI')]
        data_new1['AIR_SYSTEM_DELAY'] = data_new1['AIR_SYSTEM_DELAY'].fillna((data_new1['AIR_SYSTEM_DELAY'].mean()))
        data_new1['has_A'] = np.where(data_new1['AIRLINE'].apply(lambda x: 'A' in x), 1, 0)
        randm_sample = data_new1.sample(frac=0.3)
        data_new1['DEPARTURE_DELAY'] = (data_new1['DEPARTURE_DELAY']-data_new1['DEPARTURE_DELAY'].min())/(data_new1['DEPARTURE_DELAY'].max()-data_new1['DEPARTURE_DELAY'].min())
        cat_columns = ["ORIGIN_AIRPORT"]
        df_processed = pd.get_dummies(data_new1, prefix_sep="__",columns=cat_columns)
        df_processed.to_csv('/Users/himswamy0/Desktop/Python_practice/Session_2/data/final_data.csv')
        return ()
