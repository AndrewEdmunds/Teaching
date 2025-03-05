// ==========================================
// JavaScript Lesson 2: Functions & Loops
// ==========================================

// Functions
// ---------
// Functions allow us to group code together and reuse it.
// In Python, you defined functions using `def`, but in JavaScript, we use `function`.

// Example:
function sayHello() {
    console.log("Hello, world!");
}

// To call (execute) the function, we use its name followed by parentheses:
sayHello();  // This will print "Hello, world!" to the console.

// ➡ Try it out: Define a function named greet that prints "Welcome to JavaScript!" and call it.


function Intro() {
    console.log("Welcome to JavaScript!")
}
Intro()


// Parameters & Arguments
// ----------------------
// Functions can accept inputs (called parameters) to make them more useful.
// In Python: `def greet(name):`
// In JavaScript:

function greet(name) {
    console.log("Hello, " + name + "!");
}

// Now we can call the function and pass a value (argument) for "name":
greet("Alice");
greet("Bob");

// ➡ Try it out: Modify the function so that it also prints "Have a great day!" after the greeting.


function GreatDay(dayweek) {
    console.log("Have a great" + dayweek + "!")
}
GreatDay("Friday")


// Returning Values
// ----------------
// Functions can return values instead of just printing them.
// In Python: `return` is used, and it's the same in JavaScript.

function add(a, b) {
    return a + b;
}

// We can store the result in a variable:
let sum = add(5, 7);
console.log(sum);  // Prints 12

// ➡ Try it out: Create a function called `multiply` that takes two numbers and returns their product.


function multiply(y, z) {
    return y * z
}
let numbs = multiply(3, 7)
console.log(numbs)


// Loops: Repeating Code
// ----------------------
// In Python, we use `for` and `while` loops to repeat tasks.
// JavaScript has similar loops, but with a different syntax.

// For Loop (like Python's `for i in range(...)`):
// Runs a block of code a set number of times.

for (let i = 1; i <= 5; i++) {
    console.log("Iteration " + i);
}

// ➡ Try it out: Modify the loop to count from 1 to 10 instead.


for (let k = 1; k <= 10; k++) {
    console.log("Miku " + k)
}


// While Loop (like Python's `while` loop):
// Runs as long as a condition is true.

let count = 0;
while (count < 3) {
    console.log("Count is: " + count);
    count++;
}

// ➡ Try it out: Modify the loop to count from 1 to 5.


let counter = 0
while (counter < 6) {
    console.log("Counter has reached: " + counter)
    counter++
}


// Looping Through Arrays
// ----------------------
// In Python, we loop through lists using `for item in my_list:`
// In JavaScript, we do the same with arrays.

let fruits = ["Apple", "Banana", "Cherry"];

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);  // Prints each fruit
}

// ➡ Try it out: Add another fruit to the array and loop through it again.


fruits.push("Grape")
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}


// Final Challenge:
// ----------------
// 1. Write a function named `isEven` that takes a number as a parameter.
// 2. It should return `true` if the number is even, otherwise return `false`.
// 3. Use a loop to print all even numbers from 1 to 10 by calling your function.


function isEven(J) {
    if (J % 2 == 0) {
        return true
    }    
    else {
        return false
    }
    }
    for (let Problem = 1; Problem < 11; Problem++) {
        if (isEven(Problem)) {
            console.log(Problem)
        }
    }

