# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:26:07 2023

@author: KENDOLESANTHOSHKUMAR
"""

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as pt

df=pd.read_csv("C:/Users/KENDOLESANTHOSHKUMAR/Downloads/Avocado.csv")
df.head()

df.tail()

df.info

df.describe()

df.shape

df.dtypes

df.columns

df=df[['Date','AveragePrice','Total Volume','4046','4225','4770','Total Bags','type','region']]
df

df=df.drop('Date',axis=1)

df.head()

df.isnull().sum()

df.groupby('AveragePrice').mean()

df[['AveragePrice','Total Volume']]

#Data Visualization

pt.figure(figsize=(10,5))
df.hist()

pt.figure(figsize=(12,9))
sb.scatterplot(x='AveragePrice',y='Total Volume',hue='type',data=df)

pt.figure(figsize=(10,5))
pt.title("Distribution of Average Price")
sb.histplot(df['AveragePrice'],color='blue')

pt.figure(figsize=(10,5))
pt.title("Price of Avocado")
sb.boxplot(x='type',y='AveragePrice',data=df,color='red')

pt.figure(figsize=(15,10))
pt.title("AveragePrice of the PArticular Region")
pt.xticks(rotation='vertical')
sb.boxplot(x='region',y='AveragePrice',data=df,color='red')

pt.figure(figsize=(10,5))
pt.xlabel('Avacado type')
pt.ylabel('AveragePrice')
sb.barplot(x='type',y='AveragePrice',data=df)

pt.figure(figsize=(12,6))
pt.xlabel('Region')
pt.ylabel('AveragePrice')
pt.title("Average Price By Region")
pt.xticks(rotation=90)
sb.scatterplot(x='region',y='AveragePrice',data=df)

correlation_matrix=df.corr()
pt.figure(figsize=(8,6))
pt.title("Correlation Matrix")
sb.heatmap(correlation_matrix,annot=True)
pt.show()

pt.hist(df['AveragePrice'],bins=20,color='yellow')
pt.xlabel('AveragePrice')
pt.ylabel('Frequency')
pt.title('Distributon of Average Price')

pt.figure(figsize=(10,5))
pt.title("TotalVolume VS AveragePrice")
pt.xlabel("TotalVolume")
pt.ylabel("AveragePrice")
pt.scatter(df['Total Volume'],df['AveragePrice'])
pt.show()

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x=df.drop(columns=['AveragePrice'])
y=df['AveragePrice']

le=LabelEncoder()
encoded=x.copy()
for i in x.select_dtypes(include='object').columns:
    encoded[i]=le.fit_transform(x[i])`

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

print(x_train.shape)

print(x_test.shape)

print(y_train.shape)

print(y_test.shape)

x_train,x_test,y_train,y_test=train_test_split(encoded,y,test_size=0.3,random_state=42)

lr=LinearRegression()
lr.fit(x_train,y_train)

x_pred=lr.predict(x_test)

x_test[0:10]

y_test[0:10]

lr.coef_

lr.intercept_

lr.predict(x_test[0:10])

