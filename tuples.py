# similar to a list but different usually with brackets around them but not all the time
# putting tuples inside a list using a brackets and parenthesis

short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")
tuple_in_list = [("Rolf", "Bob")]

# sometimes they will be defined with brackets around them
# can't use .append on a tuple
# to add to a tuple you would have to do this
friends = ("Rolf", "Bob", "Anne")
friends = friends + ("Jen",)
print(friends)
# it creates a new tuple with four elements
#tuples useful when you want to keep things unchanged