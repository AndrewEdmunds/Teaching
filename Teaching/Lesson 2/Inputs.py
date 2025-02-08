# Welcome to lesson 2 of learning Python!

# Input Statements
# Input statements allow you to interact with users by taking input from them.
# This is useful for making your programs dynamic and user-friendly.

# Basic Input
# The `input()` function is used to get input from the user. The input is always received as a string.

#name = input("Enter your name: ")
#print(f"Hello, {name}!")

# In this code block, the program asks for the user's name and then greets them.

# Try it yourself!
# Ask the user for their favorite "thing" is and print a message that includes their input:
'''
favourite_thing = input ("favourite food:")
print(f"your favorite food is {favourite_thing}! ")
'''


# Converting Input
# Since the `input()` function returns a string, you'll often need to convert the input to another data type.

#age = input("Enter your age: ")
#age = int(age)  # Convert the input to an integer
#print(f"You are {age - 2} years old.")

# In this example, the input is converted from a string to an integer.

# Exercise:
# Ask the user for their height in centimeters and convert it to meters (you convert from centimeters to
# meters by dividing by 100) and then print the result:
'''
Height = input("enter your height in cm ")
Height = int(Height) 

print(f"you are {Height / 100 } in meters ")
'''
# Handling Multiple Inputs
# You can handle multiple inputs by using the `split()` method.
'''
numbers = input("Enter Three numbers separated by a space: ")
num1, num2, num3 = numbers.split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
print(f"The sum of the numbers is {num1 + num2 - num3}.")
'''
# In this code, the user enters two numbers, which are then split and converted to integers.

# Activity:
# Ask the user for three favorite foods separated by commas. Print each food on a new line:
'''
foods= input("name 3 foods you like with spaces ") 

food1, food2, food3 = foods.split()

print(food1) 
print(food2)
print(food3)
'''



# Using Input in Loops
# You can use the `input()` function inside loops to continually ask for user input.
'''
while True:
    command = input("Enter a command (or 'exit' to quit): ")
    if command == "exit":
        break
    print(f"You entered: {command}")
'''
# This loop will keep asking for a command until the user types "exit".

# Challenge:
# Write a loop that asks the user to enter numbers. If the user enters a negative number, exit the loop. Otherwise, print the square of the number:
'''
while True:
    number = input("enter a number")
    number = int(number)
    if number < 0:
        print("exit the loop")
        break
    else:
        print(f"the sqaure root of number is {number**0.5}")
'''




# Validating Input
# It's important to validate user input to ensure your program handles errors gracefully.
'''
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        print(f"Your age is {age}.")
        break
    else:
        print("Please enter a valid number.")
'''
# This loop will keep asking for age until a valid number is entered.

# Exercise:
# Ask the user to enter a valid email address (containing "@" and ".").
# Keep asking until a valid email is entered:

  





# Combining It All
# Let's create a program that combines everything we've learned about input statements.

while True:
    name = input("Enter your name: ")
    if not name.isalpha():
        print("Please enter a valid name using letters only.")
        continue
    
    age = input("Enter your age: ")
    if not age.isdigit():
        print("Please enter a valid age in numbers.")
        continue

    age = int(age)
    
    print(f"Hello, {name}. You are {age} years old.")
    break

# This program ensures that both the name and age inputs are valid before proceeding.

# Final Exercise:
# Write a program that asks for the user's name, age, and favorite number.
# Validate each input and print a message that includes all the information:







# And that's it for input statements! Keep practicing, and you'll master taking user input in no time.

# Happy coding!
