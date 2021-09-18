
#Annabelle Poer PSID:1798854

import math
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height*wall_width

print('Wall area:', wall_area, 'square feet')
paint_can = 350
Paint_needed ='{:.2f}'.format(wall_area/paint_can)
print('Paint needed:', Paint_needed, 'gallons')
Paint_needed =(wall_area/paint_can)
cans = math.ceil(Paint_needed)
print('Cans needed:', cans, 'can(s)\n')

my_dict = {'red': 35,
           'blue': 25,
           'green': 23}

color = input('Choose a color to paint the wall:\n')
cost = my_dict[color]*cans
cost_str = '$'+str(cost)
print('Cost of purchasing',color, 'paint:',cost_str)