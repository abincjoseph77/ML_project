import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics



#file reading
df=pd.read_csv(r"E:\abin\ABIN\Upscode\pandas\calicut_data.csv")
print(df.head())
print(df.info())


#price per cent
df["price_per_cent"] = df["price_lakhs"] / df["land_area_cents"]
print(df.head())



#converting categorical data to numerical data
print(df.columns)
numeric_featchers = ['property_id',  'latitude',
       'longitude', 'land_area_cents',  'distance_to_school_km',
       'distance_to_airport_km', 'distance_to_railway_station_km',
       'distance_to_hospital_km', 'distance_to_medical_college_km',
       'distance_to_bus_stop_km', 'price_lakhs', 'price_per_cent']


# un=['location_name', 'taluk', 'village','land_type',] converting this text colums to numerics using one-hot encoding
df_processed = pd.get_dummies(df,columns=['location_name', 'taluk', 'village','land_type'],drop_first=True)
print(df_processed.head())


#removing normal colams and add new df_processed column 
dummy_featcher = []
for column_name in df_processed.columns:
    if column_name.startswith('land_type') or column_name.startswith('village') or column_name.startswith('location_name') or column_name.startswith('taluk'):
        dummy_featcher.append(column_name)
        
print(dummy_featcher)


#add all column
freachers = numeric_featchers + dummy_featcher
print(freachers)


#adding feactchers in x and y

x = df_processed[freachers]
y= df_processed['price_per_cent']