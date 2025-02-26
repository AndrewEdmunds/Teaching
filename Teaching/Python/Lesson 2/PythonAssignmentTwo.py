# Loops
# For Loop:
# 1. Write a for loop that prints the numbers from 1 to 10.
'''
for numbers in range (1, 11):
    print(numbers)
'''


# 2. Create a list of your favorite holiday and use a for loop to print each fruit:
'''
holidays = ["christmas", "halloween", "easter"]

for holiday in holidays:
    print(holiday) 
    ''' 

# While Loop:
# 1. Write a while loop that prints numbers from 5 to 15.
'''
n = 5 

while  4 < n < 16:
    print(n)
    n+=1  
'''  
    


# 2. Create a while loop that prints "Hello, World!" 5 times:
'''
m = 1

while m < 6:
    print("Hello World!") 
    m +=1
'''




# Break and Continue:
# 1. Write a for loop that prints numbers from 1 to 20, but stops if the number is 13.
'''
for i in range (1, 21):
    print(i)
    if i == 13:
        break
''' 

# 2. Create a while loop that prints numbers from 1 to 10, but skips any number divisible by 4(Remember your "break"s and "continue"s):
'''
i=1
while i < 11:
    if i % 4 ==0:
        i+=1  
        continue 
    print(i) 
    i+=1
'''    
# If, Elif, and Else Statements
# If Statements:
# 1. Write an if statement that checks if a number is positive and prints "The number is positive."
'''
i = 2
if i > 0:
    print("the number is positve")
'''

# 2. Create an if statement that checks if a string contains the letter "a" and prints "The string contains 'a'.":
'''
string = "banana"
if string.__contains__ ("a"):
    print ("the string contains 'a'.")
'''

# Elif Statements:
# 1. Write a program that checks the temperature and prints whether it's "cold", "warm", or "hot":
'''
temperature = 23
if temperature < 0:
    print("cold")
elif 0 < temperature < 20:
    print("warm")
elif 20 < temperature < 30:
    print("hot")
else:
    print("very hot")
'''


# 2. Modify the above program to include an additional check for "very hot" if the temperature is above 30:







# Else Statements:
# 1. Write a program that checks if a number is even or odd and prints the result.
'''
i = 11
if i % 2 == 0: 
    print("number is even")
elif i % 2 != 0: 
    print("number is odd")
'''




# 2. Create a program that checks the user's age and prints whether they are a child, teenager, or adult:
'''
age = 16
if age < 12:
    print("child")
elif 12 < age < 18:
    print("teenager")
elif age > 18:
    print("adult") 
'''





# Input Statements
# Basic Input:
# 1. Ask the user for their favorite movie and print a message that includes their input.
'''
favourite_movie = input("whats your favourtie movie? ")
print(favourite_movie +"is a great movie")
'''

# 2. Write a program that asks the user for their hometown and prints a greeting message:
'''
hometown = input("what is your hometown? ")
print(hometown + " is a great place to live ")
'''




# Converting Input:
# 1. Ask the user for their birth year, convert it to an integer, and calculate their age.
# 2. Create a program that asks the user for the length and width of a rectangle and calculates the area:

'''
#1
Birth_year = input("Please Enter Your Birth Year Papi: ")

Birth_year = int(Birth_year)

current_year = 2025

age = current_year - Birth_year

print(f"You are {age} years old")
'''
'''
#2
length = int(input("Enter Rectangle Length: "))

width = int(input("Enter Rectangle Width: "))

area = width * length 

print(f"the area of the rectangle is {area}")
'''

# Handling Multiple Inputs:
# 1. Ask the user for two numbers separated by a comma, split the input, and print the sum of the numbers.
# 2. Write a program that asks for three words separated by spaces and prints each word on a new line:

1#
'''
numbers= input("Enter Two Numbers Seperated By A Comma: ")

num1, num2 = numbers.split(",")

sum_of_numbers = int(num1) + int(num2)

print(f"the sum of the numbers is:", sum_of_numbers)
'''
2#
'''
words = input("Enter Three Words Seperated By Space: ")

words = words.split()
for words in words:
    print(words)
'''





# Validating Input:
# 1. Write a program that asks for a username and ensures it contains only letters.
# 2. Create a program that asks for a password and checks if it meets certain criteria (e.g., at least 8 characters long, contains a number):

1#
'''
username = input("Write A Username With Only Letters: ")

username = username.isalpha()
if username is True:
    print("Username Only Has Letters: ")
else:
    print("Username Has Either Numbers Or Symbols: ")
'''
#2
'''
password = input(" Write A Password That Is At Least 8 Characters Long And Contains A Number")
passwordAlphaCheck = password.isalpha()
AllPossibleNumber = "0123456789"
if any(char in AllPossibleNumber for char in password) is False and password.__len__() < 8:
    print("Password Is Not Long Enough And Dont Contain Any Numbers, Can You Read?")
elif any(char in AllPossibleNumber for char in password) is False:
    print("Password Does Not Have Any Numbers But Is Long Enough, Please Learn To Read.")
elif password.__len__() < 8:
    print("Password Isnt Long Enough But Has Numbers ")
else:
    print("Password Is Valid, Good Job ")
'''


    








