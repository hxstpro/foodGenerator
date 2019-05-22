import random, os, time

foodPlaces = []
with open('foodPlaces.txt') as filehandle:
    foodPlaces = [current_place.rstrip() for current_place in filehandle.readlines()]

insult= []
with open('insults.txt') as filehandle:
    insult = [current_place.rstrip() for current_place in filehandle.readlines()]

foodCost = round(random.uniform(10, 69))
random.shuffle(foodPlaces)

response = ''
while response != 'y':
    del foodPlaces[0]
    print('Do you wanna eat some ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + "?")
    response = input().lower()

print('Enjoy your $' + str(foodCost) + ' of ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + '. See you next Tuesday!!!')
   
time.sleep(5)
