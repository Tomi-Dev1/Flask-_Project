document.addEventListener("DOMContentLoaded", function () {
    console.log("game.js loaded! ✅"); // Debugging line
// This makes sure the code runs only after the web page has fully loaded.
// The console.log("game.js loaded! ✅"); is for debugging (checking if the script works).

    let balloon = document.getElementById("balloon");
// Looks for an HTML element with the id "balloon".
// Stores it in the variable balloon so we can use it later.
    if (balloon) {
        console.log("Balloon button found! 🎈"); // Debugging line
// Checks if the balloon was found on the page.
// If yes, it moves on to the next part of the code.
// If no, it shows an error message (console.error("Balloon button not found! ❌");).
        balloon.addEventListener("click", function () {
            console.log("Balloon clicked! 💥"); // Debugging line
            balloon.style.display = "none"; // Hides the balloon
            alert("Boom! 🎈 You popped the balloon!");
        });
// Listens for a click on the balloon.
// When clicked, it:
// Logs "Balloon clicked! 💥" in the console (for debugging).
// Hides the balloon using balloon.style.display = "none";.
// Shows an alert message: "Boom! 🎈 You popped the balloon!".        
    } else {
        console.error("Balloon button not found! ❌");
    }
});

