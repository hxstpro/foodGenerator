import random, os, time

foodPlaces = []
with open('foodPlaces.txt') as filehandle:
    foodPlaces = [current_place.rstrip() for current_place in filehandle.readlines()]

insult= []
with open('insults.txt') as filehandle:
    insult = [current_place.rstrip() for current_place in filehandle.readlines()]

foodCost = round(random.uniform(10, 69))

response = ''
while response != 'y':
    print('Do you wanna eat ' + str(random.choice(foodPlaces)) + ', ' + random.choice(insult) + "?")
    response = input().lower()
print()
print('Enjoy your $' + str(foodCost) + ' of ' + random.choice(foodPlaces) + ', ' + random.choice(insult) + ". See you tomorrow!")

time.sleep(3)
