# string
# collection of characters inside single qoutes or double qoutes

first_name = "Ashok"
last_name = " Chopade"

full_name = first_name + last_name
print(full_name)

# print(first_name + 3) throws as error because string + string can add but not string and integer
# print(first_name + "3") you can do this (no error)
print(first_name + str(3)) # also you can do this (no error)

print(first_name * 5) # prints first_name 10 times
