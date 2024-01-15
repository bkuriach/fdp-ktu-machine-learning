# A list is a collection of items that are ordered and changeable.
fruits = ["apple", "banana", "cherry"]

# You can access items in a list by referring to their index number.
print(fruits[0])  # Output: apple

# You can change the value of a specific item by referring to the index number.
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# You can add items to the end of the list with the append() method.
fruits.append("dragonfruit")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'dragonfruit']

# You can remove items from the list with the remove() method.
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'dragonfruit']

# You can determine how many items a list has with the len() function.
print(len(fruits))  # Output: 3

fruits.append("orange")
fruits.append("grapes")
fruits.append("grapes")
print(fruits)  
fruits.pop()
print(fruits)  

#sort the list
fruits.sort()
print(fruits) 

# Sort the list based on the last characters of the strings.
fruits.sort(key=lambda fruit: fruit[-1])
print(fruits)  # Output: ['apple', 'banana', 'cherry']

#sort the list based on lentgh of the strings
fruits.sort(key=lambda fruit: len(fruit))
print(fruits)  # Output: ['apple', 'banana', 'cherry']