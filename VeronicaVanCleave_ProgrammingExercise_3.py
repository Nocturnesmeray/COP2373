def get_expenses():
    """
    Receives a list of monthly expenses with their costs.

    Parameters:
        None

    Variables:
        expenses (list): A list of expenses with their costs.
        expense (str): What the user paid for.
        cost (float): The amount the user paid.

    Logic:
        1. Create a list for expense and cost.
        2. Ask the user to enter their monthly expenses.
        3. Add the inputs from the message into the expenses list.

    return:
        expenses (list): A list of expenses with their costs.
    """
    expenses = []

    print(f"Enter your monthly expenses. Type done when finished.")

    #has the user input an expense and the cost of that expense
    while True:
        expense = input("Expense: ")


        if expense.lower() == "done":
            break

        cost = float(input("Cost: "))
        expenses.append([expense, cost])

    return expenses

def calculate(expenses):
    """
    Determines and shows the highest expense, lowest expense, and total expense.

    Parameters:
        expenses (list): A list of expenses with their costs.

    Variables:
        max_expense (list): The highest expense.
        min_expense (list): The lowest expense.
        total_expense (float): The total expense.

    Logic:
        1. Calculate the highest expense, lowest expense, and total expense.
        2. Show the highest expense, lowest expense, and total expense.

    Return:
        None
    """
    from functools import reduce

    max_expense = max(expenses, key=lambda x: x[1])
    min_expense = min(expenses, key=lambda x: x[1])
    total_expense = reduce(lambda total, item: total + item[1], expenses, 0)

    #shows the user the results to help the user review their expenses
    print(f"Your highest expense is: {max_expense[0]} ${max_expense[1]}.")
    print(f"Your lowest expense is: {min_expense[0]} ${min_expense[1]}")
    print(f"Your total expenses is: ${total_expense}.")

    return

if __name__ == "__main__":
    expenses = get_expenses()
    calculate(expenses)