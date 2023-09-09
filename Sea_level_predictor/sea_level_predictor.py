import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_level = pd.read_csv('epa-sea-level.csv')
    x = sea_level['Year']
    y = sea_level['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y, label='Data')

    # Perform linear regression and plot lines
    def plot_linreg(x, y, label):
        slope, intercept, r, p, std_err = linregress(x, y)
        x_pred = list(range(1880, 2051))
        y_pred = [slope * year + intercept for year in x_pred]
        plt.plot(x_pred, y_pred, label=label)

    # Create first line of best fit for the entire dataset
    plot_linreg(x, y, 'Linear Regression (1880-2050)')

    # Create second line of best fit for data from 2000 to 2013
    x2 = x[x >= 2000]
    y2 = y[x >= 2000]
    plot_linreg(x2, y2, 'Linear Regression (2000-2050)')

    # Add labels, legend, and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
