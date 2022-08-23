import os

lines = ["hi\n", "this is another line of text\n", "one more line of text\n"]
# Opening and writing to a file
try:
    # Create a file and write to it
    f = open("text.txt", "w")
    # Write a stream of data to the file. Note that we have to explicitly add the new line charater.
    f.write("Hello world\n")
    f.writelines(lines)
except Exception as e:
    print(e)
finally:
    f.close()

# file object attributes

with open("text.txt","a") as f:
    print(f.name)
    print(f.closed)
    print(f.mode)

# Reading a file - specific number of bytes
try:
    f = open("text.txt", "r")
    l = f.read(10)
    print(l)
except Exception as e:
    print(e)
finally:
    f.close()

# Reading a file - another way
try:
    f = open("text.txt", "r")
    for each in f:
        print(each)
except Exception as e:
    print(e)
finally:
    f.close()

# Using with - automatically closes resources and free up memory
with open("text.txt", "r") as f:
    for line in f.readlines():
        print(line)

# Writing to and reading from a binary file
with open("binary.bin", "wb+") as f:
    num = [10, 20, 30, 40, 50, 60, 70]
    arr = bytearray(num)
    f.write(arr)
    
with open("binary.bin", "rb") as f:
    # num = list(f.read())
    for i in f.read():
        print(i)

# File pointers
with open("text.txt", "r") as f:
    s = f.readline()
    print(s)
    # file.seek(offset, from where[0: beginning, 1: current, 2: end])
    print("Current position", f.tell())
    f.seek(7, 0)
    s = f.readline()
    print(s)

# truncate a file - truncate to atmost specified size - mode should be a/a+ or w/w+
with open("text.txt", "a+") as f:
    f.truncate(45)
    f.seek(0, 0)
    for l in f.readlines():
        print(l)

# Rename a file
try:
    os.rename("binary.bin", "binary_file.bin")
except Exception as e:
    print(e)

# Delete a file
try:
    os.remove("binary_file.bin")
except Exception as e:
    print(e)
