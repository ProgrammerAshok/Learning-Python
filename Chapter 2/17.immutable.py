# strings are immutable

string = "string"
print(string[1])

# i wanna change string
# string[1] = "T" # you can't change 
# print(string)

# you want to replce string you can do this but ....
print(string.replace("t", "T")) # replace method not changing orginal string creating new string 
print(string)
