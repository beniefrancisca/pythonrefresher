# adding numbers into strings together
# using formatted strings

age = 34
age_as_str = str(age)
print(f"You are {age}")


name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)

name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name="Jose")
print(jose_greeting)