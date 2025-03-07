//===============================================
//JavaScript Lesson 1: Introduction to JavaScript
//===============================================
/*
JavaScript is a programming language used to make web pages interactive. If Python is like writing instructions for a computer to follow, JavaScript is like adding a layer of interaction to web pages.

You’ve already learned Python, so some of the concepts will feel familiar, but JavaScript has its own way of doing things. Let’s start with the basics.

Printing to the Console
Just like Python has print(), JavaScript uses console.log() to display output.

Python vs. JavaScript
Python:

print("Hello, world!")
JavaScript:
*/
console.log("Hello, world!");

/*
Try running this in your browser’s developer console! (Right-click a webpage, click "Inspect," go to "Console," and type the code.)

Variables
Variables in JavaScript store data, just like in Python. But instead of x = 10, we use let, const, or var.

Python vs. JavaScript

Python:
x = 10

JavaScript:
*/
let x = 10;  // or const x = 10;

/*
let is like a normal variable (it can change).
const is like a constant (it cannot change).


Try declaring a variable in JavaScript and printing it using console.log().

Data Types
JavaScript and Python have similar data types:

Numbers (10, 3.14)
Strings ("Hello", 'World')
Booleans (true, false)
Python:

name = "Alice"
age = 25
is_student = True

JavaScript:
*/
let name = "Alice";
let age = 25;
let isStudent = true;
/*
Notice that true and false in JavaScript are lowercase.

Basic Operators
Just like in Python, JavaScript has:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulo - remainder after division)
Example in JavaScript:
*/
let a = 10;
let b = 3;
console.log(a + b);  // 13
console.log(a % b);  // 1

/*
Try performing basic math operations in JavaScript.

If Statements
Conditional statements in JavaScript work like Python but with different syntax.

Python:

x = 10
if x > 5:
    print("x is greater than 5")
JavaScript:

*/
let y = 10;
if (y > 5) {
    console.log("x is greater than 5");
}
/*
Notice the curly braces {} instead of indentation.

Conclusion
JavaScript and Python share many similarities, but JavaScript has its own syntax and rules. In the next lesson, we’ll explore loops, functions, and how JavaScript interacts with web pages.

Try This!

Declare a variable and print it using console.log().
Write an if statement that checks if a number is even (use x % 2 === 0).*/