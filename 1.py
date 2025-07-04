'''
Mock_MatplotLib

1 Problem 1 : https://tinyurl.com/MatplotlibInterviewQuestion
'''

'''
Problem:

Imagine you are working for a travel agency named "Wanderlust Adventures." Your team has been assigned a project to analyze and visualize the travel data for the past year. The data includes information about various destinations, the number of travelers per month, and the revenue generated. As the data analyst, you decide to use Matplotlib to create insightful visualizations.
As a data analyst at "Wanderlust Adventures," you have been given a dataset containing monthly travel data for different destinations. The dataset includes information about the number of travelers and the revenue generated each month. Your task is to create three visualizations using Matplotlib: a line plot, a pie chart, and a scatter plot.

Line Plot: Create a line plot using Matplotlib that illustrates the trend of both traveler count and revenue over the past year. The x-axis should represent the months, while the y-axis should represent the traveler count and revenue, respectively. The line plot should display two lines, one for traveler count and another for revenue, showcasing their trends over time.
Pie Chart: Generate a pie chart using Matplotlib to display the distribution of traveler count among the top five destinations for the entire year. Each slice of the pie should represent a destination, and its size should correspond to the proportion of travelers visiting that particular destination.
Scatter Plot: Create a scatter plot using Matplotlib that demonstrates the relationship between the number of travelers and the revenue generated for each month. Each data point on the scatter plot should represent a month, with the x-coordinate representing the traveler count and the y-coordinate representing the revenue generated.
Note: Use the file called "travel.csv"

 
[ ]
#Please use the file travel.csv for the above#The dataset is available at https://tinyurl.com/travelDataset
# '''

import pandas as pd

file_path = "/mnt/data/travel.csv"
df = pd.read_csv(file_path)

df.head()

import matplotlib.pyplot as plt # type: ignore
import numpy as np

monthly_data = df.groupby('Month').agg({'Travelers': 'sum', 'Revenue': 'sum'}).reindex([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Line Plot: Travelers and Revenue over months
plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data['Travelers'], marker='o', label='Travelers')
plt.plot(monthly_data.index, monthly_data['Revenue'], marker='o', label='Revenue')
plt.title('Monthly Travelers and Revenue')
plt.xlabel('Month')
plt.ylabel('Count / Revenue')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


destination_data = df.groupby('Destination')['Travelers'].sum()
top_5_destinations = destination_data.sort_values(ascending=False).head(5)

# Pie Chart: Top 5 destinations by traveler count
plt.figure(figsize=(8, 8))
plt.pie(top_5_destinations, labels=top_5_destinations.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Destinations by Traveler Count')
plt.tight_layout()
plt.show()


scatter_data = df.groupby('Month').agg({'Travelers': 'sum', 'Revenue': 'sum'}).reindex([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Scatter Plot: Travelers vs Revenue
plt.figure(figsize=(8, 6))
plt.scatter(scatter_data['Travelers'], scatter_data['Revenue'], s=100)
for i, month in enumerate(scatter_data.index):
    plt.text(scatter_data['Travelers'][i]+10, scatter_data['Revenue'][i], month)
plt.title('Travelers vs Revenue per Month')
plt.xlabel('Traveler Count')
plt.ylabel('Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()
