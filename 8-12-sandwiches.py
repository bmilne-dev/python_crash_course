# write a function that accepts a list of items a person wants on a sandwich
# the function should have one parameter that collects as many items as the
# function call provides, and it should print a summary of the sandwich that
# is being ordered.

# toppings = []
def request_toppings():
    toppings = []
    print("What toppings would you like?")
    print("(enter 'q' when finished")
    while True:
        topping = input("Topping: ")
        if topping == 'q':
            break
        toppings.append(topping)
    return toppings

def show_toppings(toppings):
    print("You requested the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

topping_list = request_toppings()
show_toppings(topping_list)
