import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
mtcars = pd.read_csv('mtcars.csv')

# Extract the relevant columns
wt = mtcars['wt']
mpg = mtcars['mpg']

# Create the scatter plot
plt.scatter(wt,mpg)
plt.xlabel('Weight (wt)')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Mpg vs. Weight')

# Draw a regression line through the data
coefficients = np.polyfit(wt,mpg,1)
slope = coefficients[0]
intercept = coefficients[1]

# Add the regression line
plt.plot(wt,slope * wt + intercept, color='red')

# Display the plot
plt.show()
