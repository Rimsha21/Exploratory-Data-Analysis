
# coding: utf-8

# ## Author-  Rimsha Virmani
# 
# ## GRIP @ The Sparks Foundation
# 
# ## Task 5: Exploratory Data Analysis - Retail
# 
# ## Aim: Perform Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# ## As a business manager, try to find out the weak areas where you can work to make more profit.
# ## What all business problems you can derive by exploring the data?
# 
# ## Dataset: https://bit.ly/3i4rbWl
# 

# In[3]:


#Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[4]:


#Importing data
df= pd.read_csv('SampleSuperstore.csv')


# In[5]:


df.head()


# ## Step 1: Data Exploration

# In[6]:


df.describe()


# In[7]:


#checking for missing values in the data
df.isnull().sum()


# In[8]:


#info about the data
df.info()


# In[18]:


#columns inside the data
df.columns


# In[19]:


df['Country'].value_counts()


# In[21]:


df['Ship Mode'].value_counts()


# ## Step 2: Data Visualization

# In[20]:


#correlation matrix and plotting heatmap
corrmat= df.corr()
sns.heatmap(corrmat, annot=True, cmap='RdYlGn')
plt.title('Correlation between variables')


# In[49]:


#plotting pairplot
sns.pairplot(df)


# In[28]:


df.groupby('Ship Mode').groups


# In[33]:


sns.countplot( df['Ship Mode'], color='b')


# In[34]:


#Customer Segments
df['Segment'].value_counts()


# In[35]:


sns.countplot(df['Segment'], color='g')


# In[36]:


#Category Wise Analysis
sns.countplot(df['Category'])
plt.title('Categories of Products')


# In[37]:


#Region-Wise ordered product categories
sns.countplot(df['Region'], hue= df['Category'])


# In[50]:


# Total profit vs sales
fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total profit VS sales ")
sns.barplot(data=df.groupby('Sub-Category')['Sales','Profit'].agg(sum),x='Sales',y='Profit',ax=axes[1])
df.groupby('Sub-Category')['Sales','Profit'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show()


# In[51]:


fig,ax= plt.subplots(1,1,figsize=(12,7))
sns.countplot(df['Quantity'],hue=df['Region'])
plt.show()


# In[39]:


# Quantity of different Sub-Categories Ordered

df['Sub-Category'].value_counts()


# In[41]:


# Region Wise Analysis
rw= df.groupby('Region')['Profit','Sales'].agg('sum')
rw.plot.bar()
plt.title('Region wise profit and sales')


# In[42]:


df['Region'].value_counts()


# In[43]:


#City wise analysis
df['City'].value_counts()


# In[45]:


len(df['City'])


# ## Conclusion

# In[52]:


The exploratory data analysis on the given dataset has been performed successfully.
It can be seen that:
1. The features Profit and Discounts are highly related.
2. Over Less quantity of products also the sales were high.

3. The mode of shipping doesn not affect much to the sales

