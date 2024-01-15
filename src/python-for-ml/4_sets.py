# A set is a collection of unique elements.
fruits = {"apple", "banana", "cherry", "apple"}

# Duplicates are automatically removed in a set.
print(fruits)  # Output: {'cherry', 'banana', 'apple'}

# You can add an item to a set using the add() method.
fruits.add("dragonfruit")
print(fruits)  # Output: {'cherry', 'banana', 'apple', 'dragonfruit'}

# You can remove an item from a set using the remove() method.
fruits.remove("apple")
print(fruits)  # Output: {'cherry', 'banana', 'dragonfruit'}

# You can check if an item exists in a set using the in keyword.
print("banana" in fruits)  # Output: True

# You can determine how many items a set has with the len() function.
print(len(fruits))  # Output: 3

# You can perform set operations like union, intersection, difference, and symmetric difference.
other_fruits = {"banana", "dragonfruit", "elderberry"}
print(fruits.union(other_fruits))  # Output: {'cherry', 'banana', 'elderberry', 'dragonfruit'}
print(fruits.intersection(other_fruits))  # Output: {'banana', 'dragonfruit'}
print(fruits.difference(other_fruits))  # Output: {'cherry'}
print(fruits.symmetric_difference(other_fruits))  # Output: {'cherry', 'elderberry'}