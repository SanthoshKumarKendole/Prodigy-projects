# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 22:00:11 2023

@author: KENDOLESANTHOSHKUMAR
"""

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np



#reading all the data 

df=pd.read_csv("C:/Users/KENDOLESANTHOSHKUMAR/Downloads/hospitals.csv")
print(df)


variable_count=df['Variable'].value_counts()
bar_width=5
x=range(len(variable_count.index))

pt.bar(variable_count.index,variable_count.values)
pt.xlabel('Variable')
pt.ylabel('Measures Per Million Population')
pt.title('HealthCare Resources')


pt.xticks(x,variable_count.index,rotation=45)
pt.tight_layout()
pt.show()