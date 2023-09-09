import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Register matplotlib converters
register_matplotlib_converters()

# Import and preprocess the data
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index('date', inplace=True)

# Clean the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw a line plot
    plt.figure(figsize=(12, 6))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    sns.lineplot(data=df, legend=False)
    plt.savefig('line_plot.png')
    plt.close()

def draw_bar_plot():
    # Create a monthly bar plot
    df_bar = df.copy()
    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.strftime('%B')
    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean().round().astype(int).reset_index()
    
    # Add missing data for the first four months of 2016
    missing_data = {
        "Year": [2016] * 4,
        "Month": ['January', 'February', 'March', 'April'],
        "value": [0] * 4
    }
    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw a bar plot
    plt.figure(figsize=(12, 6))
    plt.title("Daily freeCodeCamp Forum Average Page Views per Month")
    chart = sns.barplot(data=df_bar, x="Year", y="value", hue="Month", palette="tab10")
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')
    plt.savefig('bar_plot.png')
    plt.close()

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Create subplots for yearly and monthly box plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Yearly box plot
    sns.boxplot(data=df_box, x="Year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Monthly box plot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="Month", y="value", order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save the box plot image
    plt.savefig('box_plot.png')
    plt.close()
