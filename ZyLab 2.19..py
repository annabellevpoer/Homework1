
#Annabelle Poer PSID:1798854

lemon_juice = int(input('Enter amount of lemon juice (in cups):\n'))
water_cups = int(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
ingredient_servings = int(input('How many servings does this make?\n'))

print()
print('Lemonade ingredients - yields', '{:.2f}'.format(ingredient_servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water_cups), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')
desired_servings = int(input('How many servings would you like to make?\n'))

print()

print('Lemonade ingredients - yields', '{:.2f}'.format(desired_servings), 'servings')
divider = float(desired_servings/ingredient_servings)
print('{:.2f}'.format(lemon_juice*divider), 'cup(s) lemon juice')
print('{:.2f}'.format(water_cups*divider), 'cup(s) water')
print('{:.2f}'.format(agave_nectar*divider), 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', '{:.2f}'.format(desired_servings), 'servings')
print('{:.2f}'.format(lemon_juice*divider/16), 'gallon(s) lemon juice')
print('{:.2f}'.format(water_cups*divider/16), 'gallon(s) water')
print('{:.2f}'.format(agave_nectar*divider/16), 'gallon(s) agave nectar')