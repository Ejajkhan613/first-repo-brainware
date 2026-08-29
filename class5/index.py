import pandas as pd

# Data Type Conversion
# data = {
#     "name": ["A", "B", "C"],
#     "class": ["X", "X", "X"],
#     "age": ["25", "30", "35"],
#     "salary": ["50000.0", "60000.0", "55000.0"],
#     "date": ["2024-01-01", "2024-02-01", "2024-03-01"]
# }

# df = pd.DataFrame(data)

# dtypes -> used to find the data type
# astype -> used to change the data type
# pd.to_datetime -> used to work with date

# str -> alphanumeric characters
# category -> city, country, gender

# Data Types
# int, float, category, str, datetime


# df["age"] = df["age"].astype(int)

# df["salary"] = df["salary"].astype(float)

# df["class"] = df["class"].astype("category")

# df["date"] = pd.to_datetime(df["date"])


# df["day"] = df["date"].dt.day
# df["month"] = df["date"].dt.month
# df["year"] = df["date"].dt.year

# print(df)








# Find and fix missing or null data
# data = {
#  "name": ["A", "B", "C", "D"],
#  "age": [25, None, None, 35]
# }


# Class Result Analysis
data = {
    "name": ["Aman", "Riya", "John", "Sara", "Ali", "Neha"],
    "math": [85, 92, 78, 88, 95, 70],
    "science": [90, 85, 80, 92, 88, 75],
    "english": [78, 88, 85, 90, 92, 72]
}

df = pd.DataFrame(data)

# Find the Total Marks of each student
df["total"] = df["math"] + df["science"] + df["english"]

# Find the average of each student
df["average"] = df["total"] / 3

# sort the data based on average (desc - asc) sort_value()
df = df.sort_values(by="average", ascending=False)

# filter the topper student based on average -> iloc
topper = df.iloc[:3]

# find the class average
print(df["average"].mean().round(2))


# Find the student with least average (last 3 students)
# least = df.iloc[-3:]
# print(topper)
# print(least)