# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:19:42 2023

@author: KENDOLESANTHOSHKUMAR
"""

import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sb
import numpy as np

df=pd.read_csv("C:/Users/KENDOLESANTHOSHKUMAR/Downloads/laptops_train.csv")
print(df)

df.head()

df.isnull().sum()

df['Model Name'].value_counts()

df.drop('Model Name',axis=1,inplace=True)

df.info()

df['Screen Size'].unique()

df['Screen Size'].str.replace('"','')

df['Screen Size']=df['Screen Size'].str.replace('"','')

df.head()

df['Screen'].value_counts()

def screen(display):
    if "Touchscreen" in display:
        return "Touch"
    else:
        return "Non Touch"

df['Screen'].apply(screen).value_counts()

df['Screen']=df['Screen'].apply(screen)

df['Screen'].value_counts().plot(kind='bar')
pt.show()

df.head()

df["CPU"].unique()

def cpu(cpu):
    if "i3" in cpu:
        return "i3"
    elif 'i5' in cpu:
        return 'i5'
    elif 'i7' in cpu:
        return 'i7'
    return 'others'

df['CPU']=df['CPU'].apply(cpu)

pt.figure(figsize=(10,5))
df['CPU'].value_counts().plot(kind='bar')
pt.show()

df['CPU'].value_counts()

df['Storage'].unique()

df.drop("Storage",axis=1,inplace=True)

df.head()

df['RAM'].unique()

df['RAM'].str.split('GB').str[0]

df['RAM']=df['RAM'].str.split('GB').str[0]

df['RAM'].unique()

df.head()

df['GPU'].unique()

def gpu(gpu):
    if "Nvidia" in gpu:
        return "Nvidia"
    elif "AMD" in gpu:
        return "AMD"
    elif "Intel" in gpu:
        return "Intel"
    else:
        return "others"
    

df['GPU'].apply(gpu)

df['GPU']=df["GPU"].apply(gpu)

df['GPU'].unique()

df['GPU'].value_counts().plot(kind='bar')
pt.show()

df.head()

df['Operating System'].value_counts()

df['Operating System'].str.replace('macOS','Mac OS').value_counts()

df['Operating System']=df['Operating System'].str.replace('macOS','Mac OS')

df['Operating System Version'].value_counts()

df['Operating System Version'].isnull().sum()

df['Operating System Version'].unique()

df['Operating System Version'].fillna(df['Operating System Version'].mode()[0])

df['Operating System Version']=df['Operating System Version'].fillna(df['Operating System Version'].mode()[0])

df['Operating System Version'].unique()

df['Operating System Version'].str.replace('X','10')

df['Operating System Version']=df['Operating System Version'].str.replace('X','10')

df['Operating System Version'].unique()

df['Operating System Version'].str.replace('10 S','10').unique()

df['Operating System Version']=df['Operating System Version'].str.replace('10 S','10')

df['Operating System Version'].unique()

df['Operating System Version'].value_counts().plot(kind='bar')
pt.show()

df.head()

df['Weight'].unique()

df['Weight'].str.split('kg').str[0].unique()

df['Weight']=df['Weight'].str.split('kg').str[0]

df.head()

df['Price'].unique()

df['Price'].astype('str').str[:7]

df['Price']=df['Price'].astype('str').str[:7]

df['Price'].unique()

df.info()

df.head()

df['Screen Size']=df['Screen Size'].astype('float')
df['RAM']=df['RAM'].astype('int')
df['Operating System Version']=df['Operating System Version'].astype('int')
df['Weight']=df['Weight'].astype('float')
df['Price']=df['Price'].astype('int')

df.info()

df.head()

df.select_dtypes(include='object').nunique()

df["Manufacturer"].unique()

def brand(company):
    if company in ['Apple',"HP",'Dell','LG']:
        return "Major Brands"
    elif company in ['Acer','Asus','Razer','MSI']:
        return "Gaming Brands"
    elif company in ['Chuwi','Toshiba','Vero']:
        return "Chinese Brands"
    return "others brands"

df['Manufacturer'].apply(brand)

df['Manufacturer']=df['Manufacturer'].apply(brand)

df['Manufacturer'].value_counts().plot(kind='bar')
pt.show()

df.select_dtypes(include='object').nunique()

# Data Analysis

variable= df.select_dtypes(include='object')

fig,axis= pt.subplots(nrows=3,ncols=2,figsize=(15,10))
axis=axis.flatten()


for i , var in enumerate(variable):
    sb.countplot(y=var,data=df,ax=axis[i])
    axis[i].set_title(var)
pt.tight_layout()
pt.show()

variabe = df.select_dtypes(include='object')

fig, axs = pt.subplots(nrows=3,ncols=2,figsize=(15,10))

for i ,var in enumerate(variable):
    if i < len(axs.flat):
        
        cat_counts = df[var].value_counts().head()
        
        axs.flat[i].pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%' ,startangle=90)
        axs.flat[i].set_title(f'{var} Distribution')

fig.tight_layout()
pt.show()



