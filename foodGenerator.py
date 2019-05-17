#! python3

import random
foodPlaces = ['Bdubs', 'Chiptole', 'Penn Station', 'Skyline', 'Da PuNcAkEs', 'Popeyes', 'Arbys', 'Five Guys',
              'Mikes Nashville', 'Hardees', 'Jimmy Johns', 'China Cottage', 'Main St. Deli', 'Noodles & Co', 'El Toro']
insultA = ['fattyboi', 'ugly nerd', 'loser', 'jerkface', 'dunce', 'cretin', 'fat cow', 'dorkface', 'wankaa', 'dingbat', 'stupid idiot',
           'pinhead', 'reeeeeee-tard', 'troglodyte', 'butt-sniff', 'turdmunch', 'fart sniffer']
insultB =['you imperialist flunkey', 'you imperialist lackey', 'you half-baked traitor', 'you reckless reactionary',
          'you politically illiterate militarist', 'you shameless beast']
foodCost = round(random.uniform(10, 69))

response = 'n'
while response == 'n':
        ranPlace = random.choice(foodPlaces)
        ranInsultA = random.choice(insultA)
        ranInsultB = random.choice(insultB)
        print('Do you wanna eat ' + str(ranPlace) + ', ' +ranInsultA + "?")
        response = input().lower()
        print()
print('Enjoy your $' + str(foodCost) + ' of ' + ranPlace + ', ' + ranInsultB + ".")
