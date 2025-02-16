# Now that you understand many of the basics of python, it is time to move to some slightly more advanced topics.

# We'll start with control flow. The control flow helps us decide which part of the code to execute based on certain conditions.

# If Statements
# If statements execute code when a condition is true.


x=10

if x > 5:
    print("x is greater than 5")

#So with this block of code above, what do you think would happen if you ran it?

#Furthermore, what do you think would happen if you gave a value of less than 5?

# Now, you try! Write your own if statement where the console will print something if x is less than 5:







# Else and Elif Statements

# Sometimes, you want to check multiple conditions in your code.
# The if statement lets you check one condition, but what if you need to check more than one?
# That's where elif and else statements come into play.

# The elif (short for "else if") statement allows you to check an additional condition if the previous if statement is false.
# You can have multiple elif statements to check various conditions.
# The else statement is used to execute a block of code if none of the previous conditions are true.

# Let's break it down with an example:

x = 10

if x > 15:
    # This block will only execute if x is greater than 15
    print("x is greater than 15")
elif x > 5:
    # This block will execute if the previous condition (x > 15) was false, but this condition (x > 5) is true
    print("x is greater than 5 but less than or equal to 15")
else:
    # This block will execute if none of the above conditions were true
    print("x is 5 or less")

# In this example, Python will first check if x is greater than 15.
# If it is, it will print "x is greater than 15" and skip the rest of the checks.
# If x is not greater than 15, it will move to the next condition and check if x is greater than 5.
# If this condition is true, it will print "x is greater than 5 but less than or equal to 15".
# If neither condition is true, the code inside the else block will run, printing "x is 5 or less".

# Try an elif and else statement for different conditions:







# Nested If Statements

# You can use if statements inside other if statements for more complex conditions.
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")

# Let's think about this block of code:
# What happens if x is greater than 5?
# What about if x is less than 5?

# Now, what if x is less than 15 but still greater than 5?

# But what if x is 16?

# How can we modify this code to check if x is greater than 5 and also an even number?
# Think about adding another nested if statement to check if x % 2 == 0 (this checks if x is even).







# Can you write a nested if statement to check if a number is between 10 and 20 and also a multiple of 3?
# Give it a try and see how you can expand the logic further.








# Let's also consider what will happen if x is set to 5.

# Finally, can you create a nested if statement that includes an else block for both the outer and inner conditions?
# This will help you handle all possible scenarios effectively.

