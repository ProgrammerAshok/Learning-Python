# string slicing
# slicing / selecting sub sequences

language = "python"

# syntax - [start argument : stop argument -1]
print(language[0:2])
print(language[2:6])

# you can do also negative indexing
print("\nnegative slicing")
print(language[-5: -1])

# something new
print(language[:])  # printing complete string
print(language[1:]) # same as language[1 : 6]
print(language[:4]) # same as language[0 : 4]
