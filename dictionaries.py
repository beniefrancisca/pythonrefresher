#using curly braces
friend_ages = {"Rolf":24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])
# it will print out the age
# when in print you add brackets to insert the name

# to add to a dictionary
# to update a dictionary of an existing name
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 20

print(friend_ages)

# you cannot add duplicate keys

# how to store multiple information in dictionaries using lists and tuples, makes it easy to trace

friends = (
    {"name": "Rolf Smilth", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)
print(friends[0]["name"])
# by using 0 it highlights looking at the first line of the dictionary and the property of the dictionary

# or you can do
# friend = friends[0]

# using dict to turn data into a dictionary
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
firend_ages = dict(friends)
print(friend_ages)