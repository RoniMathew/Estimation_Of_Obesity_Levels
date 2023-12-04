#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


DataDF= pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')


# In[7]:


#viewing the first 5 rows
DataDF.head()


# In[8]:


#viewing the last 5 rows
DataDF.tail()


# In[10]:


#shape of the dataset
DataDF.shape


# In[12]:


#checking and counting missing values if present
DataDF.isnull().sum()


# In[13]:


#Analysing statistical data of the dataframe 
DataDF.describe()


# In[16]:


#Analysing statistical data of the full dataframe 
DataDF.describe(include="all")


# In[14]:


#Analysing the dataframe info
DataDF.info()


# In[ ]:





# In[ ]:




