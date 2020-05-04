# make several dictionaries, where the name of each dictionary
# is the name of a pet. In each dictionary, include the kind of
# animal and the owner's name. Store these dictionaries in a list
# called pets. Next, loop through your list and as you do print 
# everything you know about each pet.

larry = {
    'owner': 'joe',
    'name': 'larry',
    'animal': 'dog',
    'color': 'brown',
    'food': 'steak',
    }

kev = {
    'owner': 'mary',
    'name': 'kev',
    'animal': 'iguana',
    'color': 'green',
    'food': 'insects',
    }

spot = {
    'owner': 'jeff',
    'name': 'spot',
    'animal': 'dog',
    'color': 'black and white',
    'food': 'chicken',
    }

pets = [larry, kev, spot]

for pet in pets:
    for info in pet.keys():
        if info == 'owner':
            print(f"\nOwner's name: {pet['owner'].title()}")
        if info == 'name':
            print(f"\tPet's name: {pet['name'].title()}")
        if info == 'animal':
            print(f"\tType of pet: {pet['animal'].title()}")
        if info == 'color':
            print(f"\tColor: {pet['color'].title()}")
        if info == 'food':
            print(f"\tFavorite food: {pet['food'].title()}")
