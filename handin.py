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
    year = int(split_date[0])
    rainfall_per_month[month-1] = value + rainfall_per_month[month-1]

print(rainfall_per_month)
rainfall_per_year = sum(rainfall_per_month)
print(rainfall_per_year)
import json
with open("seattle.json", "w") as file:
  json.dump( rainfall_per_month, file, indent =4, sort_keys = True )

#relative rainfall per month compared to year
#lets try first for seattle, I only had time to make fractions out of it
relative_rainfall = []
for i in range(12): 
    print(rainfall_per_month[i]/rainfall_per_year)

print(relative_rainfall)