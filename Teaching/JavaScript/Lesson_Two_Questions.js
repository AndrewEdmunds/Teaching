// ==========================================
// JavaScript Lesson 2: Functions & Loops - Questions
// ==========================================

// ✅ Multiple Choice Questions
// ---------------------------

// 1️⃣ What keyword is used to define a function in JavaScript?
//    A) def
//    B) function
//    C) define
//    D) func

// Answer: __B__


// 2️⃣ What will the following code print?
function greet(name) {
    return "Hello, " + name + "!";
}
console.log(greet("Alice"));

//    A) Hello, Alice!
//    B) greet("Alice")
//    C) undefined
//    D) "Hello, Alice!"

// Answer: __A__


// 3️⃣ What will the following loop do?
for (let i = 0; i < 3; i++) {
    console.log("Looping...");
}

//    A) Print "Looping..." three times
//    B) Print "Looping..." four times
//    C) Print "Looping..." indefinitely
//    D) Nothing, there's an error

// Answer: __A__


// 4️⃣ How do you call a function named `sayHello`?
//    A) sayHello;
//    B) sayHello();
//    C) call sayHello();
//    D) execute sayHello();

// Answer: __B__


// ✅ Open-Ended Questions
// -----------------------

// 5️⃣ What is the difference between returning a value in a function and using console.log() inside the function?

//Return is used to save the values for later use and console.log is for seeing a functions effects.

// 6️⃣ Write a function called `multiply` that takes two parameters and returns their product.
//work:
function multiply(s, d) {
    return s * d
}
let Quest = multiply(9, 11)
console.log(Quest)

// 7️⃣ Modify the following loop to count **from 1 to 10** instead of from 0 to 4.
for (let i = 0; i < 5; i++) {
    console.log(i);
}
//work:
for (let i = 1; i < 11; i++) {
    console.log(i);
}

// 8️⃣ Given the array below, write a loop that prints each fruit.
let fruits = ["Apple", "Banana", "Cherry"];
//work:
for (let FruitLoops = 0; FruitLoops < 3; FruitLoops++) {
    console.log("I'd like a " + fruits[FruitLoops]);
}

// 9️⃣ What will the following loop print?
let count = 3;
while (count > 0) {
    console.log("Counting down: " + count);
    count--;
}
//work:
// Counting down: 3
// Counting down: 2
// Counting down: 1

// Explain what happens when count reaches 0.
//work:
// Nothing... the process ends.

// 🔟 Challenge Question:
//     Write a function `isEven` that takes a number and returns `true` if it's even, `false` otherwise.
//     Then, use a loop to print all even numbers from 1 to 10 using your function.

function isEven(L) {
    if (L % 2 == 0) {
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