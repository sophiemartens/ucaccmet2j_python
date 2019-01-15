import json
with open('precipitation.json') as f:
    precipitation_list = json.load(f)
from collections import Counter
#for all cities in total


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
print(cities)