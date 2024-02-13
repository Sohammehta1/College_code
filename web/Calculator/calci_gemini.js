// Function to clear the display
function clearDisplay() {
    currentNumber = "";
    operator = null;
    updateDisplay();
}

// Function to calculate the square of a number
function squareNumber() {
    if (currentNumber !== "") {
        try {
            let number = parseFloat(currentNumber);
            currentNumber = (number * number).toString();
            updateDisplay();
        } catch (error) {
            alert("Invalid input for square operation.");
        }
    }
}

// Function to format and display the number
function updateDisplay() {
    document.getElementById("display").value = currentNumber.replace(/\B(?=(\d{3})+(?!\d))/g, ","); // Add comma separators (optional)
}

// Handle division by zero case
function checkDivisionByZero() {
    if (operator === "/" && currentNumber === "0") {
        alert("Division by zero is not allowed!");
        clearDisplay();
        return true;
    }
    return false;
}

// Handle errors during calculation
function handleErrors() {
    try {
        const result = eval(currentNumber);
        currentNumber = result.toString();
        updateDisplay();
    } catch (error) {
        alert("Invalid calculation. Please check your input.");
        clearDisplay();
    }
}

// Main event listener for button clicks
window.addEventListener("click", function(event) {
    const target = event.target;

    if (target.tagName === "BUTTON") {
        if (target.textContent.match(/^[0-9]+$/)) {
            appendNumber(target.textContent);
        } else if (target.textContent === ".") {
            // Prevent multiple decimal points
            if (!currentNumber.includes(".")) {
                appendNumber(".");
            }
        } else if (target.textContent === "+" || target.textContent === "-" ||
                   target.textContent === "*" || target.textContent === "/") {
            appendOperator(target.textContent);
        } else if (target.textContent === "C") {
            clearDisplay();
        } else if (target.textContent === "x²") {
            squareNumber();
        } else if (target.textContent === "=") {
            if (checkDivisionByZero()) {
                return;
            }
            calculate();
            handleErrors();
        }
    }
});
