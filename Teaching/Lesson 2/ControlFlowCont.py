# Now that you understand the basics of control flow with if, elif, and else statements, now we move onto loops!

# Loops
# Loops are essential in programming. They help us automate repetitive tasks and iterate over sequences. 
# We'll start with the basic types of loops in Python: `for` and `while`.

# For Loops
# A `for` loop is used for iterating or "going over" a sequence (like a list, tuple, dictionary, set, or string). 

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# In this code block, the `for` loop will print each fruit in the `fruits` list.

# Try it yourself!
# Create a list of your favorite anything.
# Write a `for` loop to print each items name:







# While Loops
# A `while` loop will continue to execute as long as its condition remains true.

i = 1

while i < 6:
    print(i)
    i += 1



# This loop will print numbers 1 to 5. The loop will stop when `i` becomes 6.

# Exercise:
# Write a `while` loop to print numbers from 10 to 1:







# Break and Continue
# Sometimes you need more control over your loops. This is where `break` and `continue` come in.
# `break` will stop the loop entirely.
# `continue` will skip the current iteration and continue with the next one.

# Example with `break`:

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# This will print numbers 1 to 4 and then stop.

# Example with `continue`:

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

# This will print numbers 1 to 4 and 6 to 9, skipping 5.

# Activity:
# Write a `for` loop that prints numbers from 1 to 10, but skips any number divisible (x % y == 0) by 3:







# Challenge:
# Write a nested loop to print a multiplication table (1-10):







# Loop Control with Else
# In Python, you can also have an `else` block with loops. The `else` part is executed when the loop finishes normally (not stopped by `break`).

for i in range(5):
    print(i)
else:
    print("Loop finished normally.")

# Thought Experiment:
# What do you think will happen if you add a `break` statement inside the loop?







# Infinite Loops
# Be cautious of infinite loops! They can crash your program if not handled correctly.

while True:
    print("This will run forever unless you stop it.")
    break  # comment this line to cause an infinite loop

# Safety Tip:
# Always make sure there's a way out of your loop.







# Summary and Practice
# We've covered the basics of `for` loops, `while` loops, `break` and `continue` statements, nested loops, loop control with `else`, and the dangers of infinite loops.

# Final Exercise:
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three, print "Fizz" instead of the number.
# For multiples of five, print "Buzz".
# For numbers which are multiples of both three and five, print "FizzBuzz":

# And that's it for loops! Keep practicing, and you'll master loops in no time.

# Happy coding!


names = ["Andrew", "Brady", "Teegan"]
name_1, name_2, name_3 = names[0], names[1], names[2]
positions = ["Top Lane", "Jungle", "Mid Lane", "ADC", "Support"]
position_1, position_2, position_3, position_4, position_5 = positions[0], positions[1], positions[2], positions[3], positions[4]
Teegans_Lane = ""
Andrews_Lane = ""
Bradys_Lane = ""
Teegans_Acceptable_Positions = [position_2, position_5]
Andrews_Acceptable_Positions = [position_1, position_2, position_4, position_5]
Bradys_Acceptable_Positions = [position_1, position_2, position_3, position_4, position_5]
Andrews_Final_Lane = ""
Bradys_Final_Lane = ""
Teegans_Final_Lane = ""
choice_2 = ""



print("What lane should we all play?")

while True:
    while Teegans_Lane not in Teegans_Acceptable_Positions:
        Teegans_Lane = input(f"What lane should {name_3} play?: ")
        if Teegans_Lane == position_3:
            print(f"well {name_3} sucks mid, so that's an auto loss")
        elif Teegans_Lane == position_1:
            print(f"uh... if you're putting {name_3} in {position_1} you're just gonna run into the same issue as putting {name_3} in {position_3}...")
        elif Teegans_Lane == position_2:
            print(f"Y'know what? Putting {name_3} in {position_2} means he can't run it down too hard, so definitely a possibility")
        elif Teegans_Lane == position_4:
            print(f"Why the actual fuck would {name_3} play {position_4}?")
        elif Teegans_Lane == position_5:
            print("Well you might as well put him in the lane that's kinda expected to run it down...")
        elif Teegans_Lane not in positions:
            print("bro you didn't even pick one of the lanes")
        else:
            print("Bro I dont even know how you got here")
            break


    while Teegans_Lane not in Teegans_Final_Lane:
        Teegans_Final_Lane = input(f"Okay, so what lane do you really think we should stick him in, {position_2} or {position_5}?: ")

        if Teegans_Final_Lane == position_2:
            print(f"Alright! So we'll stick him in {position_2}! Hopefully you're not expecting any ganks...")
        elif Teegans_Final_Lane == position_5:
            print(f"Alright! We'll stick him in {position_5}! At least he won't make our laning experience worse!")
        else:
            print(f"Bro, can you just pick '{position_2}' or '{position_5}'?")


    while choice_2 != name_1 and choice_2 != name_2:
        choice_2 = input(f"Alright, now that we have {name_3} out of the way, who do you want to choose next? {name_1}? or {name_2}?: ")
        if choice_2 == name_1:
            Final_Name = name_2
            print(f"Alright, lets try to find a role for {name_1}.")
            while Andrews_Lane not in Andrews_Acceptable_Positions:
                Andrews_Lane = input(f"So which role do you think {name_1} Should play?: ")
                if Andrews_Lane == Teegans_Final_Lane:
                    print(f"You can't put {name_1} in {name_3}s lane?")
                elif Andrews_Lane == position_1:
                    print(f"well {name_1} barely plays {position_1}, but I'm sure he'd manage")
                elif Andrews_Lane == position_2:
                    print(f"It's safe to say it's a pretty close one for who's the best jungler between {name_1} and {name_2}, so this would definitely be a solid choice")
                elif Andrews_Lane == position_3:
                    print(f"{position_3} is definitely {name_1}s weakest lane, so that's probably not the best idea")
                elif Andrews_Lane == position_4:
                    print(f"{name_1} is definitely the most cracked {position_4} out of the three of us, so this is definitely a solid choice")
                elif Andrews_Lane == position_5:
                    print(f"You know {name_1} would literally rather run it down than play {position_5} without {name_2} in {position_4} right? Maybe keep that in mind...")
                elif Andrews_Lane not in positions:
                    print("bro you didn't even pick one of the lanes")
                else:
                    print("Bro I dont even know how you got here")
                    break
            while Andrews_Final_Lane not in Andrews_Acceptable_Positions:
                Andrews_Final_Lane = input(f"Okay so what is the final decision on where {name_1} is going?: ")
                if Andrews_Final_Lane == position_1:
                    print(f"Alright, we'll put {name_1} in {position_1} this should be fine")
                elif Andrews_Final_Lane == position_2:
                    print(f"Alright, we'll put {name_1} in {position_2}, I'm sure he'll do a good job")
                elif Andrews_Final_Lane == position_4:
                    print(f"ALright we'll put {name_1} as {position_4}, this is probably for the best")
                elif Andrews_Final_Lane == position_5:
                    print(f"Are you sure? Well I hope you at least put {name_2} as {position_5}...")
        elif choice_2 == name_2:
                        print(f"Alright, lets try to find a role for {name_2}.")
                        while Bradys_Lane not in Bradys_Acceptable_Positions:
                            Bradys_Lane = input(f"So which role do you think {name_2} Should play?: ")
                            if Bradys_Lane == Teegans_Final_Lane:
                                print(f"You can't put {name_2} in {name_3}s lane?")
                            elif Bradys_Lane == position_1:
                                print(f"well {name_2} is definitely our {position_1} main, so that's definitely valid")
                            elif Bradys_Lane == position_2:
                                print(f"It's safe to say it's a pretty close one for who's the best jungler between {name_1} and {name_2}, so this would definitely be a solid choice")
                            elif Bradys_Lane == position_3:
                                print(f"Well {name_2} don't main {position_3}, but he does have experience... I guess theres nothing wrong with it")
                            elif Bradys_Lane == position_4:
                                print(f"Well {name_1} is definitely our {position_4} main, but I guess {name_2} is alright too...")
                            elif Bradys_Lane == position_5:
                                print(f"{name_2} is a cracked {position_5}, so yeah that's hot")
                            elif Andrews_Lane not in positions:
                                print("bro you didn't even pick one of the lanes")
                            else:
                                print("Bro I dont even know how you got here")
                                break
                        while Bradys_Final_Lane not in Bradys_Acceptable_Positions:
                            Bradys_Final_Lane = input(f"Okay so what is the final decision on where {name_2} is going?: ")
                            if Bradys_Final_Lane == position_1:
                                print(f"Alright, we'll put {name_2} in {position_1} I'm sure he'll do well")
                                choice_2 = name_2
                                
                            elif Bradys_Final_Lane == position_2:
                                print(f"Alright, we'll put {name_2} in {position_2}, I'm sure he'll do a good job")
                                choice_2 = name_2
                                
                            elif Bradys_Final_Lane == position_3:
                                print(f"Alright, we'll put {name_2} in {position_3}, that's probably for the best")
                                choice_2 = name_2
                                
                            elif Bradys_Final_Lane == position_4:
                                print(f"Alright, we'll put {name_2} in {position_4}, strange choice but valid")
                                choice_2 = name_2
                                
                            elif Bradys_Final_Lane == position_5:
                                print(f"Again, another solid choice")
                                choice_2 = name_2
                                

            
        else:
            print(f'You need to pick either "{name_1}" or "{name_2}"')

    choice_3 = name_1 if choice_2 == name_2 else name_2
    if choice_3 == name_1:
        print(f"Alright, lets finish it off with {name_1}.")
        while Andrews_Lane not in Andrews_Acceptable_Positions:
            Andrews_Lane = input(f"So which role do you think {name_1} Should play?: ")
            if Andrews_Lane == Teegans_Final_Lane:
                print(f"You can't put {name_1} in {name_3}s lane?")
            elif Andrews_Lane == position_1:
                print(f"well {name_1} barely plays {position_1}, but I'm sure he'd manage")
            elif Andrews_Lane == position_2:
                print(f"It's safe to say it's a pretty close one for who's the best jungler between {name_1} and {name_2}, so this would definitely be a solid choice")
            elif Andrews_Lane == position_3:
                print(f"{position_3} is definitely {name_1}s weakest lane, so that's probably not the best idea")
            elif Andrews_Lane == position_4:
                print(f"{name_1} is definitely the most cracked {position_4} out of the three of us, so this is definitely a solid choice")
            elif Andrews_Lane == position_5:
                print(f"You know {name_1} would literally rather run it down than play {position_5} without {name_2} in {position_4} right? Maybe keep that in mind...")
            elif Andrews_Lane not in positions:
                print("bro you didn't even pick one of the lanes")
            else:
                print("Bro I dont even know how you got here")
                break
        while Andrews_Final_Lane not in Andrews_Acceptable_Positions:
            Andrews_Final_Lane = input(f"Okay so what is the final decision on where {name_1} is going?: ")
            if Andrews_Final_Lane == position_1:
                print(f"Alright, we'll put {name_1} in {position_1} this should be fine")
            elif Andrews_Final_Lane == position_2:
                print(f"Alright, we'll put {name_1} in {position_2}, I'm sure he'll do a good job")
            elif Andrews_Final_Lane == position_4:
                print(f"ALright we'll put {name_1} as {position_4}, this is probably for the best")
            elif Andrews_Final_Lane == position_5:
                print(f"Are you sure? Well I hope you at least put {name_2} as {position_5}...")
    elif choice_3 == name_2:
        print(f"Alright, lets try to find a role for {name_2}.")
        while Bradys_Lane not in Bradys_Acceptable_Positions:
            Bradys_Lane = input(f"So which role do you think {name_2} Should play?: ")
            if Bradys_Lane == Teegans_Final_Lane:
                print(f"You can't put {name_2} in {name_3}s lane?")
            elif Bradys_Lane == position_1:
                print(f"well {name_2} is definitely our {position_1} main, so that's definitely valid")
            elif Bradys_Lane == position_2:
                print(f"It's safe to say it's a pretty close one for who's the best jungler between {name_1} and {name_2}, so this would definitely be a solid choice")
            elif Bradys_Lane == position_3:
                print(f"Well {name_2} don't main {position_3}, but he does have experience... I guess theres nothing wrong with it")
            elif Bradys_Lane == position_4:
                print(f"Well {name_1} is definitely our {position_4} main, but I guess {name_2} is alright too...")
            elif Bradys_Lane == position_5:
                print(f"{name_2} is a cracked {position_5}, so yeah that's hot")
            elif Andrews_Lane not in positions:
                print("bro you didn't even pick one of the lanes")
            else:
                print("Bro I dont even know how you got here")
                break
        while Bradys_Final_Lane not in Bradys_Acceptable_Positions:
            Bradys_Final_Lane = input(f"Okay so what is the final decision on where {name_2} is going?: ")
            if Bradys_Final_Lane == position_1:
                print(f"Alright, we'll put {name_2} in {position_1} I'm sure he'll do well")
            elif Bradys_Final_Lane == position_2:
                print(f"Alright, we'll put {name_2} in {position_2}, I'm sure he'll do a good job")
            elif Bradys_Final_Lane == position_3:
                print(f"Alright, we'll put {name_2} in {position_3}, that's probably for the best")
            elif Bradys_Final_Lane == position_4:
                print(f"Alright, we'll put {name_2} in {position_2}, strange choice but valid")
            elif Bradys_Final_Lane == position_5:
                print(f"Again, another solid choice")







