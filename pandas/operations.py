#!/usr/bin/env python
# coding: utf-8

import numpy as pn
import pandas as pd
import csv


data = pd.read_csv('matches.csv')
data


type(data)


data.head()  


data.tail()


data.shape


data.info()


data.describe()


# conditonal filtering 
mask = data['city']=='Pune'
data[mask]


data[mask].shape


mask1 = data['city']=='Pune'
mask2 = data['date']> '2016-01-21'
data[mask1 & mask2]


data[mask1 & mask2].shape[0]


# the value_counts() function  --> apply on categorical data    used for frequency analysis of categorical data
data['winner'].value_counts()


data['venue'].value_counts()


# graph using plot function
import matplotlib.pyplot as plt


data['winner'].value_counts().plot(kind='pie')


data['winner'].value_counts().head(7).plot(kind='bar')


data['win_by_runs'].plot(kind='hist')


data.plot()




