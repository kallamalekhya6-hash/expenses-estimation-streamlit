function estimateExpenses() {
    let income = parseFloat(document.getElementById("income").value);
    let rent = parseFloat(document.getElementById("rent").value);
    let utilities = parseFloat(document.getElementById("utilities").value);
    let food = parseFloat(document.getElementById("food").value);
    let transportation = parseFloat(document.getElementById("transportation").value);
    let entertainment = parseFloat(document.getElementById("entertainment").value);
    let misc = parseFloat(document.getElementById("misc").value);

    let totalExpenses = rent + utilities + food + transportation + entertainment + misc;
    let remaining = income - totalExpenses;

    document.getElementById("result").innerHTML = `
        Total Expenses: ₹${totalExpenses.toFixed(2)} <br>
        Remaining Balance: ₹${remaining.toFixed(2)}
    `;
}
