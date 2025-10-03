import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv(r"E:\abin\ABIN\Upscode\pandas\calicut_data.csv")

print(df.head())


df["pice_per_cent"]=df["price_lakhs"]/df["land_area_cents"]


# print(df.head())

# print(df["pice_per_cent"].describe())





# sns.histplot(data=df,x='pice_per_cent')
# plt.title('Distribution of price')
# plt.show()



# sns.scatterplot(data=df,x='distance_to_hospital_km',y='pice_per_cent')
# plt.title('distance_to_hospital_km vs pice_per_cent ')
# plt.show()



# y=mx+c


df_processed = pd.get_dummies(df,columns=["location_name","taluk","village"],drop_first=True)
print("df_processed",df_processed.head())