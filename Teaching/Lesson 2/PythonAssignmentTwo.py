# Loops
# For Loop:
# 1. Write a for loop that prints the numbers from 1 to 10.
# 2. Create a list of your favorite fruits and use a for loop to print each fruit:
'''
for Numb in range(1, 11):
    print(Numb)
'''

'''
fruits = ["orange", "banana", "apple"]
for fruit in fruits:
    print(fruit)
'''

# While Loop:
# 1. Write a while loop that prints numbers from 5 to 15.
# 2. Create a while loop that prints "Hello, World!" 5 times:
'''
x=5
while x < 16:
    print(x)
    x += 1
'''

'''
y=0
while y < 5:
    print("Hello World!")
    y += 1
'''
# Break and Continue:
# 1. Write a for loop that prints numbers from 1 to 20, but stops if the number is 13.
# 2. Create a while loop that prints numbers from 1 to 10, but skips any number divisible by 4:
'''
for z in range(1,21):
    print(z)
    if z == 13:
        break
    '''

'''
for z in range(1,11):
    if z % 4 == 0:
        continue
    print(z)
'''

# If, Elif, and Else Statements
# If Statements:
# 1. Write an if statement that checks if a number is positive and prints "The number is positive."
# 2. Create an if statement that checks if a string contains the letter "a" and prints "The string contains 'a'.":
'''
z = 3
if z > 0:
    print("The Number is Positive.")
'''

'''
z = "Lillia"
if z.__contains__("a") or z.__contains__("A"):
    print("The String contains 'a'.")
'''
# Elif Statements:
# 1. Write a program that checks the temperature and prints whether it's "cold", "warm", or "hot":
'''
cold = "cold"
warm = "warm"
hot = "hot"
very_hot = "very hot"
current_temp = 30
if current_temp <= 0:
    print(cold)
elif 0 < current_temp <= 10:
    print(warm)
elif 30 > current_temp >= 11:
    print(hot)
else:
    print(very_hot)
'''



# 2. Modify the above program to include an additional check for "very hot" if the temperature is above 30:



# Else Statements:
# 1. Write a program that checks if a number is even or odd and prints the result.
# 2. Create a program that checks the user's age and prints whether they are a child, teenager, or adult:
'''
z = 0
if z % 2 == 0 and z != 0:
    print("Number is Even")
elif z == 0:
    print("Number is Zero")
else:print("Number is Odd")
'''



# Input Statements
# Basic Input:
# 1. Ask the user for their favorite movie and print a message that includes their input.
# 2. Write a program that asks the user for their hometown and prints a greeting message:
#1st Method
'''
Movie_Name = input("Write the name of your favorite Movie: ")
print(f"{Movie_Name} is sexy")
'''
#2nd Method
'''
Movie_Name = input("Write the name of your favorite Movie: ")
print(Movie_Name + " is sexy")
'''
#end
'''
HomeTown = input("Writ the name of your Hometown: ")
print(f"{HomeTown} is worse than Bay Roberts")
'''

# Converting Input:
# 1. Ask the user for their birth year, convert it to an integer, and calculate their age.
# 2. Create a program that asks the user for the length and width of a rectangle and calculates the area:
'''
Name_Ask = input("Write the year you were born: ")
Name_Ask = int(Name_Ask)
print(Name_Ask)
Age = 2025 - Name_Ask
print(Age)
'''

'''
Cock_Size_Int = input("Write Length and Width of your cock seperated by a space: ")
Cock_Size_Length, Cock_Size_Width = Cock_Size_Int.split()
print(Cock_Size_Length)
print(Cock_Size_Width)
Cock_Size_Length = int(Cock_Size_Length)
Cock_Size_Width = int(Cock_Size_Width)
Area_Cock = Cock_Size_Length * Cock_Size_Width
print(Area_Cock)
'''


# Handling Multiple Inputs:
# 1. Ask the user for two numbers separated by a comma, split the input, and print the sum of the numbers.
# 2. Write a program that asks for three words separated by spaces and prints each word on a new line:
'''
Two_Numb = input("Write Two Numbers seperated by a comma: ")
Numb1, Numb2 = Two_Numb.split(",")
print(Numb1)
print(Numb2)
Numb1 = int(Numb1)
Numb2 = int(Numb2)
Numb_Sum = Numb1 + Numb2
print(Numb_Sum)
'''

'''
Three_Words = input("Write 3 Words separated by spaces: ")
Word1, Word2, Word3 = Three_Words.split()
print(Word1)
print(Word2)
print(Word3)
'''


# Validating Input:
# 1. Write a program that asks for a username and ensures it contains only letters.
# 2. Create a program that asks for a password and checks if it meets certain criteria (e.g., at least 8 characters long, contains a number):
'''
Username_info = input("Write a username using ONLY letters: ")
Username_info_comp = Username_info.isalpha()
if Username_info_comp is True:
    print("User Name Contains Only Letters")
else:
    print("User Name Contains Numbers and is Invalid")
'''

'''
Password_Crit = input("Write a password that is '8 Characters Long' and 'Contains a Number'")
Numbers = "1234567890"
if Password_Crit.__len__()< 8:
    print("Password is Too Short")
elif any(char in Numbers for char in Password_Crit) is False:
    print("Password Does Not Contain A Number")
else:
    print("Password is Valid")
'''
