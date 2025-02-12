fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# With list comprehension you can do all that with only one line of code:
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = [x2 for x2 in fruits2 if "a" in x2]

print(newlist2)
