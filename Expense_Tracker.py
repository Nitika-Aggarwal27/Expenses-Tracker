# Making a Expense Tracker simple project using python

expenses = [] #list of all items in dictionary format.
print("Welcome! To our Expense Tracker.")

while True:
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Total amount spent")
    print("4. Exit")

    choice = int(input("Choose One Option:"))

    match choice:
        case 1:
            date = input("Enter Date of amount spend: ")
            category = input("Enter category of expenses: ")
            description = input("Enter description of items: ")
            amount = float(input("Enter amount spend: "))

            expense = {
                "date" : date,
                "category" : category,
                "description": description,
                "amount": amount
            }

            expenses.append(expense)
            print("Done! Your Expenses added.")
        case 2:
            if(len(expenses)==0):
                print("Please add something your expense :).")
            else:
                print("Here it is your all expenses.")
                count = 1
                for each in expenses:
                    print(f"expense number {count} => {each["date"]}, {each["category"]}, {each["description"]}, {each["amount"]} ")
                    count += 1
        case 3:
            total = 0
            for eachamount in expenses:
                total += eachamount["amount"]
            print("Total Amount:", total) 
        case 4:
            print("Thank You for using our Expense Tracker :).")
            break
        case _:
            print("Invalid Option.")
    