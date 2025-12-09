import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_basic_stats(df, col_name):
    return df[col_name].describe()

def plot_distribution(df, col_name, ax=None):
    """Creates the histogram/boxplot"""
    pass

def analyze_correlations(df):
    """creates Heatmaps"""
    pass

def plot_histogram(df, column_name, ax=None, color='skyblue'):
    """"""
    pass

def plot_categorical_bar(df, column_name, ax=None):
    """"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))