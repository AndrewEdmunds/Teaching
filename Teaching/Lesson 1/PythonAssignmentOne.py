# This assignment will take you through some of the topics we covered in today's lesson.

# Question one: Please write a simple print statement
# Write a Python script to print the following message: "Hello, world!"

print("Hello, World!")



# Question two: Please write two variables that you will use in a math question. (assign 2 different numbers to 2 different variables)

Lillia = 11

Irelia = 8



# Question three: Please now use the variables you created to solve a math problem. (the math operators in python are
# addition: "+", subtraction: "-", multiplication: "*", and division: "/")

print(Irelia*Lillia)



# Question four: Please create a list of your favorite League of Legends Characters, add a new League of Legends Characters to the list, and then sort the list in alphabetical order.
# Print the final list.

League_Characters=["Lillia","Irelia","Jinx"]

League_Characters.append("Gwen")

League_Characters.sort()

print(League_Characters)



# Question five: Given the following dictionary, retrieve and print the age and height of "Teegan".
people = {
    "Andrew": {"age": 22, "height": "5ft 11in"},
    "Brady": {"age": 21, "height": "5ft 4in"},
    "Teegan": {"age": 7, "height": "3ft 7in"}
 }

print(people["Teegan"])



# Question six: Using the same dictionary from Question five, add a new key-value pair to "Andrew" with the key "favorite_color" and the value "blue".
# Print the updated dictionary.

(people["Andrew"].update(favorite_color="blu"))
print(people["Andrew"])



# Question seven: Write a Python script to create a list of numbers from 1 to 10. Remove the number 5 from the list, append the number 11 to the list, and then reverse the list.
# Print the final list.

Numbers=[1,2,3,4,5,6,7,8,9,10]

Numbers.pop(4)

Numbers.append(11)

Numbers.reverse()

print(Numbers)



# Question eight: Write a Python script to:
# 1. Print all the keys in the given dictionary.
# 2. Print all the values in the given dictionary.
# 3. Remove the entry for "Brady" and print the updated dictionary.
Goofy_Bitches = {
     "Andrew": {"age": 22, "height": "5ft 11in"},
     "Brady": {"age": 21, "height": "5ft 4in"},
     "Teegan": {"age": 7, "height": "3ft 7in"}
 }

print(Goofy_Bitches.keys())

print(Goofy_Bitches.values())

Goofy_Bitches.pop("Brady")

print(Goofy_Bitches)


