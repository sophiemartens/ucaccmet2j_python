import json
with open('precipitation.json') as f:
    precipitation_list = json.load(f)

seattle=[]
for measurement in precipitation_list:
    if measurement['station']== "GHCND:US1WAKG0038":
	    seattle.append(measurement)

rainfall_per_month = [0]*12
for measurement in seattle:
    split_date = measurement['date'].split("-")
    value = measurement['value']
    month= int(split_date[1])
    rainfall_per_month[month-1] = value + rainfall_per_month[month-1]

print(rainfall_per_month)
 
import json
with open("seattle.json", "w") as file:
  json.dump( rainfall_per_month, file, indent =4, sort_keys = True )
