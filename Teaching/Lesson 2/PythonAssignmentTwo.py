# Loops
# For Loop:
# 1. Write a for loop that prints the numbers from 1 to 10.
# 2. Create a list of your favorite fruits and use a for loop to print each fruit:

i = 1
for i in range(1,11):
    print(i)


candies= ["starbursts", "nerds", "rockets", "jolly ranchers", "marshmallows"]

for candy in candies:
    print(candy)



# While Loop:
# 1. Write a while loop that prints numbers from 5 to 15.
# 2. Create a while loop that prints "Hello, World!" 5 times:

p = 5

while 15>=p>=5:
    print(p)
    p+=1


q = 1
while q<=5:
    print("Hello World!")
    q+=1


# Break and Continue:
# 1. Write a for loop that prints numbers from 1 to 20, but stops if the number is 13.
# 2. Create a while loop that prints numbers from 1 to 10, but skips any number divisible by 4:

q=1
for q in range(1,20):
    print(q)
    q+=1
    if q == 13:
        break



# If, Elif, and Else Statements
# If Statements:
# 1. Write an if statement that checks if a number is positive and prints "The number is positive."
# 2. Create an if statement that checks if a string contains the letter "a" and prints "The string contains 'a'.":

number = 1

if number > 0:
    print("the number is positive")


string = "Andrew"

if string.__contains__("A"):
    print("The string contains A")


# Elif Statements:
# 1. Write a program that checks the temperature and prints whether it's "cold", "warm", or "hot":

temp = -19


if temp > 20:
    print("its hot")
elif temp > 0:
    print("its warm")
elif temp <= 0:
    print("Its cold")



# 2. Modify the above program to include an additional check for "very hot" if the temperature is above 30:

if temp > 30:
    print("its very hot")
elif temp > 20:
    print("its hot")
elif temp > 0:
    print("its warm")
elif temp <= 0:
    print("Its cold")





# Else Statements:
# 1. Write a program that checks if a number is even or odd and prints the result.
# 2. Create a program that checks the user's age and prints whether they are a child, teenager, or adult:

value = 3

if value % 2==0:
    print("the value is even")
else:
    print("The value is odd")





# Input Statements
# Basic Input:
# 1. Ask the user for their favorite movie and print a message that includes their input.
# 2. Write a program that asks the user for their hometown and prints a greeting message:







# Converting Input:
# 1. Ask the user for their birth year, convert it to an integer, and calculate their age.
# 2. Create a program that asks the user for the length and width of a rectangle and calculates the area:







# Handling Multiple Inputs:
# 1. Ask the user for two numbers separated by a comma, split the input, and print the sum of the numbers.
# 2. Write a program that asks for three words separated by spaces and prints each word on a new line:







# Validating Input:
# 1. Write a program that asks for a username and ensures it contains only letters.
# 2. Create a program that asks for a password and checks if it meets certain criteria (e.g., at least 8 characters long, contains a number):
