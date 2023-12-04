#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import sklearn as sk
from scipy.stats import skew, kurtosis


# In[2]:


DataDF =pd.read_excel("Obesity_DataSet.xlsx")


# In[3]:


DataDF.head()


# # 1 Gender

# In[4]:


#Checking the total count of unique values in the column 'Gender'
DataDF['Gender'].value_counts()


# In[5]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Gender',palette='muted')
plt.title('Gender Distribution')
plt.show()


# In[6]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Gender'].value_counts()
count.index =['Male','Female']
colors = ['#008fd5','#e5ae37']

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index, autopct='%1.1f%%', colors=colors)
plt.title("Gender Distribution")

#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 2 Age

# In[7]:


#Descriptive Summary of column 'Age'
DataDF['Age'].describe()


# In[8]:


#Skewness And Kurtosis
# Calculating the skewness of the column
skewness = DataDF['Age'].skew().round(2)
print("Skewness of column 'Age':", skewness)

# Calculating the kurtosis of the column
kurtosis = DataDF['Age'].kurtosis().round(2)
print("Kurtosis of column 'Age':", kurtosis)


# #a skewness of 1.56 suggests a positively skewed distribution for the 'Age' column.
# The 'Age' distribution is positively skewed, meaning that there may be some older individuals who are significantly older than the majority of the population.

# #a kurtosis of 2.99 suggests a distribution with moderately heavy tails compared to a normal distribution.
# The distribution has moderately heavy tails, indicating that there may be some variability in the ages of individuals in the dataset, but it is not extremely pronounced.

# In[9]:


#Boxplot
#Creating the boxplot using seaborn
ax = sns.boxplot(x='Age', data=DataDF, color='#008fd5')

#Adding a title to the plot
ax.set_title('Age Distribution')

plt.show()


# In[15]:


#Plotting the distribution of the column 'Age' by histogram
plt.figure(figsize=(10,5))
colors = ['#008fd5','#e5ae37']
sns.histplot(x='Age',data=DataDF,hue='Obesity_Level',multiple='stack',
             bins='auto',stat='frequency',kde=True,color=colors,palette='colorblind')
plt.xticks(np.arange(10,70,5))
plt.show()


# # 3 Height

# In[11]:


#Descriptive Summary 
DataDF['Height'].describe()


# In[12]:


#Skewness And Kurtosis
# Calculating the skewness of the column
skewness = DataDF['Height'].skew().round(2)
print("Skewness of column 'Height':", skewness)

# Calculating the kurtosis of the column
kurtosis = DataDF['Height'].kurtosis().round(2)
print("Kurtosis of column 'Height':", kurtosis)


# #a skewness of -0.01 suggests a very slight negative skewness, meaning that the distribution has a slightly longer left tail than the right. However, the skewness is close to zero, indicating almost symmetrical distribution.

# #a kurtosis of -0.57 indicates that the distribution has slightly lighter tails compared to a normal distribution. It suggests a flatter peak and less extreme values in the tails

# In[13]:


#Boxplot
#Creating the boxplot using seaborn
ax = sns.boxplot(x='Height', data=DataDF, color='#008fd5')

#Adding a title to the plot
ax.set_title('Height Distribution')

plt.show()


# In[18]:


#Plotting the distribution of the column by histogram
plt.figure(figsize=(10,5))
colors = ['#008fd5','#e5ae37']
sns.histplot(x='Height',data=DataDF,hue='Obesity_Level',multiple='stack',
             bins='auto',stat='frequency',kde=True,color=colors,palette='colorblind')
plt.xticks(np.arange(1.4,2.1,0.1))
plt.show()


# # 4 Weight

# In[19]:


#Descriptive Summary 
DataDF['Weight'].describe()


# In[20]:


#Skewness And Kurtosis
# Calculating the skewness of the column
skewness = DataDF['Weight'].skew().round(2)
print("Skewness of column 'Weight':", skewness)

# Calculating the kurtosis of the column
kurtosis = DataDF['Weight'].kurtosis().round(2)
print("Kurtosis of column 'Weight':", kurtosis)


# #A skewness value of 0.26 indicates a slightly positively skewed distribution.
# The 'Weight' distribution is slightly positively skewed, suggesting that there may be a few individuals with higher weights compared to the majority.

# #A kurtosis value of -0.7 indicates that the distribution has lighter tails than a normal distribution (platykurtic).
# The distribution has lighter tails than a normal distribution, indicating that extreme values (very high or very low weights) are less common

# In[21]:


#Boxplot
#Creating the boxplot using seaborn
ax = sns.boxplot(x='Weight', data=DataDF, color='#008fd5')

#Adding a title to the plot
ax.set_title('Weight Distribution')

plt.show()


# In[23]:


#Plotting the distribution of the column by histogram
plt.figure(figsize=(10,5))
colors = ['#008fd5','#e5ae37']
sns.histplot(x='Weight',data=DataDF,hue='Obesity_Level',multiple='stack',
             bins='auto',stat='frequency',kde=True,color=colors,palette='colorblind')
plt.xticks(np.arange(30,180,10))
plt.show()


# # 5 Family History With Overweight

# In[24]:


#Checking the total count of unique values in the column 
DataDF['Family_History_With_Overweight'].value_counts()


# In[25]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Family_History_With_Overweight',palette='muted')
plt.title('Distribution')
plt.show()


# In[99]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Family_History_With_Overweight'].value_counts()
count.index =['Yes','No']
colors = ['#008fd5','#e5ae37']

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index, autopct='%1.1f%%', colors=colors)
plt.title("'Family_History_With_Overweight' Distribution")

#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 6 Eat High Caloric Food Frequently

# In[27]:


#Checking the total count of unique values in the column
DataDF['Eat_High_Caloric_Food_Frequently'].value_counts()


# In[28]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Eat_High_Caloric_Food_Frequently',palette='muted')
plt.title('Distribution')
plt.show()


# In[100]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Eat_High_Caloric_Food_Frequently'].value_counts()
count.index =['Yes','No']
colors = ['#008fd5','#e5ae37']

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index, autopct='%1.1f%%', colors=colors)
plt.title("'Eat_High_Caloric_Food_Frequently' Distribution")

#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 7 Vegetable Consumption Frequency

# In[30]:


#Checking the total count of unique values in the column 
DataDF['Vegetable_Consumption_Frequency'].value_counts()


# In[31]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Vegetable_Consumption_Frequency',palette='muted')
plt.title('Distribution')
plt.show()


# In[101]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Vegetable_Consumption_Frequency'].value_counts()
colors = ['#008fd5','#e5ae37','#fc4f30']
explode =[0.1,0,0]

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index,explode=explode,startangle=90, autopct='%1.1f%%', colors=colors)
plt.title("'Vegetable_Consumption_Frequency' Distribution")
startangle=90
#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 8 Number Of Main Meals Daily

# In[39]:


#Checking the total count of unique values in the column 
DataDF['Number_Of_Main_Meals_Daily'].value_counts()


# In[40]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Number_Of_Main_Meals_Daily',palette='muted')
plt.title('Distribution')
plt.show()


# In[102]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Number_Of_Main_Meals_Daily'].value_counts()
colors = ['#008fd5','#e5ae37','#fc4f30','#6d904f']
explode =[0.1,0,0,0]

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index,explode=explode,startangle=90, autopct='%1.1f%%', colors=colors)
plt.title("'Number_Of_Main_Meals_Daily' Distribution")

#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 9 Consumption Of Food Between Meal

# In[46]:


#Checking the total count of unique values in the column
DataDF['Consumption_Of_Food_Between_Meal'].value_counts()


# In[47]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Consumption_Of_Food_Between_Meal',palette='muted')
plt.title('Distribution')
plt.show()


# In[103]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Consumption_Of_Food_Between_Meal'].value_counts()
count.index =['Sometimes','Frequently','Always','No']
colors = ['#008fd5','#fc4f30','#6d904f','#e5ae37']
explode =[0,0,0,0.1]

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index,explode=explode ,startangle=60,autopct='%1.1f%%', colors=colors)
plt.title("'Consumption_Of_Food_Between_Meal' Distribution")

#Adding legend
plt.legend(count.index,loc=(1.5, .5))

plt.show()


# # 10 Smoking

# In[66]:


#Checking the total count of unique values in the column 
DataDF['Smoking'].value_counts()


# In[67]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Smoking',palette='muted')
plt.title('Distribution')
plt.show()


# In[104]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Smoking'].value_counts()
count.index =['No','Yes']
colors = ['#008fd5','#fc4f30']

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index, autopct='%1.1f%%', colors=colors)
plt.title("'Smoking' Distribution")

#Adding legend
plt.legend(count.index,loc=(1.5, .5))

plt.show()


# # 11 Liquid Intake Daily

# In[71]:


#Descriptive Summary of column 
DataDF['Liquid_Intake_Daily'].describe()


# In[72]:


#Skewness And Kurtosis
# Calculating the skewness of the column
skewness = DataDF['Liquid_Intake_Daily'].skew().round(2)
print("Skewness of column 'Liquid_Intake_Daily':", skewness)

# Calculating the kurtosis of the column
kurtosis = DataDF['Liquid_Intake_Daily'].kurtosis().round(2)
print("Kurtosis of column 'Liquid_Intake_Daily':", kurtosis)


# #A skewness value of -0.1 indicates a very slight negative skewness.
# Slightly negative skewness suggests that there may be a few individuals with lower liquid intake compared to the majority, but the distribution is close to symmetrical.

# #A kurtosis value of -0.88 indicates that the distribution has lighter tails than a normal distribution (platykurtic).
# Negative kurtosis suggests that the distribution has fewer extreme values in the tails and a flatter peak compared to a normal distribution.

# In[73]:


#Boxplot
#Creating the boxplot using seaborn
ax = sns.boxplot(x='Liquid_Intake_Daily', data=DataDF, color='#008fd5')

#Adding a title to the plot
ax.set_title('Distribution')

plt.show()


# In[76]:


#Plotting the distribution of the column by histogram
plt.figure(figsize=(10,5))
colors = ['#008fd5','#e5ae37']
sns.histplot(x='Liquid_Intake_Daily',data=DataDF,hue='Obesity_Level',multiple='stack',
             bins='auto',stat='frequency',kde=True,color=colors,palette='colorblind')
plt.xticks(np.arange(0.75,3.05,0.25))
plt.show()


# # 12 Calorie Consumption Monitoring

# In[77]:


#Checking the total count of unique values in the column 
DataDF['Calorie_Consumption_Monitoring'].value_counts()


# In[78]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Calorie_Consumption_Monitoring',palette='muted')
plt.title('Distribution')
plt.show()


# In[80]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Calorie_Consumption_Monitoring'].value_counts()
count.index =['No','Yes']
colors = ['#008fd5','#e5ae37']

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index, autopct='%1.1f%%', colors=colors)
plt.title("'Calorie_Consumption_Monitoring' Distribution")

#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 13 Physical Activity

# In[81]:


#Checking the total count of unique values in the column 
DataDF['Physical_Activity'].value_counts()


# In[82]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Physical_Activity',palette='muted')
plt.title('Distribution')
plt.show()


# In[83]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Physical_Activity'].value_counts()
colors = ['#008fd5','#e5ae37','#fc4f30','#6d904f']
explode =[0.1,0,0,0]

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index, explode=explode,startangle=90,autopct='%1.1f%%', colors=colors)
plt.title("'Physical_Activity' Distribution")

#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 14 Time Using Technological Devices

# In[84]:


#Descriptive Summary of column 'Age'
DataDF['Time_Using_Technological_Devices'].describe()


# In[85]:


#Skewness And Kurtosis
# Calculating the skewness of the column
skewness = DataDF['Time_Using_Technological_Devices'].skew().round(2)
print("Skewness of column 'Time_Using_Technological_Devices':", skewness)

# Calculating the kurtosis of the column
kurtosis = DataDF['Time_Using_Technological_Devices'].kurtosis().round(2)
print("Kurtosis of column 'Time_Using_Technological_Devices':", kurtosis)


# #A skewness value of 0.62 indicates a positively skewed distribution.
# Positively skewed distributions have a long right tail, suggesting that there may be some individuals with higher values of time using technological devices compared to the majority.

# #A kurtosis value of -0.55 indicates that the distribution has lighter tails than a normal distribution (platykurtic).
# Negative kurtosis suggests that the distribution has fewer extreme values in the tails and a flatter peak compared to a normal distribution.

# In[86]:


#Boxplot
#Creating the boxplot using seaborn
ax = sns.boxplot(x='Time_Using_Technological_Devices', data=DataDF, color='#008fd5')

#Adding a title to the plot
ax.set_title('Distribution')

plt.show()


# In[87]:


#Plotting the distribution of the column by histogram
plt.figure(figsize=(10,5))
colors = ['#008fd5','#e5ae37']
sns.histplot(x='Time_Using_Technological_Devices',data=DataDF,hue='Obesity_Level',multiple='stack',
             bins='auto',stat='frequency',kde=True,color=colors,palette='colorblind')
plt.xticks(np.arange(0,2.05,0.25))
plt.show()


# # 15 Alcohol Consumption

# In[88]:


#Checking the total count of unique values in the column 'Gender'
DataDF['Alcohol_Consumption'].value_counts()


# In[89]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Alcohol_Consumption',palette='muted')
plt.title('Distribution')
plt.show()


# In[96]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Alcohol_Consumption'].value_counts()
count.index =['Sometimes','No','Frequently','Always']
colors = ['#008fd5','#e5ae37','#6d904f','#fc4f30']
explode =[0,0,0,0.3]

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index,explode=explode,startangle=180, autopct='%1.1f%%', colors=colors)
plt.title("'Alcohol_Consumption' Distribution")

#Adding legend
plt.legend(count.index,loc=(1, .5))

plt.show()


# # 16 Type Of Transportation

# In[97]:


#Checking the total count of unique values in the column 'Gender'
DataDF['Type_Of_Transportation'].value_counts()


# In[98]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Type_Of_Transportation',palette='muted')
plt.title('Distribution')
plt.show()


# In[119]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Type_Of_Transportation'].value_counts()
count.index =['Public Transportation','Automobile','Walking','Motorbike','Bike']
colors = ['#008fd5','#e5ae37','#fc4f30','#6d904f','#BA55D3']
explode =[0,0,0.2,0.4,0.6]

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(5,5))
plt.pie(count.values, labels=count.index,explode=explode,startangle=30, autopct='%1.1f%%', colors=colors)
plt.title("'Type_Of_Transportation' Distribution")

#Adding legend
plt.legend(count.index,loc=(1.5, .5))

plt.show()


# # 17 Obesity Level

# In[120]:


#Checking the total count of unique values in the column 
DataDF['Obesity_Level'].value_counts()


# In[121]:


#Ploting a countplot
plt.figure(figsize=(5,3))
sns.countplot(data=DataDF, x='Obesity_Level',palette='muted')
plt.title('Distribution')
plt.show()


# In[123]:


#Piechart
#Counting the number of occurrences of each category in the column
count = DataDF['Obesity_Level'].value_counts()
count.index =['Obesity','Overweight','Normal weight','Underweight']
colors = ['#008fd5','#e5ae37','#fc4f30','#6d904f']
explode =[0.1,0,0,0]

#Creating  pie chart with percentage using seaborn
plt.figure(figsize=(4,4))
plt.pie(count.values, labels=count.index, explode=explode,startangle=90,autopct='%1.1f%%', colors=colors)
plt.title("'Obesity_Level' Distribution")

#Adding legend
plt.legend(count.index,loc=(1.5, .5))

plt.show()


# ## FEATURE SELECTION BY CORRELATION ANALYSIS

# In[133]:


#Finding the relationship between each feature to the target feature by using Pearson's correlation
plt.figure(figsize=(10,8))
corr_matrix = DataDF.corr()
corr_matrix =corr_matrix.round(1)
cmap = sns.color_palette("coolwarm", as_cmap=True)
sns.heatmap(corr_matrix, annot=True, cmap=cmap,linewidth=1,center=0,fmt='.3f')
plt.title('Correlation Matrix')
plt.show()


# In[130]:


#Finding the relationship between each feature to the target feature by using Pearson's correlation
plt.figure(figsize=(10,8))

#Creating correlation matrix
corr_matrix = DataDF.corr()

#Creating mask
mask = np.zeros_like(corr_matrix)
mask[np.triu_indices_from(mask)] = True

#Heatmap
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr_matrix,mask=mask, annot=True, cmap=cmap,linewidth=1,center=0,fmt='.3f', cbar_kws={"shrink": .5})
plt.title('Correlation Matrix')
plt.show()


# In[ ]:





# In[ ]:




