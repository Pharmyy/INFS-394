#Ryan Hensley 3/19/24

import pandas as pd

#load data

df = pd.read_csv('data.csv')

#Print the Column Names
print("Original columns in the DataFrame:")
print(df.columns)


# Reduce the DataFrame to five specific columns
df_reduced = df[['Name', 'Age', 'Salary', 'Department', 'Status']]

# Print the number of rows in the DataFrame
print("Number of rows in the original DataFrame:", df_reduced.count())

# Remove rows if employees are part-time by quering for data not equal to part time 
df_reduced = df_reduced.query('Status != "Part-Time"')

# Print the number of rows in the DataFrame after removing rows
print("Number of rows after removing rows with value 0 in column1:", df_reduced.count())

# Create a new column and set its value to 0
df_reduced['age_gt_27'] = 0


# Assign the value of 1 to the new column based on values in a numeric column
df_reduced.loc[df_reduced['Age'] <= 27, 'age_gt_27'] = 1


# Create dummy variables for a categorical column
df_reduced = pd.get_dummies(df_reduced, columns=['Status'])

# Print the first 7 rows in the DataFrame
print(df_reduced.head(7))

# Print the last 4 rows in the DataFrame
print(df_reduced.tail(4))

# Save the DataFrame to a new CSV file without the index
df_reduced.to_csv('new_data.csv', index=False)


