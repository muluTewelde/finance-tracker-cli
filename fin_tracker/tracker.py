"""
Python program that allows user to log, update, monitor, and understand their
expenses/income
"""
import finance

def main():


    done = False
    data = []

    while not done:
        choice = print_menu()
        if choice == 1:
            add_expense(data)
        elif choice == 2:
            view_expense(data)
        elif choice == 3:
            done == True
    



def print_menu():
    """
    Function that gets user input. Checks for validity.

    Params:
        None
    
    Return:
        User response as int
    """
    print("\n" + '*' * 10 + " Menu " + '*' * 10)
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    valid = False
    while not valid:
        choice = input("\nChoose an option: ")
        if not choice.isdigit():
            print("Invalid. Must be a valid int.")
        elif 0 >= int(choice) or 3 < int(choice):
            print("Invalid. Must be in the valid range.")
        else:
            return int(choice)




main()