import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# Read csv, parse dates, use 'date' as the index column, rename 'date' column to 'Date' and 'value' column to 'Page Views'
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=True,index_col='Date', header = 0, names=['Date','Page Views'])

# Clean data
# Create a mask to filter out below 2.5% Quantile and 97.5% Quantile
quantile_mask = (df['Page Views'] >= df['Page Views'].quantile(0.025)) & (df['Page Views'] <= df['Page Views'].quantile(1-0.025))
# Use mask on dataframe
df = df[quantile_mask]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(32,10))
    # Name the title "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Plot the data
    plt.plot(df.index,df['Page Views'],'r')
    # Add x and y labels
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
