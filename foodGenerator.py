import random, os, time

foodPlaces = []
with open('foodPlaces.txt') as filehandle:
    foodPlaces = [current_place.rstrip() for current_place in filehandle.readlines()]

insult= []
with open('insults.txt') as filehandle:
    insult = [current_place.rstrip() for current_place in filehandle.readlines()]

foodCost = round(random.uniform(10, 69))
random.shuffle(foodPlaces)
YesSet = {'y', 'yeah', 'yes', 'heck yeah', 'yep'}
NoSet = {'n', 'no', 'nope', 'nah'}
AllSet = YesSet.copy()
AllSet.update(NoSet)

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
time.sleep(1)
print()

response = 0
while response not in YesSet:
        try:
            print('Do you wanna eat some ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + '?')
            response = input().lower()
            print()
            while response not in AllSet:
                print('HEY DICKHEAD! I SAID DO YOU WANT TO EAT ' + str(foodPlaces[0]).upper() + ' OR NOT?!')
                response = input().lower()
                continue
            if response in YesSet:
                continue
            print()
            del foodPlaces[0]
        except IndexError:
            print('WHOOPS: You\'re all out of options. Try again nerd!!')
            break
        continue
else:       
        print('Enjoy your $' + str(foodCost) + ' of ' + str(foodPlaces[0]) + ', ' + random.choice(insult) + '. See you next Tuesday!!!')            

time.sleep(5)
