#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd


data = pd.read_csv('match.csv')
data


data.rename(columns={'city':'place'})


# set_index() and reset_index()

data.set_index('id')


data.reset_index()




