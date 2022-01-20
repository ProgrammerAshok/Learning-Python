# strip method and more

name = "     Ashok     "
dots = "............."
print(name + dots)

# lstrip method
print("\nlstrip method")
print(name.lstrip() + dots) # Return a copy of the string with leading whitespace removed

# rstrip method
print("\nrstrip method")
print(name.rstrip() + dots) # Return a copy of the string with trailing whitespace removed.

# strip method
print("\nstrip method")
print(name.strip() + dots) # Return a copy of the string with leading and trailing whitespace removed.
