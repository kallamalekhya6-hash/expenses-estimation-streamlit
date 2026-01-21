import matplotlib.pyplot as plt

def plot_expenses(expenses):
    """
    Plot a pie chart of expenses.
    Only show categories with >0 values to avoid overlapping labels.
    Returns None if total expenses = 0.
    """
    # Filter out zero values
    filtered_expenses = {k: v for k, v in expenses.items() if v > 0}
    total = sum(filtered_expenses.values())

    if total == 0:
        return None  # Don't plot chart if no expenses

    fig, ax = plt.subplots()
    ax.pie(
        filtered_expenses.values(),
        labels=filtered_expenses.keys(),
        autopct='%1.1f%%',
        startangle=90
    )
    ax.axis('equal')
    plt.title("Expenses Distribution")
    return fig



