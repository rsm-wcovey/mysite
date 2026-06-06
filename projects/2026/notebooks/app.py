import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import joblib
from shiny import App, render, ui, reactive

mysite_palette = ['#375a7f', "#ff879b", '#189cd0', "#c46151", "#18bc9c", "#54011a", '#2c3e50']
plt.rcParams['axes.prop_cycle'] = cycler(color=mysite_palette) 

mpipe = joblib.load('../data/mpipe.pkl')

cut_cats=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_cats=['J', 'I', 'H', 'G', 'F', 'E', 'D']
clarity_cats=['I3', 'I2', 'I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

carat = 1
cut = 'Good'
color = 'G'
clarity = 'IF'

large = int((carat > 2))
carat_large = carat * large

x_vals = pd.DataFrame({
    'carat': carat,
    'cut': cut,
    'color': color,
    'clarity': clarity,
    'large': large,
    'carat:large': carat_large
}, index=[0])

y_pred = mpipe.predict(x_vals)

pred_val = y_pred[0][0]
pred_str = f'${pred_val:,.2f}'
print(pred_str)