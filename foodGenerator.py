import random, os, time

foodPlaces = []
with open('foodPlaces.txt') as filehandle:
    foodPlaces = [current_place.rstrip() for current_place in filehandle.readlines()]

insult= []
with open('insults.txt') as filehandle:
    insult = [current_place.rstrip() for current_place in filehandle.readlines()]

foodCost = round(random.uniform(10, 69))
random.shuffle(foodPlaces)

print('Hungry for lunch but you\'re also a little bitch and can\'t decide where to eat? Let me help!')
response = input('Press [ENTER] to continue. . .')
print()
while response != 'y':
        try:
            del foodPlaces[0]
            print('Do you wanna eat some ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + '? -- Press "Y" or "N": ')
            response = input().lower()
            print()
        except IndexError:
            print('WHOOPS: You\'re all out of options. Try again loser!!')
            break
        continue
else:       
        print('Enjoy your $' + str(foodCost) + ' of ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + '. See you next Tuesday!!!')            

time.sleep(5)
