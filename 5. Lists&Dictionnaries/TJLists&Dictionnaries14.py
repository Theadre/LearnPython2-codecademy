inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
             'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
             'burlap bag': ['apple', 'small ruby', 'three-toed sloth']}
inventory['pouch'].sort()
inventory["pocket"] = ['seashell', 'strange berry', 'lint']
inventory["backpack"].sort()
inventory['backpack'].remove('dagger')
inventory["gold"] += 50

print(inventory)
