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