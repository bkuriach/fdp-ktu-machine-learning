import pandas as pd

# Create a DataFrame from a dictionary.
data = {"Name": ["John", "Anna", "Peter"], "Age": [28, 24, 33]}
df = pd.DataFrame(data)

print(df)

# Access a column in the DataFrame.
print(df["Name"])

# Add a new column to the DataFrame.
df["Salary"] = [50000, 60000, 70000]
print(df)

# Access a row in the DataFrame.
print(df.loc[0])

# Apply a function to a column.
df["Age"] = df["Age"].apply(lambda age: age + 1)
print(df)

# Filter the DataFrame.
filtered_df = df[df["Age"] > 30]
print(filtered_df)

""" Group the DataFrame by a column and calculate the mean of the other columns."""

# Create a DataFrame.
df = pd.DataFrame({
    "City": ["New York", "Los Angeles", "New York", "Los Angeles"],
    "Temperature": [80, 75, 85, 78],
    "Humidity": [30, 40, 35, 45]
})

# Group the DataFrame by the 'City' column and calculate the mean of the other columns.
grouped_df = df.groupby("City").mean()

print(grouped_df)

""" Concatenate two dataframes """

# Create two DataFrames.
df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]
})

df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"]
})

# Concatenate the DataFrames.
df = pd.concat([df1, df2])

print(df)

""" 
Merge two DataFrames based on a common column
"""

import pandas as pd

# Create two DataFrames with a common column 'Key'.
df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C', 'D'],
    'Value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'Key': ['B', 'D', 'E', 'F'],
    'Value': [5, 6, 7, 8]
})

# Merge the DataFrames on the 'Key' column.
merged_df = df1.merge(df2, on='Key')

print(merged_df)
# In this code, df1.merge(df2, on='Key') merges the DataFrames df1 and df2 on the 'Key' column. 
# The resulting DataFrame merged_df contains the rows where the 'Key' values are present in both DataFrames. The 'Value' columns are disambiguated by adding suffixes '_x' and '_y' to their names. 
# If you want to keep all rows from df1 and df2, you can use df1.merge(df2, on='Key', how='outer')

""" Inner join """
import pandas as pd

# Create two DataFrames with a common column 'Key'.
df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C', 'D'],
    'Value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'Key': ['B', 'D', 'E', 'F'],
    'Value': [5, 6, 7, 8]
})

# Perform an inner join on the 'Key' column.
inner_joined_df = df1.merge(df2, on='Key', how='inner')

print(inner_joined_df)

""" Join based on multiple columns """
import pandas as pd

# Create two DataFrames with common columns 'Key1' and 'Key2'.
df1 = pd.DataFrame({
    'Key1': ['A', 'B', 'C', 'D'],
    'Key2': ['W', 'X', 'Y', 'Z'],
    'Value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'Key1': ['B', 'D', 'E', 'F'],
    'Key2': ['X', 'Z', 'Y', 'W'],
    'Value': [5, 6, 7, 8]
})

# Join the DataFrames on the 'Key1' and 'Key2' columns.
joined_df = df1.merge(df2, on=['Key1', 'Key2'], how='inner')

print(joined_df)