#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv(r"E:\drug_use.csv")

df01 = pd.read_csv(r"E:\drug_names.csv")

df02 = pd.read_csv(r"E:\census.csv")


# In[2]:


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)


# In[3]:


df2 = df[['atc','year','sex','age','nusers','country','drug_group']]


# In[4]:


df2.rename(columns = {'nusers':'no. of users'}, inplace = True)


# In[5]:


df3 = pd.merge(df2, df01, on='atc', how='left')


# In[6]:


df2.isnull()


# In[7]:


df2.duplicated()


# In[6]:


df3.dtypes


# In[10]:


df3.groupby(['formalname'])['no. of users'].sum()


# In[11]:


df3.groupby(['country'])['no. of users'].sum()


# In[13]:


df3.groupby(['sex'])['no. of users'].count()


# In[13]:


df3.groupby(['sex'])['no. of users'].sum()


# In[28]:


df3.groupby(['formalname', 'year'])['no. of users'].sum()


# In[15]:


df3.groupby(['formalname', 'sex'])['no. of users'].sum()


# In[17]:


df3.groupby(['country', 'formalname'])['no. of users'].sum()

#DK, NO Selective serotonin reuptake inhibitors, Sertraline
#SE Fluoxetine


# In[18]:


df3.groupby(['formalname', 'age', 'sex'])['no. of users'].sum() 
#SSRI


# In[10]:


df02.groupby(['age'])['cnt'].sum()


# In[29]:


df3.groupby(['drug_group', 'sex'])['no. of users'].sum()

