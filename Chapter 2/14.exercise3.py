# Question : take two separated inputs from user 
# 1. user's name , example - "Aryan"
# 2. a single characher , "a"

# Output : 2 print lines
# 1. user's name length
# 2. count the character that user inputed ("bonus : case insensitive count")

# Answer : 

name , single_char = input("Enter your name and a single character comma separeted : ").split(",")
name = name.lower().strip()
single_char = single_char.lower().strip()
print(f"Your name length is : {len(name)}\nCount is : {name.count(single_char)}")
