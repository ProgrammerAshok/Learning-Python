# string formatting
name = "Ashok"
age = 15

print("hello " + name + " your age is " + str(age)) # ugly syntax

# string formatting
print("Hello {} your age is {}".format(name, age)) # python 3

print(f"Hello {name} your age is {age}") # python 3.6 (clean)


# you can also do this
print("Hello {} your age is {}".format(name, age + 10))
print(f"Hello {name} your age is {age + 10}")
