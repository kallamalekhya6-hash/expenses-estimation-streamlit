import streamlit as st
from utils import calculate_total_expenses, plot_expenses

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Expenses Estimation", layout="centered")

# -----------------------------
# Title
# -----------------------------
st.title("💰 Expenses Estimation Tool")
st.write("Enter your income and monthly expenses below:")

# -----------------------------
# Income Section
# -----------------------------
st.header("Income")
income = st.number_input("Total Income", min_value=0.0, value=50000.0)

# -----------------------------
# Expenses Section
# -----------------------------
st.header("Expenses")

rent = st.number_input("Rent", min_value=0.0, value=0.0)
utilities = st.number_input("Utilities", min_value=0.0, value=0.0)
food = st.number_input("Food", min_value=0.0, value=0.0)
transportation = st.number_input("Transportation", min_value=0.0, value=0.0)
entertainment = st.number_input("Entertainment", min_value=0.0, value=0.0)
miscellaneous = st.number_input("Miscellaneous", min_value=0.0, value=0.0)

expenses = {
    "Rent": rent,
    "Utilities": utilities,
    "Food": food,
    "Transportation": transportation,
    "Entertainment": entertainment,
    "Miscellaneous": miscellaneous
}

# -----------------------------
# Calculate Button
# -----------------------------
if st.button("Estimate Expenses"):
    total_expenses = calculate_total_expenses(expenses)
    remaining_balance = income - total_expenses

    st.success(f"✅ Total Expenses: ₹{total_expenses:.2f}")
    st.info(f"💰 Remaining Balance: ₹{remaining_balance:.2f}")

    st.subheader("Expense Distribution")
    fig = plot_expenses(expenses)
    st.pyplot(fig)

# -----------------------------
# Footer / Author
# -----------------------------
st.markdown("---")
st.markdown(
    """
    <p style="text-align: center; color: gray; font-size: 14px;">
        © 2026 | Developed by <b>  Kallam Alekhya</b> | Expenses Estimation Project
    </p>
    """,
    unsafe_allow_html=True
)
