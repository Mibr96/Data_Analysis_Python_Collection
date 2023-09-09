# Medical Data Visualizer

## Assignment
In this project, you will utilize matplotlib, seaborn, and pandas to visualize and perform calculations on medical examination data. The dataset contains valuable information collected during medical examinations, including body measurements, blood test results, and lifestyle choices. Your goal is to explore the relationships between cardiac disease, body measurements, blood markers, and lifestyle choices using this dataset.

## Data Description
- Age: Objective Feature (age in days)
- Height: Objective Feature (height in centimeters)
- Weight: Objective Feature (weight in kilograms)
- Gender: Objective Feature (categorical)
- Systolic Blood Pressure: Examination Feature (ap_hi)
- Diastolic Blood Pressure: Examination Feature (ap_lo)
- Cholesterol: Examination Feature (1: normal, 2: above normal, 3: well above normal)
- Glucose: Examination Feature (1: normal, 2: above normal, 3: well above normal)
- Smoking: Subjective Feature (binary)
- Alcohol Intake: Subjective Feature (binary)
- Physical Activity: Subjective Feature (binary)
- Presence or Absence of Cardiovascular Disease: Target Variable (binary)

## File Name
File name: medical_examination.csv

## Tasks
1 Create a chart similar to examples/Figure_1.png, displaying the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.

2 Use the data to complete the following tasks in medical_data_visualizer.py:

- A dd an overweight column to the data. Determine if a person is overweight by calculating their BMI (Body Mass Index), which is obtained by dividing their weight in kilograms by the square of their height in meters. If the BMI is > 25, mark the person as overweight (value 1), otherwise, mark them as not overweight (value 0).

- Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If it's more than 1, set it to 1.

- Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). Split the dataset by Cardio so that there is one chart for each cardio value. The chart should resemble examples/Figure_1.png.

- Clean the data by filtering out incorrect patient segments, such as those with diastolic pressure higher than systolic pressure (df['ap_lo'] <= df['ap_hi']), height below the 2.5th percentile (df['height'] >= df['height'].quantile(0.025)), height above the 97.5th percentile, weight below the 2.5th percentile, and weight above the 97.5th percentile.

- Create a correlation matrix using the dataset and plot it using seaborn's heatmap(). Mask the upper triangle. The chart should resemble examples/Figure_2.png.
