x = 0
while x <= 5:
    print(x)
    x = x + 1

#numbers = [0, 1, 2, 3, 4]
#for nu in numbers:
#   print(nu)

for num in range(5):
    print(num)
   
counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])

    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for county in counties_dict:
        print(county)
    for countykey in counties_dict.keys():
        print(countykey)