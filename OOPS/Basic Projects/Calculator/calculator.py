import argparse
import json
from operations import add,subtraction,multiplication,division

HISTORY_FILE="history.json"

def load_history():
    try:
        with open(HISTORY_FILE,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_history(history):
    with open(HISTORY_FILE,"w") as file:
        json.dump(history,file,indent=4)

def add_to_history(operation):
    history=load_history()

    history.append(operation)

    history = history[-10:]

    save_history(history)

def show_history():
    history=load_history()

    if not history:
        return "No history Found"
    
    print("Calculation History:")
    for index,item in enumerate(history,start=1):
        print(f"{index}.{item}")

def main():
    parser=argparse.ArgumentParser(
        description="CLI Calculator"
    )

    parser.add_argument("num1",type=float,nargs="?")
    parser.add_argument("num2",type=float,nargs="?")

    parser.add_argument(
        "--operation",
        choices=["add","sub","mul","div"],
        help="Choose Operation"
    )

    parser.add_argument(
        "--history",
        action="store_true",
        help="Show Calculation history"
    )

    args=parser.parse_args()

    if args.history:
      show_history()
      return

    if args.operation=="add":
        result=add(args.num1,args.num2)
        symbol="+"

    elif args.operation=="sub":
        result=subtraction(args.num1,args.num2)
        symbol="-"

    elif args.operation=="mul":
        result=multiplication(args.num1,args.num2)
        symbol="*"
    
    elif args.operation=="div":
        result=division(args.num1,args.num2)
        symbol="/"
    else:
        print("Invalid Choice")
        return
    
    print(f"Result:{result}")

    calculation=f"{args.num1} {symbol} {args.num2} = {result}"
    add_to_history(calculation)

if __name__=="__main__":
    main()