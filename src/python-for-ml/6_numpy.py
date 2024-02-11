import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Perform arithmetic operations
print("Addition:", arr + 2)
print("Multiplication:", arr * 2)

# Calculate statistical measures
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", matrix)

# Matrix multiplication
print("Matrix multiplication:\n", np.dot(matrix, matrix))

# Transpose of a matrix
print("Transpose:\n", np.transpose(matrix))

# Inverse of a matrix
try:
    print("Inverse:\n", np.linalg.inv(matrix))
except np.linalg.LinAlgError:
    print("Matrix is not invertible")

# Element-wise multiplication
print("Element-wise multiplication:\n", np.multiply(matrix, matrix))


"""
Convert the list to a NumPy array.
"""
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)  # Output: array([1, 2, 3, 4, 5])


""" 
Sum of a matrix
"""
# Create a 2D array (matrix).
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum the matrix column-wise.
column_sums = np.sum(matrix, axis=0)

print(column_sums)  # Output: array([12, 15, 18])


# Sum the matrix Row-wise.
row_sums = np.sum(matrix, axis=1)
print(row_sums)  # Output: array([ 6, 15, 24])


""" 
Stack columns of a matrix
"""
# Create two 1D arrays.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack the arrays as columns.
c = np.column_stack((a, b))

print(c)  # Output: array([[1, 4], [2, 5], [3, 6]])

""" 
Finf NaN values 
"""
# Create a 1D array with a NaN value.
arr = np.array([1, 2, np.nan, 4, 5])

# Find NaN values in the array.
nan_indices = np.isnan(arr)

print(nan_indices)  # Output: array([False, False,  True, False, False])
# In this code, np.isnan(arr) returns a Boolean array of the same shape as arr, where True indicates a NaN value 
# and False indicates a non-NaN value. You can use this Boolean array to index arr and get the NaN values or replace them. 
# For example, arr[nan_indices] gives the NaN values and arr[nan_indices] = 0 replaces the NaN values with 0.