import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # Calculate the number of each race represented in the dataset
    race_count = df['race'].value_counts()

    # Calculate the average age of men
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

    # Calculate the percentage of people with a Bachelor's degree
    percentage_bachelors = (len(df[df['education'] == 'Bachelors']) / len(df)) * 100

    # Calculate the percentage of people with advanced education (>50K)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = (len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100
    lower_education_rich = (len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100

    # Find the minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Calculate the percentage of people who work the minimum hours and earn >50K
    num_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
    rich_percentage = (len(num_min_workers) / len(df[df['hours-per-week'] == min_work_hours])) * 100

    # Find the country with the highest percentage of people earning >50K
    earn_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    pop_per_native_country = df['native-country'].value_counts()
    result = (earn_by_country / pop_per_native_country).sort_values(ascending=False)
    highest_earning_country = result.index[0]
    highest_earning_country_percentage = result.iloc[0] * 100

    # Identify the most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # Print or return the results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors:.1f}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich:.1f}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich:.1f}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage:.1f}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage:.1f}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }