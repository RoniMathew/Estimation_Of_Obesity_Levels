#!/usr/bin/env python
# coding: utf-8

# In[55]:


get_ipython().system('pip install openpyxl')


# In[1]:


#Importing Libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl


# In[2]:


#Converting data into a dataframe
DataDF= pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')


# In[3]:


#viewing the first 5 rows
DataDF.head()


# In[4]:


#basic information about the dataset
DataDF.info()


# # Gender

# In[5]:


DataDF['Gender'].sort_values().unique()


# In[6]:


#replcaing the vaules female and male with 0 and 1 consecutively
DataDF['Gender'].replace(["Female","Male"],[0,1],inplace=True)


# In[7]:


DataDF['Gender'].sort_values().unique()


# # Age

# In[8]:


DataDF['Age']=DataDF['Age'].astype(int)


# In[9]:


DataDF['Age'].sort_values().unique()


# # Height

# In[10]:


DataDF['Height']=DataDF['Height'].round(2)


# In[11]:


DataDF['Height'].sort_values().unique()


# # Weight

# In[12]:


DataDF['Weight']=DataDF['Weight'].round(1)


# In[13]:


DataDF['Weight'].sort_values().unique()


# Changing Column Names

# In[14]:


# Rename columns
new_column_names = {
'family_history_with_overweight': 'Family_History_With_Overweight', 
'FAVC': 'Eat_High_Caloric_Food_Frequently',
'FCVC': 'Vegetable_Consumption_Frequency',
'NCP': 'Number_Of_Main_Meals_Daily',
'CAEC': 'Consumption_Of_Food_Between_Meal',
'SMOKE': 'Smoking',
'CH2O': 'Liquid_Intake_Daily',
'SCC': 'Calorie_Consumption_Monitoring',
'FAF': 'Physical_Activity',
'TUE': 'Time_Using_Technological_Devices',
'CALC': 'Alcohol_Consumption',
'MTRANS': 'Type_Of_Transportation',
'NObeyesdad': 'Obesity_Level'
}
DataDF = DataDF.rename(columns=new_column_names)


# In[15]:


DataDF.info()


# # Family History With Overweight

# In[16]:


DataDF['Family_History_With_Overweight'].sort_values().unique()


# In[17]:


#replcaing the vaules no and yes with 0 and 1 consecutively
DataDF['Family_History_With_Overweight'].replace(["no","yes"],[0,1],inplace=True)


# In[18]:


DataDF['Family_History_With_Overweight'].sort_values().unique()


# # Eat High Caloric Food Frequently

# In[19]:


DataDF['Eat_High_Caloric_Food_Frequently'].sort_values().unique()


# In[20]:


#replcaing the vaules no and yes with 0 and 1 consecutively
DataDF['Eat_High_Caloric_Food_Frequently'].replace(["no","yes"],[0,1],inplace=True)


# In[21]:


DataDF['Eat_High_Caloric_Food_Frequently'].sort_values().unique()


# # Vegetable Consumption Frequency

# In[22]:


DataDF['Vegetable_Consumption_Frequency']=DataDF['Vegetable_Consumption_Frequency'].astype(int)


# In[23]:


DataDF['Vegetable_Consumption_Frequency'].sort_values().unique()


# # Number Of Main Meals Daily

# In[24]:


DataDF['Number_Of_Main_Meals_Daily']=DataDF['Number_Of_Main_Meals_Daily'].astype(int)


# In[25]:


DataDF['Number_Of_Main_Meals_Daily'].sort_values().unique()


# # Consumption Of Food Between Meal

# In[26]:


DataDF['Consumption_Of_Food_Between_Meal'].sort_values().unique()


# In[27]:


DataDF['Consumption_Of_Food_Between_Meal'].replace(["no","Sometimes","Frequently","Always"],[0,1,2,3],inplace=True)


# In[28]:


DataDF['Consumption_Of_Food_Between_Meal'].sort_values().unique()


# # Smoking

# In[29]:


DataDF['Smoking'].sort_values().unique()


# In[30]:


DataDF['Smoking'].replace(["no","yes"],[0,1],inplace=True)


# In[31]:


DataDF['Smoking'].sort_values().unique()


# # Liquid Intake Daily

# In[32]:


DataDF['Liquid_Intake_Daily']=DataDF['Liquid_Intake_Daily'].round(1)


# In[33]:


DataDF['Liquid_Intake_Daily'].sort_values().unique()


# # Calorie Consumption Monitoring

# In[34]:


DataDF['Calorie_Consumption_Monitoring'].sort_values().unique()


# In[35]:


DataDF['Calorie_Consumption_Monitoring'].replace(["no","yes"],[0,1],inplace=True)


# In[36]:


DataDF['Calorie_Consumption_Monitoring'].sort_values().unique()


# # Physical Activity

# In[37]:


DataDF['Physical_Activity']=DataDF['Physical_Activity'].astype(int)


# In[38]:


DataDF['Physical_Activity'].sort_values().unique()


# # Time Using Technological Devices 

# In[39]:


DataDF['Time_Using_Technological_Devices']=DataDF['Time_Using_Technological_Devices'].round(2)


# In[40]:


DataDF['Time_Using_Technological_Devices'].sort_values().unique()


# # Alcohol Consumption 

# In[41]:


DataDF['Alcohol_Consumption'].sort_values().unique()


# In[42]:


DataDF['Alcohol_Consumption'].replace(["no","Sometimes","Frequently","Always"],[0,1,2,3],inplace=True)


# In[43]:


DataDF['Alcohol_Consumption'].sort_values().unique()


# # Type Of Transportation

# In[44]:


DataDF['Type_Of_Transportation'].sort_values().unique()


# In[45]:


DataDF['Type_Of_Transportation'].replace(["Automobile","Bike","Motorbike","Public_Transportation","Walking"],[1,2,3,4,5],inplace=True)


# In[46]:


DataDF['Type_Of_Transportation'].sort_values().unique()


# # Obesity Level

# In[47]:


DataDF['Obesity_Level'].sort_values().unique()


# In[48]:


DataDF['Obesity_Level'].replace(['Insufficient_Weight', 'Normal_Weight','Overweight_Level_I','Overweight_Level_II', 
    'Obesity_Type_I','Obesity_Type_II','Obesity_Type_III'],[0,1,2,2,3,3,3],inplace=True)


# #Insufficient_Weight -0
# #Normal_Weight -1
# #Overweight_Level_I,Overweight_Level_II -2
# #Obesity_Type_I,Obesity_Type_II,Obesity_Type_III -3

# In[49]:


DataDF['Obesity_Level'].sort_values().unique()


# In[ ]:





# In[50]:


#basic information about the dataset
DataDF.info()


# In[51]:


#Analysing statistical data of the dataframe 
DataDF.describe()


# In[52]:


DataDF.head()


# In[53]:


DataDF.to_excel('Obesity_DataSet.xlsx', index=False)


# In[ ]:




