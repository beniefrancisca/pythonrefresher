nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

name_friend = input("Enter your friends name: ")
# Add the name to the empty set

user_friends.add(name_friend)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.

print(user_friends.intersection(nearby_people))