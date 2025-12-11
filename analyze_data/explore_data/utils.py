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

def plot_categorical_bar(data_dict, title='Summary', ylabel='Count', ax=None, color='#1f77b4',show=True):
    """Geberate a bar chart for a categorical column"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    s = pd.Series(data_dict)

    s.plot(kind='bar', ax=ax, color=color, rot=0)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_ylabel(ylabel)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    for container in ax.containers:
        ax.bar_label(container)

    if show: 
        plt.show()

    return ax