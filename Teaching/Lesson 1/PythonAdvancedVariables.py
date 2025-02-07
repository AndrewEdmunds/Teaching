#Now on to some more complex variables in python.

#The first one we will cover is lists.

#A list in python is much like a physical list as in it contains multiple different elements.

#While a variable such as an integer can only ever contain one element, for example "x = 1" can
#only ever contain the value of 1, a list can contain multiple values. An example of this is as follows:

FirstList = [1,"pineapple",22,34,"Fork"]

#If you would like to see the entire list you can use the following line of code:

#print(FirstList)

#However you can also do other things with lists such as selecting a specific item in the list:

#print(FirstList[3])

#There are also many functions you can preform on lists. A few of them include:

#Append:

FirstList.append("appended")

#print(FirstList)

#What the append function accomplishes is as you can see from the console, it adds another element to
#the end of the list.

#Pop:

FirstList.pop()
#print(FirstList)

#As you can see, the pop function is simply the inverse of the Append function where the append function
#adds a new element onto the end of the list, the pop function removes the last element in the list from
#the list.

#extend

AdditionalItems = ["food", "vehicles", 24]

FirstList.extend(AdditionalItems)

#print(FirstList)

#As you can see here the extend function takes one list and adds it on to the end of another list, in function,
#it is simply a version of append that can add multiple elements rather than only 1.

#clear

FirstList.clear()

#print(FirstList)

#What this function achieves is it deletes the entire contents of the list, leaving you with an empty list.

#While there are many more functions you can preform on lists, they are all quite as simple as each other
#therefore if you understand how and why these previous functions work you will have no problem understanding
#the others.







#Next up we will go over dictionaries.

#Dictionaries are a very useful way of storing data.

#While lists are a very basic way of storing data, dictionaries are much more organized. They assign keys to
#values in the dictionary. you can have keys such as "name", "height", "age", or any amount of descriptors and
#you would then assign values to the keys. Here is an example:

person = {"name": "Andrew", "height": "5ft 11in"}

#now say you wanted to "search" for the name of a person, you would do so with the next line where you
#print the name of the person variable:

#print(person["name"])

#As you can see, it returns the name value from the variable.

#you can also create more complex dictionaries such of the following "dictonary of dictonaries":

people = {
    "Andrew": {"age": 22, "height": "5ft 11in"},
    "Brady": {"age": 21, "height": "5ft 4in"},
    "Teegan": {"age": 7, "height": "3ft 7in"}
    }

#This can be useful because say you would like to get the information of a person from their name,
#you would do so with the following print statement:

#print(people["Andrew"])

#That concludes the basics on dictionaries and how they work, now just like lists you can preform
#different functions on dictionaries, we will now go over a few.

#add a person

people["Brian"] = {"age": 47, "height": "6ft 1in"}

#print(people)

#as you can see from the output, this is how you would add a new person to the list, in essence, it
#functions similarly to the append function on a list.

#remove a person
people.pop("Brady")

#print(people)

#as seen above, the pop functions exactly as it does on dictionaries, except you need to specify which
#entry you want to delete.

#adding a new key and value

people["Andrew"].update({"job": "Full Stack Developer"})

#print(people["Andrew"])

#this function is how you would add a new key and value to an item in a list.

#similarly to lists, there are many functions that you can preform on dictionaries but none are
#truly on a different level of complexity to each other, so I will leave it there.