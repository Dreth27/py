import pandas as pd

# Creating a Data Series
data_series = pd.Series([10, 20, 30, 40, 50], name="Numbers")
print("Data Series:")
print(data_series)
print()

# Creating a Data Frame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']
}

data_frame = pd.DataFrame(data)
print("Data Frame:")
print(data_frame)
print()

# Accessing specific columns in a Data Frame
ages = data_frame['Age']
print("Ages:")
print(ages)
print()

# Adding a new column to the Data Frame
data_frame['Salary'] = [60000, 70000, 80000, 90000, 100000]
print("Data Frame with Salary:")
print(data_frame)
print()

# Filtering Data Frame rows
filtered_data = data_frame[data_frame['Age'] < 40]
print("Filtered Data Frame (Age < 40):")
print(filtered_data)
