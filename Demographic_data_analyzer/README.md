###Demographic Data Analyzer

*Assignment

In this coding challenge, your task is to perform a comprehensive analysis of demographic data using the powerful Pandas library. You'll be working with a dataset extracted from the 1994 Census database, which provides valuable insights into various demographic attributes. Here's a glimpse of the dataset:


| age	| workclass |	fnlwgt |	education |	education-num |	marital-status |	occupation |	relationship |	race |	sex |	capital-gain |	capital-loss |	hours-per-week |	native-country |	salary |
|     :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      |   :---:      | 
39	| State-gov |	77516	| Bachelors  |	 	13 |	Never-married |	Adm-clerical |	Not-in-family |	White  |		Male |	2174 |	0 |	40 |	United-States |	<=50K |
50 |	Self-emp-not-inc |	83311 |	Bachelors  |		13 |	Married-civ-spouse |	Exec-managerial  |		Husband	| White  |		Male |	0	 | 0 |	13 | 	United-States |	<=50K |
38 |	Private |	215646 |	HS-grad  |		9 |	Divorced |	Handlers-cleaners |	Not-in-family |	White  |		Male |	0 |	0	| 40 |	United-States |	<=50K |
53 |	Private |	234721 |	11th  |		7 |	Married-civ-spouse |	Handlers-cleaners |	Husband |	Black  |		Male |	0 |	0 |	40 |	United-States |	<=50K |
28 |	Private |	338409 |	Bachelors  |	 	13 |	Married-civ-spouse |	Prof-specialty |	Wife |	Black  |		Female |	0 |	0 |	40 |	Cuba |	<=50K |



*Key Questions to Answer:

- How many people of each race are represented in this dataset? Provide a Pandas series with race names as the index labels (race column).
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of people who work the minimum hours per week have a salary of more than 50K?
- Which country has the highest percentage of people earning more than 50K, and what is that percentage?
- Identify the most popular occupation among individuals who earn more than 50K in India.

*Testing
For development, you can use main.py to test your functions. Click the "run" button and main.py will run.

*Dataset Source
The dataset used in this assignment was sourced from the UCI Machine Learning Repository and originally compiled by:

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.
