import json

#Explore the struct of the data
filename='Data\eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)

readable_file='Data\readable_eq_data.json'
with open(filename,'w') as f:
    json.dump(all_eq_data, f , indent=4)