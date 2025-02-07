# This assignment will take you through some of the topics we covered in today's lesson.

# Question one: Please write a simple print statement
# Write a Python script to print the following message: "Hello, world!"

#print ("hello, world!")





# Question two: Please write two variables that you will use in a math question. (assign 2 different numbers to 2 different variables)

x = 2 
w = 8







# Question three: Please create two variable and solve a math problem with them. (the math operators in python are
# addition: "+", subtraction: "-", multiplication: "*", and division: "/")

x = 10 
print( 5 + x )






# Question four: Please create a list of your favorite lol champs, add a new champ to the list, and then sort the list in alphabetical order.
# Print the final list.

firstlist=["vi", "amumu", "volibear", "nasus", "neeko",]

firstlist.append ("teemo",) 

firstlist.sort()

#print(firstlist)
# Question five: Given the following dictionary, retrieve and print the age and height of "Teegan".
people = {
     "Andrew": {"age": 22, "height": "5ft 11in"},
     "Brady": {"age": 21, "height": "5ft 4in"},
     "Teegan": {"age": 7, "height": "3ft 7in"}
}
#print(people["Teegan"])






# Question six: Using the same dictionary from Question five, add a new key-value pair to "Andrew" with the key "favorite_color" and the value "blue".
# Print the updated dictionary.

people["Andrew"].update({"favourite_color": "blue"}) 


people["Andrew"]


#print(people["Andrew"])


# Question seven: Write a Python script to create a list of numbers from 1 to 10. Remove the number 5 from the list, append the number 11 to the list, and then reverse the list.
# Print the final list.

numberlist=[1, 2, 3, 4, 5, 6,7, 8, 9, 10]

numberlist.pop(4)

numberlist.append(11)

numberlist.reverse()


#print(numberlist)

# Question eight: Write a Python script to:
# 1. Print all the keys in the given dictionary.
# 2. Print all the values in the given dictionary.
# 3. Remove the entry for "Brady" and print the updated dictionary.


people = {
     "Andrew": {"age": 22, "height": "5ft 11in"},
     "Brady": {"age": 21, "height": "5ft 4in"},
     "Teegan": {"age": 7, "height": "3ft 7in"}
 }



#print(people.keys())

#print(people.values())

people.pop("Brady")

#print(people)
