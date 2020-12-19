voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)
voting_data.insert(1,{"county":"El Paso","registered_voters":461149})

voting_data.pop(0)
voting_data[2]=({"county":"Denver", "registered_voters": 463353})
voting_data[1]=({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# If Else statements
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
    # What is the score?
# score = int(input("What is your test score? "))

# Elif Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# in and not in
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

    #if not(x > y):