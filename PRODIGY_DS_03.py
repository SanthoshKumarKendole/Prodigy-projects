import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

df=pd.read_csv("C:/Users/KENDOLESANTHOSHKUMAR/Downloads/bank.csv")
print(df)

df.head()

df.tail()

df.shape

df.columns

df.info()

df.describe()


df.isnull().sum()

#Visualization

pt.figure(figsize=(16,9))
sb.countplot(x='job',data=df)

sb.countplot(x='job',data=df)

sb.countplot(x='marital',data=df)

sb.countplot(x='education',data=df)

sb.countplot(x='deposit',data=df)

sb.countplot(x='default',data=df)

fig,axes=pt.subplots(nrows=2,ncols=2,figsize=(12,10))
df.plot(kind='hist',y='age',bins=70,color='red',ax=axes[0][0])
df.plot(kind='hist',y='balance',bins=10,color='blue',ax=axes[0][1])
df.plot(kind='hist',y='duration',bins=60,color='yellow',ax=axes[1][0])
df.plot(kind='hist',y='campaign',bins=10,color='green',ax=axes[1][1])
pt.show()

pt.figure(figsize=(16,9))
sb.pairplot(data=df,hue='default')

hey_df=df.select_dtypes(exclude=[object])
hey_df.corr()

pt.figure(figsize=(16,9))
sb.heatmap(hey_df.corr(),annot=True)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df['job']=le.fit_transform(df['job'])
df['marital']=le.fit_transform(df['marital'])
df['education']=le.fit_transform(df['education'])
df['deposit']=le.fit_transform(df['deposit'])
df['default']=le.fit_transform(df['default'])
df['loan']=le.fit_transform(df['loan'])
df['contact']=le.fit_transform(df['contact'])
df['poutcome']=le.fit_transform(df['poutcome'])
df['housing']=le.fit_transform(df['housing'])
df['month']=le.fit_transform(df['month'])

df.head()

df.drop(['pdays','previous','poutcome'],axis=1)
df.head()

X=df.drop(['default'],axis=1)
y=df['default']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


from sklearn.tree import DecisionTreeClassifier
dc=DecisionTreeClassifier()
dc.fit(X_train,y_train)

y_pred=dc.predict(X_test)

y_pred

#Evaluating the model

from sklearn.metrics import accuracy_score,confusion_matrix
acc=accuracy_score(y_pred,y_test)*100
print(acc)

cm=confusion_matrix(y_pred,y_test)
print(cm)

