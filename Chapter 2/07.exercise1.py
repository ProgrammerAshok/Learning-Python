# Question : Ask user to input 3 numbers and you have to print average of three numbers using string formatting
# Bonus : try to take all three comma seprated inputes in one line

# Answer :

num1, num2, num3 = input("Enter 3 numbers (comma seprated ,) : ").split(",")
total = (int(num1) + int(num2) + int(num3))/3
print(f"The average of these 3 numbers is : {total}")
