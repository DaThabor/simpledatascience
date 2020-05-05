# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:20:08 2020

@author: ThaborWalbeek
"""

#*****************************************************
#**** Load all packages into the environment *********
#*****************************************************

import pandas as pd
import numpy as np
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
from sklearn.datasets import load_boston