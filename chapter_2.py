# store a message in a variable, 
# then print that variable.

# exercise 2-2:
# change the value of your variable
# and print the new message.

message = "simple message"

print(message_1)

message = "new message"

print(message)


# store a person's name in a variable,
# and print a message to that person.
# your message should be simple, like
# "Hello Eric, would you like to learn 
# some Python today?"

name = 'joe'

print(f"Sup {name.title()}, would you like to learn "
    "some python today?")

# exercise 2-4:
# print the person's name in lower case, 
# upper case, and title case. 

print(name.lower())
print(name.upper())
print(name.title())

# exercise 2-5:
# find a quote from a famous person you
# admire. print the quote and the name of
# its author.

print("Stephen Fry once said, "
    "\"The short answer is 'no'. The long answer is 'fuck no'\"")

# exercise 2-6:
# store the quote in a variable, then store
# the message in another variable and print
# a formatted version.

message = "Stephen Fry once said, "
quote =  "\"The short answer is 'no'. The long answer is 'fuck no'\""

print(message + quote)

# exercise 2-7:
# store a name in a variable with a bunch of
# whitespace. print the name with all the
# whitespace, then remove some with lstrip()
# some with rstrip() and then all of it with 
# strip()

spacey_name = '   \t\n sarah langley \n\n\t'

print(spacey_name)
print(spacey_name.lstrip())
print(spacey_name.rstrip())
print(spacey_name.strip())



# write addition, subraction, multiplication
# and division operations that each result 
# in the number 8. enclose them in print 
# statements.

print(5 + 3)
print(8 / 1)
print(4 * 2)
print(10 - 2)


# exercise 2-9:
# store your favorite number in a variable.
# then, using that variable, create a message
# that reveals your favorite number and print it.

favorite_number = 5
message = f"my favorite number is {favorite_number}"

print(message)


