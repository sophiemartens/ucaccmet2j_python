import json
with open('precipitation.json') as f:
    precipitation_list = json.load(f)
from collections import Counter
#for all cities in total, I misinterpreted the prompt so that's why I calculated the total rainfall in all cities


seattle=[]
for measurement in precipitation_list:
    if measurement['station']== "GHCND:US1WAKG0038":
	    seattle.append(measurement['value'])
sum_seattle=sum(seattle)
cincinnati=[]
for measurement in precipitation_list:
    if measurement['station']== "GHCND:USW00093814":
	    cincinnati.append(measurement['value'])
sum_cincinnati = sum(cincinnati)
maui=[]
for measurement in precipitation_list:
    if measurement['station']== "GHCND:USC00513317":
	    maui.append(measurement['value'])
sum_maui = sum(maui)
sandiego=[]
for measurement in precipitation_list:
    if measurement['station']== "GHCND:US1CASD0032":
	    sandiego.append(measurement['value'])
sum_sandiego = sum(sandiego)
cities = [sum_seattle, sum_cincinnati, sum_maui, sum_sandiego]
sum_cities = sum(cities)
print(sum_cities)

rainfall_per_month = [0]*12
for measurement in cities:
    split_date = measurement['date'].split("-")
    value = measurement['value']
    month= int(split_date[1])
    year = int(split_date[0])
    rainfall_per_month[month-1] = value + rainfall_per_month[month-1]