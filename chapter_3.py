# 3-1:
# store the names of a few of your 
# friends in a list called names.
# print each person's name by 
# accessing each element in the list
# one at a time.

friends = [
        'jon', 'max', 
        'ross', 'greg', 
        'tomas'
        ]

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print('\n\n')

# 3-2:
# using the friends list, print
# a message to each friend. the 
# message should be the same for 
# each friend.

message = " you're great!"

print(friends[0] + message)
print(friends[1] + message)
print(friends[2] + message)
print(friends[3] + message)
print(friends[4] + message)

print('\n\n\n')
# 3-3:
# think of your favorite mode of 
# transportation, like a motorcycle
# or car. make a list with several 
# examples. use your list to print them

motorcycles = [
            'ducati', 'honda cbr600', 
            'honda magna'
            ]


# (fast forwarding a few chapters)

for motorcycle in motorcycles:
    print(f"I would like to ride a "
        f"{motorcycle.title()} someday.")
print('\n\n\n')

# 3-4:
# if you could invite anyone, living or
# deceased to dinner, who would you invite?
# make a list that includes at least 3 people
# you'd like to invite to dinner. print a 
# message to each person, letting them know they're
# invited.

guests = [
        'albert einstein', 'pablo picasso', 
        'ernest hemingway', 'vivian maier',
        'susan sontag', 'david foster wallace'
        ]

for guest in guests:
    print(f"{guest}, you are formally invited "
        "to dinner tonight!!")

print('\n\n\n')
# 3-5:
# you hear that one of your guests can't make it, 
# so you need to send out new invitations.
# remove a guest from the list, add someone new.
# send out new invitations.

uninvited = guests.pop(2)

print(f"Sorry, {uninvited} is still too "
    "hungover from partying last night. "
    "he won't be able to make it tonight.")

guests.append('ursula k. leguin')

for guest in guests:
    print(f"{guest}, sorry for the change in plans, "
        f"but {uninvited} couldn't make it tonight."
        " however, dinner is still on and you are all "
        "officially invited!!")
print('\n\n\n')

# 3-6:
# you just found a bigger table! let the guests know 
# that you'll be inviting more people.
# insert() a guest to the beginning of the list.
# insert() a guest to the middle of the list.
# append() a guest.
# print a new set of invitations.

print("Guys! we found a bigger table! "
    "as if you all aren't enough, I'll invite more people!")

guests.insert(0, 'etta james')
guests.insert(3, 'haruki murakami')
guests.append('nina simone')

for guest in guests:
    print(f"{guest}, you're invited!!")

print('\n\n\n')
# 3-7:
# you just found out that your new table won't
# arrive in time, and you'll only have space 
# for 2 guests. print a message that you can 
# only invite 2 people. then use pop() to remove
# guests until there are only 2 left, letting each
# uninvited guest know. 
# print a message to the two remaining people.
# then use del to remove the last two names and
# print the empty list.

print("Sorry, my big table won't arrive in time. "
    "I can only have 2 people over tonight!")

for guest in guests[:-2]:
    not_coming = guests.pop()
    print(f"Sorry {not_coming}, I can't "
        "have you over for dinner tonight.")

for guest in guests:
    print(f"Hey {guest}, you're still invited")

del guests[:]

print(guests)


print('\n\n\n')


# 3-8:
# think of at least 5 places you'd like to visit.
# store the locations in a list
# print the list in original order
# use sorted() to print the list
# print the original order again
# use reverse() and print the list
# revers() back to orignal order
# use sort() to order the list alphabetically
# use sort() to order the list backwards alphabetically

places = [
        'prague', 'rio de janiero',
        'hawaii', 'tokyo', 'qatar'
        ]

print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)


print('\n\n\n')


# 3-9:
# using your guest list from 3-4,
# use len() to print how many guests
# you're inviting.

guests = [
        'albert einstein', 'pablo picasso', 
        'ernest hemingway', 'vivian maier',
        'susan sontag', 'david foster wallace'
        ]

print(f"I am inviting {len(guests)} guests tonight.")

print('\n\n\n')


# 3-10:
# think of something you could store in a list.
# for example a list of mountains, rivers, cities,
# etc. write a list that creates a list containing
# these items and then uses each function/method introduced
# introduced in this chapter at least once.

ny_streets = [
            'bleeker', 'canal',
            'broadway', 'myrtle',
            'houston', 'delancey'
            ]

ny_streets.reverse()
alphabetical_streets = sorted(ny_streets)
ny_streets.sort(reverse=True)
print(f"I have listed {len(ny_streets)} streets")
in_brooklyn = 'myrtle'
ny_streets.remove(in_brooklyn)
ny_streets.append('park')
ny_streets.insert(0, 'wall')

for street in ny_streets:
    x = ny_streets.pop()
    print(f"{x} is a street/avenue in manhattan.")

del alphabetical_streets[:]

print('\n\n\n')


# end of chapter
