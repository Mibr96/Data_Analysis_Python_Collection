import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalize data for 'cholesterol' and 'gluc'
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using 'pd.melt' using specified columns
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Create the categorical plot
    catplot = sns.catplot(data=df_cat, x="variable", hue="value", col="cardio", kind="count")
    catplot.set_ylabels("total")
    fig = catplot.fig

    # Save the figure
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                 & (df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975)))
                 & (df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975)))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))

    # Create the heatmap
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask)
    fig = plt.gcf()
    plt.show()

    # Save the figure
    fig.savefig('heatmap.png')
    return fig