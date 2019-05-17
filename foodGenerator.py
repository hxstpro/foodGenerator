#! python3

import random

foodPlaces = []
with open('foodPlaces.txt') as filehandle:
        foodPlaces = [current_place.rstrip() for current_place in filehandle.readlines()]

insult= []
with open('insults.txt') as filehandle:
        insult = [current_place.rstrip() for current_place in filehandle.readlines()]

foodCost = round(random.uniform(10, 69))

response = 'n'

while response == 'n':
        ranPlace = random.choice(foodPlaces)
        ranInsult = random.choice(insult)
        ranInsult2 = random.choice(insult)
        print('Do you wanna eat ' + str(ranPlace) + ', ' +ranInsult + "?")
        response = input().lower()
        print()

print('Enjoy your $' + str(foodCost) + ' of ' + ranPlace + ', ' + ranInsult2 + ". See you tomorrow!")
