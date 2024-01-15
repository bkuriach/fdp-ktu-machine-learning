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

# A dictionary is a collection of key-value pairs.
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "CompSci"]
}

# You can access the items of a dictionary by referring to its key name.
print(student["name"])  # Output: John

# You can change the value of a specific item by referring to its key name.
student["age"] = 21
print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Math', 'CompSci']}

# You can add items to the dictionary by using a new index key and assigning a value to it.
student["grade"] = "A"
print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Math', 'CompSci'], 'grade': 'A'}

# You can remove items from the dictionary with the del keyword.
del student["age"]
print(student)  # Output: {'name': 'John', 'courses': ['Math', 'CompSci'], 'grade': 'A'}

# You can determine how many items a dictionary has with the len() function.
print(len(student))  # Output: 3