# using len and sum functions

grades = [80, 75, 90, 100]
total = sum(grades)
length = len(grades)
# sum adds everything together gives a total
# len gives us the length of the collection

average = total / length
print(average)
# sum divided by length

# which of these data structures are less ideal list, tuple or set ?

grades = [80, 75, 90, 100]  # best choice with total flexibility
grades = (80, 75, 90, 100)  # cannot add new things in overtime with tuples only use if you do not need to add things
grades = {80, 75, 90, 100}  # set is the worst choice to use you can  add another number like 100 because of duplicates
