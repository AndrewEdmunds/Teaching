// =====================================
// 🏆 JavaScript and HTML Interaction 🏆
// =====================================

// Now that you've learned the basics of JavaScript, we can move on to the fun part. let's see how it works with HTML! 
// JavaScript can be used to change text, handle user input, and modify page styles dynamically. 

// =======================================
// ✅ 1. Changing Text with JavaScript ✅
// =======================================
// In HTML, elements can have an `id` that allows JavaScript to select and modify them.
// Example: Open an HTML file and add this:

/*
<!DOCTYPE html>
<html lang="en">
<head>
    <title>JS & HTML Example</title>
</head>
<body>
    <h1 id="greeting">Hello, World!</h1>
    <button onclick="changeText()">Click Me</button>

    <script src="script.js"></script>
</body>
</html>
*/

// In your script.js file, write this function:
function changeText() {
    document.getElementById("greeting").textContent = "You clicked the button!";
}

// 👉 When the button is clicked, the text changes!

// ========================================
// ✅ 2. Getting User Input and Using It ✅
// ========================================
// JavaScript can take input from an HTML form and use it dynamically.
// Example: Add this to an HTML file:

/*
<!DOCTYPE html>
<html lang="en">
<head>
    <title>JS Input Example</title>
</head>
<body>

    <label for="nameInput">Enter your name:</label>
    <input type="text" id="nameInput">
    <button onclick="sayHello()">Greet</button>

    <h2 id="output"></h2>

    <script src="script.js"></script>
</body>
</html>
*/

// In script.js, write:
function sayHello() {
    let name = document.getElementById("nameInput").value; // Get input value
    document.getElementById("output").textContent = "Hello, " + name + "!";
}

// ✅ Try entering your name and clicking the button!

// =======================================
// ✅ 3. Changing Page Styles Dynamically ✅
// =======================================
// JavaScript can modify CSS properties like colors and font sizes.
// Example: Add this to an HTML file:

/*
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Change Background</title>
</head>
<body>

    <button onclick="changeColor()">Change Background</button>

    <script src="script.js"></script>
</body>
</html>
*/

// In script.js, write:
function changeColor() {
    document.body.style.backgroundColor = "lightblue"; // Change the background color
}

// ✅ Try clicking the button to see the effect!

// =======================================
// 🎯 CHALLENGES: Practice What You Learned!
// =======================================
// 1️⃣ Modify Text Dynamically:
//    - Create an HTML page where users can enter their **favorite color** and display a message like:
//      `"Your favorite color is Blue!"`

// 2️⃣ Interactive Button:
//    - Make a button that **hides/shows** text when clicked. (Hint: Use `style.display`)

// 3️⃣ CSS Styling with JavaScript:
//    - Add a button that changes the **text color** of a paragraph when clicked. (Hint: Use `style.color`)

// 🚀 Once you've completed these exercises, you'll be ready for more advanced web interactions!
