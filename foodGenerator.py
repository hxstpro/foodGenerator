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
time.sleep(.500)
print('Welcome to the Restaurant-O-Generator 2000')
time.sleep(.500)
pressEnter = input('Press [ENTER] to continue . . .')
print()
time.sleep(.500)
print('[+] accessing local restaurants . . .')
time.sleep(3)
print('[+] finished. importing database . . .')
time.sleep(.300)
print('[+] starting RNGesus . . .')
time.sleep(.300)
print('[+] daemon started successfully!')
time.sleep(.300)
print('[+] importing "asshole.dict" . . .')
time.sleep(1)
print('[+] "asshole.dict" loaded - success!!!')
time.sleep(.300)
print('[+] scanning "dictionary.index" . . .')
time.sleep(1)
print('[+] "dictionary.index" loaded - success!!!')
time.sleep(.300)
print('[+] program starting  . . .')
print('[+] complete  . . .')
time.sleep(2)

print()

#def user_input(response):
#    if 

response = 0
while response != 'y':
        try:
            del foodPlaces[0]
            print('Do you wanna eat some ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + '? -- Press "Y" or "N": ')
            response = input().lower()
            print()
        except IndexError:
            print('WHOOPS: You\'re all out of options. Try again nerd!!')
            break
        continue
else:       
        print('Enjoy your $' + str(foodCost) + ' of ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + '. See you next Tuesday!!!')            

time.sleep(5)
