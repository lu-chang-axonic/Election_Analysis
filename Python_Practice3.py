'''
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
for countykey in counties_dict.keys():
   print(countykey)
for countykey in counties_dict.values():
    print(countykey)
for county in counties_dict:
    print(counties_dict[county])


for county in counties_dict.values ():
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print (key,value)
'''    

# Make the dictionary the list
'''
counties_dict = [{"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438},{"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438},{"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}]
for x in counties_dict:
    print (x)

for i in range(len(counties_dict)):
   print (counties_dict[i])

counties_dict = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for x in counties_dict:
    print(x['registered_voters'])
for x in counties_dict:
    for value in x.values():
        print(value)
'''
import csv
dir(csv)
print (dir(csv))