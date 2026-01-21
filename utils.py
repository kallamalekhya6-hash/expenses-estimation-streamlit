import matplotlib.pyplot as plt

def calculate_total_expenses(expenses_dict):
    """
    Calculate total expenses from expense dictionary
    """
    return sum(expenses_dict.values())


def plot_expenses(expenses_dict):
    """
    Generate a pie chart for expense distribution
    """
    categories = list(expenses_dict.keys())
    amounts = list(expenses_dict.values())

    fig, ax = plt.subplots()
    ax.pie(
        amounts,
        labels=categories,
        autopct='%1.1f%%',
        startangle=90
    )
    ax.axis('equal')  # Makes the pie chart circular

    return fig
