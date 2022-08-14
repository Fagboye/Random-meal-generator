import random 
# I define the base constituents of the meals
Base = ['rice', 'spaghetti', 'noodles', 'Amala']
primary_meal = random.choice(Base)


if primary_meal == 'rice':
    secondary = ['white', 'fried', 'jollof']
    random_secondary = random.choice(secondary)
    print(f'{random_secondary} {primary_meal}')

if primary_meal == 'Amala':
  soup = ['egusi', 'efo']
  r_soup = random.choice(soup)
  print(f'{primary_meal} and {r_soup}')