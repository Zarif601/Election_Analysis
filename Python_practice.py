# Testing if statements
counties = ['Arapahoe', 'Denver', 'Jefferson']

if counties[1] == 'Denver':
    print(counties[1])

# Testing if-else statements
temperature = 90

if temperature > 80:
    print('Turn on the AC.')
else:
    print('Open the windows.')

# Testing nested if-else statements
# What is the score?
score = 90

# Determine the grade.
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

# Testing Membership Operators
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

# Testing loops
for county in counties:
    print(county)

# Testing loops with dictionaries
counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

# Testing loops with dictionaries within lists
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
 {"county":"Denver", "registered_voters": 463353}, 
 {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
     print(f'{county_dict["county"]} county has {county_dict["registered_voters"]:,} registered voters.')