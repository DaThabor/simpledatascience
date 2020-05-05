# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:27:11 2020

@author: ThaborWalbeek
"""

#*******************************************************
#** Load data dictionary for Linear Regression Models **
#*******************************************************

# Boston dataset

import pandas as pd
from IPython.display import display, HTML
from sklearn.datasets import load_boston

boston_ds = load_boston()
print(boston_ds.DESCR)

# Advertisement dataset

print("\n")
print("The Data Dictionary for the advertisement data set")
print("\n")
print(".. _advertisement_dataset:")
print("\n")
print("Advertisement dataset")
print("---------------------------")
print("\n")
print("Data Set Characteristics:")
print("\n")
adv_dictionary = {'Column':['Sales', 'TV', 'Radio', 'Newspaper'], 
        'Description':["Sales amount in thousands USD",
                       "Budget spent on TV advertismeent",
                       "Budget spent on Radio advertisement",
                       "Budget spent on Newspaper advertisement" ]} 

adv_dictionary = pd.DataFrame(adv_dictionary)

display(HTML(adv_dictionary.to_html()))

