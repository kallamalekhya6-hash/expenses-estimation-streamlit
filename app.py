import streamlit as st
from utils import plot_expenses

st.set_page_config(page_title="Expenses Estimation", layout="centered")

st.title("Expenses Estimation App")

# Collect user input
income = st.number_input("Enter your total income:", min_value=0, value=0)

expenses = {}
expenses["Rent"] = st.number_input("Rent:", min_value=0, value=0)
expenses["Utilities"] = st.number_input("Utilities:", min_value=0, value=0)
expenses["Food"] = st.number_input("Food:", min_value=0, value=0)
expenses["Transportation"] = st.number_input("Transportation:", min_value=0, value=0)
expenses["Entertainment"] = st.number_input("Entertainment:", min_value=0, value=0)
expenses["Miscellaneous"] = st.number_input("Miscellaneous:", min_value=0, value=0)

if st.button("Estimate Expenses"):
    # Ensure no NaN or None values
    expenses = {k: (0 if v is None else v) for k, v in expenses.items()}

    # Calculate total expenses
    total_expense = sum(expenses.values())
    remaining_income = income - total_expense
    st.write(f"### Total Expenses: {total_expense}")
    st.write(f"### Remaining Income: {remaining_income}")
    # Only show pie chart if there are actual expenses
    fig = plot_expenses(expenses)
    if fig:  
        # plot_expenses returns None if total expenses are 0
        st.pyplot(fig)
    else:
        st.info("No expenses entered yet. Pie chart will appear when expenses > 0.")

st.write("\n---\n")
st.write("App by: **Alekhya Buthukuri**")

