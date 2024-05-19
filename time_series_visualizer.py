import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar

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
    # Group the dataframe by year and month
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    # Rename index columns to 'Year' and 'Month'
    df_bar.index.names = ['Year', 'Month']
    # Rename column names
    df_bar = df_bar.rename(columns=({'Page Views': 'Average Page Views'}))
    # Bring out index columns
    df_bar = df_bar.reset_index()
    # Rename months from ints to names
    df_bar['Month'] = df_bar['Month'].apply(lambda x: calendar.month_name[x])
    # Put index back in
    df_bar.index=[df_bar['Year'],df_bar['Month']]
    # Drop extra columns
    df_bar = df_bar.drop(['Year','Month'], axis=1)

    #Draw bar plot
    fig = sns.catplot(
        data=df_bar,
        x='Year', 
        y="Average Page Views", 
        kind="bar",
        hue="Month",
        legend='full',
        legend_out=False,
        hue_order=['January','February','March','April','May','June','July','August','September','October','November','December']
    ).fig

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.Date]
    df_box['month'] = [d.strftime('%b') for d in df_box.Date]

    # Draw box plots (using Seaborn)
    # Set up plots and sizing
    fig, ax=plt.subplots(1,2,figsize=(28.8,10.8))
    # Make sure plots do not overlap
    fig = plt.tight_layout(pad=5)
    # Plot year-wise box plot
    fig = sns.boxplot(
        data=df_box,
        x='year',
        y='Page Views',
        orient="v",
        legend=False,
        ax=ax[0],
        native_scale=False,
        gap=0.2,
        fliersize=2
    ).set_title('Year-wise Box Plot (Trend)').get_figure()
    # Draw month-wise boxplot 
    fig = sns.boxplot(
        data=df_box,
        x='month',
        y='Page Views',
        orient="v",
        legend=False,
        ax=ax[1],
        native_scale=False,
        gap=0.2,
        fliersize=2,
        order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ).set_title('Month-wise Box Plot (Seasonality)').get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
