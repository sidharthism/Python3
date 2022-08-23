# Python Array

# An array is a collection of items of the same type stored at contiguous memory locations. 
# Array can be handled in Python by a module named array. They can be useful when we have to manipulate only a specific data type values. 
# If you create arrays using the array module, all elements of the array must be of the same type.


# Creating a Array
# Array in Python can be created by importing array module.
#   from array import array
#   array(typecode [, initializer]) -> array

#   Return a new array whose items are restricted by typecode, and
#   initialized from the optional initializer value, which must be a list,
#   string or iterable over elements of the appropriate type.

#   Arrays represent basic values and behave very much like lists, except
#   the type of objects stored in them is constrained. The type is specified
#   at object creation time by using a type code, which is a single character.
#   The following type codes are defined:

#       Type code   C Type             Minimum size in bytes
#       'b'         signed integer     1
#       'B'         unsigned integer   1
#       'u'         Unicode character  2 (see note)
#       'h'         signed integer     2
#       'H'         unsigned integer   2
#       'i'         signed integer     2
#       'I'         unsigned integer   2
#       'l'         signed integer     4
#       'L'         unsigned integer   4
#       'q'         signed integer     8 (see note)
#       'Q'         unsigned integer   8 (see note)
#       'f'         floating point     4
#       'd'         floating point     8

#   NOTE: The 'u' typecode corresponds to Python's unicode character. On
#   narrow builds this is 2-bytes on wide builds this is 4-bytes.

#   NOTE: The 'q' and 'Q' type codes are only available if the platform
#   C compiler used to build Python supports 'long long', or, on Windows,
#   '__int64'.

#   Methods:

#   append() -- append a new item to the end of the array
#   buffer_info() -- return information giving the current memory info
#   byteswap() -- byteswap all the items of the array
#   count() -- return number of occurrences of an object
#   extend() -- extend array by appending multiple elements from an iterable
#   fromfile() -- read items from a file object
#   fromlist() -- append items from the list
#   frombytes() -- append items from the string
#   index() -- return index of first occurrence of an object
#   insert() -- insert a new item into the array at a provided position
#   pop() -- remove and return item (default last)
#   remove() -- remove first occurrence of an object
#   reverse() -- reverse the order of the items in the array
#   tofile() -- write all items to a file object
#   tolist() -- return the array converted to an ordinary list
#   tobytes() -- return the array converted to a string

#   Attributes:

#   typecode -- the typecode character used to create the array
#   itemsize -- the length in bytes of one array item

import array
# Print all typecodes - bBuhHiIlLqQfd
print(array.typecodes)

arr = array.array('d', [1, 2, 3, 4, 4, 5, 6, 7])
print(arr.typecode, arr)


# Accessing Python Array Elements - using indices

for i in range(len(arr)):
    print(arr[i])


# Slicing Python Arrays

# We can access a range of items in an array by using the slicing operator :
print(arr[1:6]) # 2nd to 6th
print(arr[3:len(arr)])
# Output : array('d', [2.0, 3.0])
print(arr[:-4]) # beginning till (len(arr) - 4) th element
print(arr[5:]) # 6th to end
print(arr[:]) # beginning to end


# Removing Python Array Elements

# We can delete one or more items from an array using Python's del statement.
# Delete 4 at index 4
del arr[4]
print(arr)

# Delete an entire array
new_arr = array.array('i', [7, 8, 9])
print(new_arr)
del new_arr
try:
    print(new_arr) # NameError: name 'new_arr' is not defined
except Exception as e:
    print(e)

# Other methods
print(arr.itemsize)
print(arr.tobytes())
print(arr.buffer_info())