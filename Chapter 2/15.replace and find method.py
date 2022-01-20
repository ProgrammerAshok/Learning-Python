# replace() method 
# find method

sentence = "I am a programmer and i am also a student"
print(sentence)

# replce method 
print("\nreplace method")
print(sentence.replace(" ", "_")) # Return a copy with all occurrences of substring old replaced by new.
print(sentence.replace("a", "", 8))

# find method
print("\nfind method")
print(sentence.find("am")) # starting finding from position 0
print(sentence.find("am",3)) # now from 3


# finding postion
am_pos1 = sentence.find("am") # am pos1 ---> number 
am_pos2 = sentence.find("am", am_pos1 + 1)
print(am_pos2)
