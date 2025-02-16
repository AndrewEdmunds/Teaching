#inputs 
# 1 
favourite_thing = input ("favourite food:")
print(f"your favorite food is {favourite_thing}! ")

#2
Height = input("enter your height in cm ")
Height = int(Height) 

print(f"you are {Height / 100 } in meters ")

#3
numbers = input("Enter Three numbers separated by a space: ")
num1, num2, num3 = numbers.split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
print(f"The sum of the numbers is {num1 + num2 - num3}.")

#4
foods= input("name 3 foods you like with spaces ") 

food1, food2, food3 = foods.split()

print(food1) 
print(food2)
print(food3)

# controlflow

#1

q=3

if q < 5:
    print("q is less then 5")

#2

leagueOfLegends = "not really fun" 

if leagueOfLegends == "fun":
    print("lets play")
elif leagueOfLegends == "not fun":
    print("dont get on")
else:
    print("fuck off")

#3

b = 5
if b > 5:
    if b % 2 == 0:
        print("b is greater then 5 and also a even number")
    else:
        print("not a even number but is greater then 5")
elif b < 5:
    if b % 2 != 0:
        print("b is less then 5 but not a even number")
    else:
        print("b is less then 5 and is a even number")
else:
    print("b is equal to 5")

#4

a = 7
if 10 < a < 20:
    if a % 3 == 0:
        print("a is between 10 and 20 and is a multiple of 3")
    elif a % 3 != 0:
        print ("a is between 10 and 20 but not a multiple of 3")
else:
    print ("a is not between 10 and 20")










