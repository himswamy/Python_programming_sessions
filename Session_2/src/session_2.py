
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


# In[2]:


data = pd.read_csv("/Users/himswamy0/Desktop/Python_practice/Session_2/data/flights.csv")
data.head(2)


# In[3]:


data.drop('DAY_OF_WEEK', axis=1, inplace=True)


# In[4]:


#data.head(2)
data.columns


# In[5]:


data.rename(columns={'WHEELS_OFF': 'HAS_WHEELS'}, inplace=True)


# In[6]:


df_split = np.array_split(data, 4)


# In[7]:


data_new = pd.concat([df_split[0],df_split[1],df_split[2],df_split[3]])

data_new = data_new.reset_index(drop=True)


# In[9]:


data_new1 = data_new.loc[data_new['AIRLINE'] == 'AA']


# In[10]:


data_new2 = data_new1[(data_new1['DEPARTURE_DELAY']<10) & (data_new1['DESTINATION_AIRPORT']=='PBI')]


# In[13]:


data_new['AIR_SYSTEM_DELAY'] = data_new['AIR_SYSTEM_DELAY'].fillna((data_new['AIR_SYSTEM_DELAY'].mean()))


# In[14]:


data_new['has_A'] = np.where(data_new['AIRLINE'].apply(lambda x: 'A' in x), 1, 0)


# In[15]:


randm_sample = data_new.sample(frac=0.3)


# In[17]:



data_new['DEPARTURE_DELAY'] = (data_new['DEPARTURE_DELAY']-data_new['DEPARTURE_DELAY'].min())/(data_new['DEPARTURE_DELAY'].max()-data_new['DEPARTURE_DELAY'].min())






# In[20]:


cat_columns = ["ORIGIN_AIRPORT"]

df_processed = pd.get_dummies(data_new, prefix_sep="__",columns=cat_columns)

df_processed.head()


# In[101]:


#four_equal_size = \
    #{name: group for name, group in data.groupby(np.arange(499999) // num)}


# In[102]:


#keys, values = zip(*four_equal_size.items())


# In[184]:


#data_new1 = pd.concat([four_equal_size[0],four_equal_size[1],four_equal_size[2],four_equal_size[3]])


# In[185]:


#data_new.columns

