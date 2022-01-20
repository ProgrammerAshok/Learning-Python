# step argument
story = "A programmer become a software devloper"

# syntax - ["start argument : stop argument : step argument"]

print(story[::2]) # step 1 means 0 step skiping step 2 means 1 step skiping
print(story[12::-1])
print(story[-1::-1])
print(story[::-1]) # trick same as story[-1::-1]
