#! /usr/bin/env python3

# an ice cream stand is a specific type of restaurant.
# write a child class that inherits from the restaurant class.
# add an attribute called flavors that stores a list of ice cream flavors
# write a method that displays these flavors


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant's name is {self.restaurant_name.title()}.")
        print(f"We serve {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

    def print_number_served(self):
        print(f"The restaurant has served {self.number_served} people!")

class IceCreamStand(Restaurant):
     """a new type of restaurant!"""

    def __init__(self, restaurant_name, cuisine_type):
        """init ice cream store, inherit restaurant"""
        super().__init__(restaurant_name, cuisine_type='ice cream')
        self.flavors = [
            'vanilla', 'chocolate',
            'mint chip', 'bubblegum',
            'pecan', 'pistachio'
        ]


    def list_flavors(self):
    """print flavor list"""
        print(f"We have the following flavors!")
        for flavor in self.flavors:
            print(flavor.title())


new_stand = IceCreamStand("ice cream 2.0")
new_stand.describe_restaurant()
new_stand.list_flavors()
