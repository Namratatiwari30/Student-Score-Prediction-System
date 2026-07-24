import pandas as pd

df = pd.read_csv("student_scores.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nDataset Statistics:")
print(df.describe())