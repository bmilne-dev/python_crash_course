# Make a dictionary called favorite_places. Think of three names 
# to use as keys in the dictionary, and store one to three favorite 
# places for each person. Loop through the dictionary, and print 
# each person's name and their favorite places.

favorite_places = {
    'sally': [
        'chicago', 'niagra falls',
        'toronto',
        ],
    'james': [
        'jersey city', 'cape may',
        'asbury park',
        ],
    'joey': [
        'los angeles', 'cabo',
        'basel'
        ],
    }

for name in favorite_places:
    print(f"\n{name.title()}'s favorite places are:")
    for place in favorite_places[name]:
        print(place.title())


