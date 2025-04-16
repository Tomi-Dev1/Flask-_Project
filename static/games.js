document.addEventListener("DOMContentLoaded", function () {
    console.log("game.js loaded! ✅"); // Debugging line

    let balloon = document.getElementById("balloon");

    if (balloon) {
        console.log("Balloon button found! 🎈"); // Debugging line

        // Add click event listener to pop the balloon
        balloon.addEventListener("click", popBalloon);
    } else {
        console.error("Balloon button not found! ❌");
        displayErrorMessage();
    }

    /**
     * Function to handle balloon popping
     */
    function popBalloon() {
        console.log("Balloon clicked! 💥"); // Debugging line

        // Add a "pop" animation class (defined in CSS)
        balloon.classList.add("pop-animation");

        // Wait for animation to finish before hiding the element
        setTimeout(() => {
            balloon.style.display = "none"; // Hides the balloon after animation
            alert("Boom! 🎈 You popped the balloon!");
        }, 500); // Adjust timeout to match animation duration
    }

    /**
     * Function to display an error message if the balloon is not found
     */
    function displayErrorMessage() {
        let container = document.querySelector(".container");
        if (container) {
            let errorMessage = document.createElement("p");
            errorMessage.textContent = "Oops! The balloon is missing. 🚫";
            errorMessage.style.color = "red";
            container.appendChild(errorMessage);
        }
    }
});
 // Debugging line
// This makes sure the code runs only after the web page has fully loaded.
// The console.log("game.js loaded! ✅"); is for debugging (checking if the script works).

    
// Looks for an HTML element with the id "balloon".
// Stores it in the variable balloon so we can use it later.
    
// Checks if the balloon was found on the page.
// If yes, it moves on to the next part of the code.
// If no, it shows an error message (console.error("Balloon button not found! ❌");).
     
// Listens for a click on the balloon.
// When clicked, it:
// Logs "Balloon clicked! 💥" in the console (for debugging).
// Hides the balloon using balloon.style.display = "none";.
// Shows an alert message: "Boom! 🎈 You popped the balloon!".        
 

