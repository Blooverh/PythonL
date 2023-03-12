import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Errors that happened:
""" Forgot encoding when reading the json file
file to be written needs forward slash "/" in order to dump info from one json
file to another json file."""

#Explore the struct of the data
filename='Data\eq_1_day_m1.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data=json.load(f)

#gets all earth quakes registered in json file 
all_earthq_dicts= all_eq_data['features']
print(f"EarthQuakes recorded in this file: {len(all_earthq_dicts)}")

#records all magnitudes of all the earthquakes on the file 
# extracting the location data 
longitudes=[]
latitudes=[]
magnitudes=[]
for eq_dict in all_earthq_dicts:
    mag= eq_dict['properties']['mag'] #magnitudes is value inside the features dictionary that contains the property dictionary where magnitudes value is inside properties dictionaty
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    magnitudes.append(mag)
    longitudes.append(lon)
    latitudes.append(lat)

print(magnitudes[:10])
print(longitudes[:10])
print(latitudes[:10])

readable_file='Data/readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data, f , indent=4)

#map the earthquakes
#quick way to specify chart data
#data =[Scattergeo(lon=longitudes, lat=latitudes)]
#specified way to specify chart data and customizing marker size
data=[{
    'type':'scattergeo',
    'lon':longitudes,
    'lat':latitudes,
    'marker':{'size':[5*mag for mag in magnitudes],},
}]
my_layout=Layout(title='Global earthquakes of past year')
fig={'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_eqs.html')
