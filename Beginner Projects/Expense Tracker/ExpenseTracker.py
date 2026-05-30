import csv
from datetime import datetime

FILE_NAME="expenses.csv"

def initilize_file():
    try:
        with open(FILE_NAME,"x",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(['Date','Category','Amount','Description'])

    except FileExistsError:
        pass

def add_expense():
    category=input("Enter the category:")
    Amount=float(input("Enter the Amount spent:"))
    description=input("Enter the description:")

    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME,"a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([date,category,Amount,description])

    print("Expense Added successfully")

def view_expense():
    try:
        with open(FILE_NAME,"r",newline="") as file:
            reader=csv.reader(file)
        
            print("----All Expenses---")

            for row in reader:
                print(row)

            print()
    except FileNotFoundError:
        print("No expense record found")

def category_summary():
    summary={}

    with open(FILE_NAME,"r",newline="") as file:
        reader=csv.DictReader(file)

        for row in reader:
            category=row["Category"]
            Amount=float(row["Amount"])

            summary[category]=summary.get(category,0)+Amount

    print("----Category Summary---")

    for category,total in summary.items():
        print(f"{category}:{total}")
    print()

def monthly_report():
    month=input("Enter the month (YYYY-MM):")

    total=0

    with open(FILE_NAME,"r",newline="") as file:
        reader=csv.DictReader(file)

        print("---Montly Report----")

        for row in reader:
            if row["Date"].startswith(month):
                print(
                    f"{row['Date']} | {row['Category']} | ₹{row['Amount']} | {row['Description']}"
                )
                total +=float(row['Amount'])
            
    print(f"Total Spending: {total}")

def clear_all_data():
    with open(FILE_NAME,"w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["Data","Category","Amount","Description"])

        print("All expenses are cleared")


def main():
    initilize_file()

    while True:
        print("===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Report")
        print("5.Clear Data")
        print("6. Exit")
        
        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            print("Enter a number")
            continue

        if choice==1:
            add_expense()

        elif choice==2:
            view_expense()

        elif choice==3:
            category_summary()

        elif choice==4:
            monthly_report()

        elif choice==5:
            clear_all_data()
        elif choice==6:
            break
        else:
            print("Invalid choice")
        

if __name__=="__main__":
    main()


    