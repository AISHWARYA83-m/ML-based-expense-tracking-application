import pandas as pd

def add_expense(date, category, amount, description):

    data = {
        "Date":[date],
        "Category":[category],
        "Amount":[amount],
        "Description":[description]
    }

    df = pd.DataFrame(data)

    df.to_csv("../data/expenses.csv", mode="a", header=False, index=False)

    print("Expense Added Successfully")


add_expense("2026-03-04","Food",300,"Dinner")