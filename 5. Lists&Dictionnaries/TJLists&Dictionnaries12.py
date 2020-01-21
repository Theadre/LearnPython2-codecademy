zoo_animals = {'Unicorn': 'Cotton Candy House',
               'Sloth': 'Rainforest Exhibit',
               'Bengal Tiger': 'Jungle House',
               'Atlantic Puffin': 'Arctic Exhibit',
               'Rockhopper Penguin': 'Arctic Exhibit'}
del zoo_animals['Unicorn']
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"] = "anything"
print(zoo_animals)
