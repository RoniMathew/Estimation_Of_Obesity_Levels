#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import warnings
warnings.filterwarnings("ignore", category=UserWarning) 


# In[3]:


#Creating a dataframe based on the data
DataDF =pd.read_excel("Obesity_DataSet.xlsx")


# In[4]:


#first 5 rows of the dataframe
DataDF.head()


# # Divide data into Dependent and Independent variables

# In[5]:


X= DataDF.iloc[:,:-1].values


# In[6]:


y= DataDF.iloc[:,16].values


# # Splitting data into test data and train data

# In[7]:


#Dividing the data into a training dataset and a test dataset. 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)


# In[8]:


X_train.shape


# In[9]:


X_test.shape


# In[10]:


y_train.shape


# In[11]:


y_test.shape


# ## STANDARDIZATION OF DATA

# In[12]:


#Scaling the data by using StandardScaler
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train_scaled=sc.fit_transform(X_train)
X_test_scaled=sc.transform(X_test)


# ## Building And Fitting Regression model

# In[13]:


# Building Multiple Linear Regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()


# In[14]:


# Fitting Multiple Linear Regression to the Training set
model.fit (X_train_scaled, y_train)


# ## Predicting the test set results

# In[15]:


y_pred =model.predict(X_test_scaled)


# In[16]:


print(y_pred)


# ## Model Evaluation

# In[17]:


# Calculating the Coefficients
print(model.coef_)


# In[18]:


#Calculating the Intercept
print(model.intercept_)


# In[19]:


# Calculating the R squared value
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)


# In[20]:


import seaborn as sns
sns.displot(y_pred-y_test,kind='kde')


# In[22]:


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_pred,y_test)


# In[23]:


mse


# In[ ]:




