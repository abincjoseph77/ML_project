import pandas as pd
from sklearn.model_selection import train_test_split




#file reading
df=pd.read_csv(r"E:\abin\ABIN\Upscode\pandas\calicut_data.csv")
print(df.head())
print(df.info())


#price per cent
df["price_per_cent"] = df["price_lakhs"] / df["land_area_cents"]
print(df.head())



#converting categorical data to numerical data
print(df.columns)
numeric_featchers = [ 'land_area_cents',  'distance_to_school_km',
       'distance_to_airport_km', 'distance_to_railway_station_km',
       'distance_to_hospital_km', 'distance_to_medical_college_km',
       'distance_to_bus_stop_km',]


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



#removing some fiels becuse of un usecase 
print(x.head())


#spliting 80 and 20 % 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# chose model 
from sklearn.ensemble import RandomForestRegressor

# create model
model = RandomForestRegressor(n_estimators=100,random_state=42)

# tarin model
model.fit(x_train,y_train)


# evaluation
y_pred = model.predict(x_test)
df_comparison = pd.DataFrame({"Actual:":y_test,"predicted":y_pred})
print(df_comparison.head())


freachers_list = model.feature_names_in_.tolist()
print(freachers_list)



new_land_property = {
  'land_area_cents': [5.5],
  'distance_to_school_km': [1.8], 
  'distance_to_airport_km': [27.0],
  'distance_to_railway_station_km': [10.5],
  'distance_to_hospital_km': [3.0],
  'distance_to_medical_college_km': [5.5],
  'distance_to_bus_stop_km': [0.7], 
  'location_name_Balussery': [0],
  'location_name_Beypore': [0],
  'location_name_Chathamangalam': [0],
  'location_name_Chemancheri': [0],
  'location_name_Cheruvannur': [0],
  'location_name_Chorode': [0],
  'location_name_Eranhikkal': [0],
  'location_name_Iringal': [0],
  'location_name_Kakkancheri': [0],
  'location_name_Kakkodi': [0],
  'location_name_Kakkur': [0],
  'location_name_Kattippara': [0],
  'location_name_Keezhariyur': [0],
  'location_name_Kizhakkoth': [0],
  'location_name_Koduvally': [0],
  'location_name_Kottappally': [0],
  'location_name_Koyilandy': [0],
  'location_name_Kozhikode Beach': [0],
  'location_name_Kozhikode City': [0],
  'location_name_Kozhikode Port': [0],
  'location_name_Kunnamangalam': [1],
  'location_name_Kuruvangad': [0],
  'location_name_Kuruvattur': [0],
  'location_name_Kuttiyadi': [0],
  'location_name_Kuttiyadi Village': [0],
  'location_name_Kuzhimanna': [0],
  'location_name_Kuzhithol': [0],
  'location_name_Mavoor': [0], 
  'location_name_Mokeri': [0],
  'location_name_Mukkom': [0],
  'location_name_Muttil': [0],
  'location_name_Nadapuram': [0],
  'location_name_Nanminda': [0],
  'location_name_Narikkuni': [0], 
  'location_name_Panangad': [0],
  'location_name_Pantalayini': [0],
  'location_name_Payyoli': [0],
  'location_name_Perambra': [0],
  'location_name_Peruvayal': [0],
  'location_name_Puthuppadi': [0],
  'location_name_Puthur': [0],
  'location_name_Thamarassery': [0], 
  'location_name_Thikkodi': [0],
  'location_name_Thiruvallur': [0],
  'location_name_Thiruvangoor': [0],
  'location_name_Ulliyeri': [0],
  'location_name_Vadakara': [0],
  'location_name_Valayam': [0], 
  'location_name_Vellimadukunnu': [0],
  'taluk_Kozhikode': [1], 
  'taluk_Vadakara': [0], 
  'village_Balussery': [0],
  'village_Beypore': [0],
  'village_Calicut': [0],
  'village_Chathamangalam': [0],
  'village_Chemancheri': [0],
  'village_Cheruvannur': [0],
  'village_Chorode': [0],
  'village_Eranhikkal': [0], 
  'village_Iringal': [0], 
  'village_Kakkancheri': [0], 
  'village_Kakkodi': [0],
  'village_Kakkur': [0],
  'village_Kattippara': [0],
  'village_Keezhariyur': [0],
  'village_Kizhakkoth': [0],
  'village_Koduvally': [0],
  'village_Kottappally': [0],
  'village_Koyilandy': [0],
  'village_Kunnamangalam': [1],
  'village_Kuruvangad': [0],
  'village_Kuruvattur': [0],
  'village_Kuttiyadi': [0],
  'village_Kuzhimanna': [0],
  'village_Kuzhithol': [0],
  'village_Mavoor': [0],
  'village_Mokeri': [0],
  'village_Mukkom': [0],
  'village_Muttil': [0],
  'village_Nadapuram': [0],
  'village_Nanminda': [0],
  'village_Narikkuni': [0],
  'village_Panangad': [0],
  'village_Pantalayini': [0],
  'village_Payyoli': [0], 
  'village_Perambra': [0],
  'village_Peruvayal': [0],
  'village_Puthuppadi': [0],
  'village_Puthur': [0], 
  'village_Thamarassery': [0], 
  'village_Thikkodi': [0],
  'village_Thiruvallur': [0],
  'village_Thiruvangoor': [0],
  'village_Ulliyeri': [0],
  'village_Vadakara': [0],
  'village_Valayam': [0],
  'village_Vellimadukunnu': [0],
  'land_type_commercial': [0],
  'land_type_residential': [1] 
}


new_land_df = pd.DataFrame(new_land_property)
new_land_predicted_value = model.predict(new_land_df )
print(new_land_predicted_value)