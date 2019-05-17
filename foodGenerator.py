#! python3

import random

foodPlaces = []
with open('foodPlaces.txt') as filehandle:
        foodPlaces = [current_place.rstrip() for current_place in filehandle.readlines()]
insultA= []
with open('insults.txt') as filehandle:
        insultA = [current_place.rstrip() for current_place in filehandle.readlines()]
        
foodCost = round(random.uniform(10, 69))

response = 'n'
while response == 'n':
        ranPlace = random.choice(foodPlaces)
        ranInsultA = random.choice(insultA)
#        ranInsultB = random.choice(insultB)
        print('Do you wanna eat ' + str(ranPlace) + ', ' +ranInsultA + "?")
        response = input().lower()
        print()
print('Enjoy your $' + str(foodCost) + ' of ' + ranPlace + ', ' + ". See you tomorrow!")
