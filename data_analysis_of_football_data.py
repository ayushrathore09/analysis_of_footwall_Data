# -*- coding: utf-8 -*-
"""Data Analysis of Football Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J9dQ32j2vftpfKvZ_XbWHa_WjJYOlVe8
"""

import pandas as pd
import matplotlib.pyplot as plt

fifa=pd.read_csv(r"c:\Users\user\Downloads\players_20.csv")
fifa.head()

fifa.shape

# to print all the columns present in file:

for col in fifa.columns:
    print(col)

fifa['nationality'].value_counts()

fifa['club'].value_counts()[0:10]
# only top 10 :

# to get top 5 list without getting values:

fifa['nationality'].value_counts()[0:5].keys()

# to get data visualization:
# graph show no of players from particular nationality:

plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:10].keys()),list(fifa['nationality'].value_counts()[0:10]),color='red')
plt.show

# no of players in a particular club :

plt.figure(figsize=(6,6))
plt.bar(list(fifa['club'].value_counts()[0:5].keys()),list(fifa['club'].value_counts()[0:5]),color='green')
plt.show

# to extract two columns from data: we use loc to specify the column name

player_salary = fifa.loc[0:,('short_name','wage_eur')]
player_salary.head()

plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'][0:5]),list(player_salary['wage_eur'][0:5]),color='pink')
plt.show

# arrnging salary in descing order:

player_salary = player_salary.sort_values(by=['wage_eur'],ascending=False)
player_salary.head()

fifa['nationality']=='geramn'

# to find out the german players :

germany = fifa[fifa['nationality']=='Germany']
germany.head(5)

# top 5 highest players :

germany.sort_values(by=['height_cm'],ascending=False).head()

fifa.sort_values(by=['age'],ascending=False).head()

# highest wage in germany :

f1= germany.loc[0:200,('short_name','wage_eur')]
f1.sort_values(by=['wage_eur'],ascending=False).head()

# highest shooting individuals:

fifa.loc[0:,('short_name','shooting')].sort_values(by=['shooting'],ascending=False).head()

# highest defending inviduals from which city:

fifa.loc[0:5,('short_name','defending','nationality')].sort_values(by=['defending'],ascending=False)

# to identify the highest defender , shooting and wages in real madrid:

real_madrid = fifa[fifa['club']=='Real Madrid']
real_madrid.sort_values(by=['club'],ascending =False).head()

real_madrid.sort_values(by=['defending'],ascending=False).head()

x=fifa.loc[0:10,('short_name','weight_kg')].sort_values(by=['weight_kg'],ascending=False)
x

plt.figure(figsize=(8,5))
plt.bar(list(x['short_name'][0:5]),list(x['weight_kg'][0:5]),color='green')
plt.show