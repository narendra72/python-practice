#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd


# data read    csv data are converted into dataframe 
data = pd.read_csv('matches.csv')
data


# to feching single column 
data['city']


type(data['city'])


# for to fetching multiple column  ->  pass list inside [ ]
data[['city','player_of_match','winner']]


type(data[['city','player_of_match','winner']])


# for to fetching row data    --> iloc[ ]
data.iloc[1]


data.iloc[2:5]


data.loc[0,"team1"]


data.iloc[0,4]


data.iloc[-1]


# maximum matchs played by any team 
data1 = data['team1'].value_counts() + data['team2'].value_counts() 
data1


# .sort_value() function   -> sort values 
data1.sort_values()       # -> by default ascending


data1.sort_values(ascending = False)


data.sort_values('win_by_runs').tail()


data.sort_values('win_by_runs',ascending=False).head()


# .drop_duplicates() 
data.drop_duplicates(subset='season')


data.drop_duplicates(subset='season',keep='last') 




