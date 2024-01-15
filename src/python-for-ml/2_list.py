""" 
Python provides several built-in data structures that are used to store collections of data. The most commonly used ones are:

Lists: Lists are ordered, mutable collections of data. They are great for keeping related items together.

Tuples: Tuples are similar to lists, but they are immutable, meaning their values can't be changed after they are created. They are useful when you have a collection of items that should not be changed.

Dictionaries: Dictionaries store data in key-value pairs. They are great for fast lookups and are widely used where items are named or identified.

Sets: Sets are unordered collections of unique elements. They are useful when you want to keep track of a collection of elements, but don't care about their order, keys or values and want to prevent duplicates.

Strings: Strings are sequences of characters and are widely used for text manipulation and storage.

Arrays: Arrays are used to store multiple values in one single variable. They are especially useful when you have a large amount of data of the same type.

Queues and Stacks: These are advanced data structures that follow specific rules for adding and removing elements (FIFO for queues and LIFO for stacks). They are useful in certain algorithms and problem-solving scenarios.

Heap: A heap is a special tree-based data structure that satisfies the heap property. It's particularly useful in algorithms involving sorting and priority queues.

Linked Lists: Linked lists are linear collections of data elements, whose order is not given by their physical placement in memory. They are used in many list, queue, and stack implementations.

Trees and Graphs: These are non-linear data structures that are useful for storing data that has inherent hierarchical or networked relationships.
"""



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