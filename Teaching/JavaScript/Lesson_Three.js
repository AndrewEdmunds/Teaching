// =====================
// Methods In JavaScript
// =====================

/*
JavaScript Methods
Now that you know about variables, loops, conditionals, and functions, it's time to talk about methods.

What Are Methods?
A method is simply a function that belongs to an object. Many built-in objects in JavaScript have their own methods that allow us to perform actions on them.

For example, you've been using console.log() to print messages to the console. Here, log is a method of the console object.

Methods exist for different data types, including strings, arrays, numbers, objects, and even HTML elements.
*/

/*
String Methods
Strings have built-in methods that allow us to manipulate text.
*/

let message = "  Hello, JavaScript!  ";

// Convert to uppercase
console.log(message.toUpperCase());

// Convert to lowercase
console.log(message.toLowerCase());

// Remove spaces from both sides
console.log(message.trim());

// Find the length of the string
console.log(message.length);

// Replace part of the string
console.log(message.replace("JavaScript", "World"));

// Extract part of the string (substring)
console.log(message.slice(2, 7));

// Check if a string contains a word
console.log(message.includes("JavaScript"));
console.log(message.includes("Python"));

// Split a string into an array
let words = message.split(" ");
console.log(words);

/*
Array Methods
Arrays have many useful methods for adding, removing, and manipulating items.
*/

let fruits = ["Apple", "Banana", "Cherry"];

// Add an item to the end
fruits.push("Mango");
console.log(fruits);

// Remove the last item
fruits.pop();
console.log(fruits);

// Remove the first item
fruits.shift();
console.log(fruits);

// Add an item to the beginning
fruits.unshift("Grapes");
console.log(fruits);

// Get the index of an item
console.log(fruits.indexOf("Banana"));

// Remove an item at a specific index
fruits.splice(1, 1);
console.log(fruits);

// Join array elements into a string
console.log(fruits.join(" - "));

// Reverse the array
console.log(fruits.reverse());

// Sort the array (alphabetically)
let numbers = [5, 2, 10, 1];
console.log(numbers.sort());
console.log(numbers.sort((a, b) => a - b));

/*
Number Methods
Numbers also have built-in methods.
*/

let num = 4.5678;

// Round a number
console.log(num.toFixed(2));

// Convert to string
console.log(num.toString());

// Convert a string to a number
let strNum = "42";
console.log(parseInt(strNum));
console.log(parseFloat("3.14"));

// Find the maximum and minimum of a list of numbers
console.log(Math.max(10, 5, 8, 30));
console.log(Math.min(10, 5, 8, 30));

// Get a random number between 0 and 1
console.log(Math.random());

// Generate a random whole number between 1 and 10
console.log(Math.floor(Math.random() * 10) + 1);

/*
Object Methods
Objects can have their own methods as well.
*/

let person = {
    name: "Alice",
    age: 25,
    greet: function() {
      return "Hello, my name is " + this.name;
    }
};
  
// Call the method
console.log(person.greet());
  
// Get keys and values of an object
console.log(Object.keys(person));
console.log(Object.values(person));

/*
Date Methods
The Date object allows us to work with dates and times.
*/

let now = new Date();

console.log(now.toDateString());
console.log(now.toLocaleTimeString());

// Get the current year, month, day
console.log(now.getFullYear());
console.log(now.getMonth() + 1);
console.log(now.getDate());

/*
Why Are Methods Important?
Methods make it easier to work with strings, numbers, arrays, objects, and dates. More importantly, they allow us to interact with HTML elements.

For example:
*/

document.getElementById("myButton").addEventListener("click", function() {
    alert("Button clicked!");
});
