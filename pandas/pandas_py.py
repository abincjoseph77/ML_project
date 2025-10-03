import pandas as pd


df=pd.read_csv(r"E:\abin\ABIN\Upscode\pandas\student_data.csv")

print(df.head())

print(df.describe())

print(df.info())


print(df['score'].describe())