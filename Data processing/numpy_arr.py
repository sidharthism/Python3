# NumPy (Numerical Python) is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. 
# Using NumPy, the following operations can be performed:
#  1. Fast mathematical and logical operations on arrays. 
#  2. Fourier transforms and routines for shape manipulation. 
#  3. Operations related to linear algebra. NumPy has in-built functions for linear algebra and random number generation.
# NOTE: NumPy arrays are homogeneous

import numpy as np


# ndarray Object

# The most important object defined in NumPy is an N-dimensional array type called ndarray.
# It describes the collection of items of the same type. Items in the collection can be accessed using a zero-based index.
# Every item in an ndarray takes the same size of block in the memory. 
# Each element in ndarray is an object of data-type object (called dtype).
# Any item extracted from ndarray object (by slicing) is represented by a Python object of one of array scalar types. (int32, int8 etc)

#      --- data-type    ------> |head | array scalar (extracted)
#     |   object(dtype)         | [ ] |
#     |                            ^
#     |                            |
# [ header |  [ ] [ ] [ ] [ ] ... [ ] [ ] ]
#                  ndarray


# CREATING ARRAYS

a = np.array([1, 2, 3, 4, 5, 6, 7]) # numpy.int32
print(a)
b = np.array([(1,2,3),(4,5,6)], dtype = float)
print(b)
c = np.array([(1,2,3),(4,5,6),(7,8,9)], dtype = np.int8)
print(c)

# Some important attributes/parameters of ndarray object
# 1. ndarray.ndim - ndim represents the number of dimensions (axes) of the ndarray. 
# 2. ndarray.shape - shape is a tuple of integers representing the size of the ndarray in each dimension. 
# 3. ndarray.size - size is the total number of elements in the ndarray. It is equal to the product of elements of the shape.
# 4. ndarray.dtype - dtype tells the data type of the elements of a NumPy array. In NumPy array, all the elements have the same data type. 
# 5. ndarray.itemsize - itemsize returns the size (in bytes) of each element of a NumPy array.


print(a.ndim, b.ndim, c.ndim) # 1 2 2
print(a.shape, b.shape, c.shape) # (7,) (2, 3) (3, 3)
print(a.size, b.size, c.size) # 7 6 9
print(a.dtype, b.dtype, c.dtype) # int32 float64 int8
print(a.itemsize, b.itemsize, c.itemsize) # 4 8 1

# Specifying minimum dimensions - ndmin
k = np.array([1,2,3,4,5,6], ndmin = 2) 
print(k) # [[1 2 3 4 5 6]]

# Scalar data types offered by numpy (normal datatypes can also be used while creating array)
# 1. bool_ - Boolean (True or False) stored as a byte
# 2. int_ - Default integer type (same as C long; normally either int64 or int32)
# 3. intc - Identical to C int (normally int32 or int64)
# 4. intp - Integer used for indexing (same as C ssize_t; normally either int32 or int64)
# 5. int8 - Byte (-128 to 127)
# 6. int16 - Integer (-32768 to 32767)
# 7. int32 - Integer (-2147483648 to 2147483647)
# 8. int64 - Integer (-9223372036854775808 to 9223372036854775807)
# 9. uint8 - Unsigned integer (0 to 255)
# 10. uint16 -Unsigned integer (0 to 65535)
# 11. uint32 - Unsigned integer (0 to 4294967295)
# 12. uint64 - Unsigned integer (0 to 18446744073709551615)
# 13. float_ - Shorthand for float64
# 14. float16 - Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
# 15. float32 - Single precision float: sign bit, 8 bits exponent, 23 bits mantiss
# 16. float64 - Double precision float: sign bit, 11 bits exponent, 52 bits mantissa


# DIFFERENT WAYS OF CREATING A NUMPY ARRAY

# There are 8 ways for creating arrays using NumPy Package

# 1. using array()
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)

# 2. using arange([start], stop,[step], [dtype]) -> 0 to stop - 1 
arr = np.arange(10)
print(arr)
arr = np.arange(1, 10)
print(arr)
arr = np.arange(0, 10, 2)
print(arr)

# 3. using linspace(start_index, end_index, no_of_elements, [dtype]) To generate evenly spaced no_of_elements in between start and end indices
arr = np.linspace(0, 9, 10) # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
print(arr)

# 4. using logspace(tart_index, end_index, no_of_elements, [dtype]) To generate no_of_elements elements, evenly spaced w.r.t interval on log scale in between start and end indices
arr = np.logspace(0, 9, 10) # [1.e+00 1.e+01 1.e+02 1.e+03 1.e+04 1.e+05 1.e+06 1.e+07 1.e+08 1.e+09]
print(arr)

# 5. using zeros(shape, [dtype=float], [order='C']) - To generate a new array with zeros. (Order is an essential row style ['C' - Column major, 'F' - Fortran style/row major] for numpy.zeroes() in Python)
arr = np.zeros(7) # [0. 0. 0. 0. 0. 0. 0.]
print(arr)
arr = np.zeros(shape=(1, 2), dtype=int) # [[0 0]]
print(arr)

# 6. using ones(shape, [dtype=float], [order='C']) - To generate a new array with ones. (Order is an essential row style ['C' - Column major, 'F' - Fortran style/row major] for numpy.zeroes() in Python)
arr = np.ones(7) # [1. 1. 1. 1. 1. 1. 1.]
print(arr)
arr = np.ones(shape=(1, 2), dtype=int) # [[1 1]]
print(arr)

# 7. using empty(shape, [dtype=float], [order='C']) - The empty() function is used to create a new array of given shape and type, without initializing entries (garbage values remain).
arr = np.empty(2) # [ 1.83967247e-283 -1.25029680e-272]
print(arr)
arr = np.empty(shape=(1, 2), dtype=int) # [[  806772865 -2021978597]]
print(arr)

# 8. using eye(N, M=None, k=0, dtype=float, order='C') - The eye() function is used to create a 2-D array with ones on the diagonal and zeros elsewhere.
# It returns an array where all elements are equal to zero, except for the k-th diagonal, whose values are equal to one.
# N - No. of rows
# M - No. of columns - defaults to N
# k - Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.
arr = np.eye(3) # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]
print(arr) 
arr = np.eye(3, k = -1)
print(arr) 
arr = np.eye(3, k = 1)
print(arr) 

# ARITHMETIC OPERATIONS WITH NUMPY ARRAY
# With scalars
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a + 1 # [2 3 4 5 6 7 8]
c = 2 ** a # [  2   4   8  16  32  64 128]
d = 7 * a # [ 7 14 21 28 35 42 49]
print(a)
print(b)
print(c)
print(d)

# With numpy ndarrays - Note that both the arrays must be of the SAME SHAPE
p = a + b # Or np.add(a, b)
q = a * b # Or np.multiply(a, b)
r = c - d # Or np.subtract(c, d)
m = b / a # Or np.divide(b, a)
print(p)
print(q)
print(r)
print(m)

k = np.array([1, 2, 3])
l = np.array([1, 2])
# print(k * l) # ValueError: operands could not be broadcast together with shapes (3,) (2,)
k = np.array([1, 2, 3]) # (1, 3)
l = np.array([[1], [2], [3]]) # (3, 3)
print(k * l) # [[1 2 3] [2 4 6] [3 6 9]] (3, 3) - Does normal matrix multiplication



a = np.array([1, 2, 3, 4, 5, 6, 7], dtype=np.float_)
b = a + 1 # [2 3 4 5 6 7 8]

# Reminder and mod
x = np.remainder(b, a)
print(x)
x = np.mod(b, a)
print(x)

# Power
y = np.power(a, b)
print(y)

# Reciprocal
z = np.reciprocal(b, a)
print(z)


# VECTOR OPERATIONS
# Dot product or Inner product or Scalar product
r = np.dot(a, b) # Or np.inner(a, b)
print(r) # 7.0


# MATRIX OPERATIONS
a = np.matrix([[2, 2, 1],
               [1, 3, 1],
               [1, 2, 2]]) # Can also use np.array
# Transpose
print(np.transpose(a))
# Trace
print("\nTrace:", a.trace())
print("Trace:", sum(a.diagonal()))
# Flatten - Modifies the original array/matrix
b = a.copy()
print(b.flatten())

# Linear algebra operations
# Rank
print(np.linalg.matrix_rank(a))
# Determinant after rounding off using np.round
print(np.round(np.linalg.det(a)))
# True inverse - The true inverse of a square matrix can be found using the inv() function of the numpy linalg package. If the determinant of a square matrix is not 0, it has a true inverse.
# If you try to compute the true inverse of a singular matrix (a square matrix whose determinant is 0), you will get an error.
print(np.linalg.inv(a))
# Eigen values
print(np.linalg.eig(a))


# RANDOM NUMBERS
# numpy.random.rand - Random values in a given shape.
a = np.random.rand(10) # 0 to 1
print(a * 10) # Scaled to 10
# numpy.random.randn - Return a sample (or samples) from the “standard normal” distribution -1 to 1
a = np.random.randn(10)
print(a)
# numpy.random.randint - randint(low[, high, size, dtype])	Return random integers from low (inclusive) to high (exclusive)
a = np.random.randint(10)
print(a)

# TRIGONOMETRIC FUNCTIONS
# By default angle is in radians
print(np.sin(90))
print(np.cos(90))
print(np.tan(90))
# In degrees
print(np.sin(90 * (np.pi/180)))

# COMPARISON
# Use the == operator to compare two NumPy arrays to generate a new array object. 
# Call ndarray.all() with the new array object as ndarray to return True if the two NumPy arrays are equivalent.
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([1, 2, 3, 4, 5, 6, 7])
c = a == b
print(c) # [ True  True  True  True  True  True  True]
print(c.all()) # True

# We can also use greater than, less than and equal to operators to compare. 
d = a + 1
e = a - 1
print(np.greater(a, d).all()) # False
print(np.greater_equal(d, a).all()) # True
print(np.less(a, e).all()) # False
print(np.less_equal(e, a).all()) # True

# For more, visit https://numpy.org/doc/stable/
