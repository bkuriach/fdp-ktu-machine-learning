

""" 
This program first creates a tuple of fruits. It then accesses an item in the tuple using its index. It also loops through the items in the tuple and checks if an item exists in the tuple. 
Finally, it prints the number of items in the tuple using the len() function. Note that tuples are immutable, so you can't change their items.
"""

# A tuple is a collection of items that are ordered and unchangeable.
fruits = ("apple", "banana", "cherry")

# You can access items in a tuple by referring to their index number.
print(fruits[0])  # Output: apple

# Trying to change the value of a specific item in a tuple raises an error because tuples are immutable.
# fruits[1] = "blueberry"  # This would raise a TypeError.

# You can loop through the items in a tuple.
for fruit in fruits:
    print(fruit)

# You can check if an item exists in a tuple.
if "banana" in fruits:
    print("Banana is in the tuple")

# You can determine how many items a tuple has with the len() function.
print(len(fruits))  # Output: 3


# Create a list of tuples.
fruits = [("apple", 1), ("banana", 2), ("cherry", 3)]

print(fruits)  # Output: [('apple', 1), ('banana', 2), ('cherry', 3)]