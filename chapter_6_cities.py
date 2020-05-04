# Make a dictionary called cities. Use the names of three
# cities as keys in your dictionary. Create a dictionary
# of information about each city and include the country 
# that the city is in, its approximate population, and one 
# fact about the city. Print the name of each city and all
# the information about it.

cities = {
    'new york': {
        'country': 'united states',
        'population': '8.5 million',
        'fact': 'Taxi\'s were originally red and green',
        },
    'bern': {
        'country': 'switzerland',
        'population': '133,791',
        'fact': 'Bern cathedral spire is the tallest in Switzerland'
        },
    'montreal': {
        'country': 'canada',
        'population': '1.78 million',
        'fact': 'No building can be taller than the cross on Mount Royal',
        },
    }

#for city in cities:
#    print(f"\nHere's some info about {city.title()}:")
#    for info in city:
#        if info == 'country':
#            print(f"{city.title()} is located in {city[info]}")
#        if info == 'population':
#            print(f"The population of {city.title()} is {city[info]}")
#        if info == 'fact':
#            print(f"And an interesting fact about {city.title()} is {city[info]}")

for city, info in cities.items():
    print(f"\nHere's some interesting info about {city.title()}:")
    print(f"{city.title()} is located in {info['country'].title()}.")
    print(f"The population of {city.title()} is {info['population']}")
    print(f"And an interesting fact about {city.title()} is:\n\t\
    {info['fact']}.")

    
