from ui import*
def print_menu():
    print ("Menu:")
    print("     1.Add expenses.")
    print("     2.Remove expenses.")
    print("     3.Replace the amount of an expense.")
    print("     4.Show expenses.")
    print("     5.Obtain different characteristics of the expenses.")
    print("     6.Filter expenses.")
    print("     7.Undo.")
    print("     8.Exit.")

def start():
    expenseList=init_expenses()
    history=[]
    undoable_commandsDict={'1':add_chosen,'2':remove_chosen,'3':replace_chosen,'6':filter_chosen,'7':undo_ui}
    non_undoable_commandsDict={'4':show_chosen,'5':characteristics_chosen}
    while True:
        print_menu()
        choice=input("Your command: >")
        if choice in undoable_commandsDict:
            undoable_commandsDict[choice](expenseList,history)
        elif choice in non_undoable_commandsDict:
            non_undoable_commandsDict[choice](expenseList)
        elif choice=='8':
            return
        else:
            print("Bad command")

def add_chosen(expenseList,history):
    apartment=input("Enter the apartment: >")
    etype=input("Enter the type: >")
    amount=input("Enter the amount: >")
    params=[]
    params.append(apartment)
    params.append(etype)
    params.append(amount)
    add_expense_ui(expenseList,params,history)

def remove_chosen(expenseList,history):
    params=[]
    print ("        1.Remove all the expenses for one apartment.")
    print ("        2.Remove all the expenses for more apartments.")
    print ("        3.Remove all the expenses having a given type.")
    choice=input("Your command: >")
    if choice=='1':
        apartment=input("Enter the apartment: >")
        params.append(apartment)
    elif choice=='2':
        apartment1=input("Enter the first apartment: >")
        apartment2=input("Enter the second apartment: >")
        params.append(apartment1)
        params.append('to')
        params.append(apartment2)
    elif choice=='3':
        etype=input("Enter the type: >")
        params.append(etype)
    else:
        print("Bad command!")
    if len(params)!=0:
        remove_expense_ui(expenseList,params,history)

def replace_chosen(expenseList,history):
    params=[]
    apartment=input("Enter the apartment: >")
    etype=input("Enter the type: >")
    amount=input("Enter the amount: >")
    params.append(apartment)
    params.append(etype)
    params.append('with')
    params.append(amount)
    replace_expense_ui(expenseList,params,history)

def filter_chosen(expenseList,history):
    params=[]
    print("     1.Filter by type.")
    print("     2.Filter by amount.")
    choice=input("Your command: >")
    if choice=='1':
        etype=input("Enter the type: >")
        params.append(etype)
    elif choice=='2':
        amount=input("Enter the amount: >")
        params.append(amount)
    else:
        print("Bad command!")
    if len(params)!=0:
        filter_expenses_ui(expenseList,params,history)

def show_chosen(expenseList):
    print ("        1.Show all the expenses.")
    print ("        2.Show all the expenses of a given apartment.")
    print ("        3.Show all the expenses having the total amount </>/= than a given amount.")
    params=[]
    choice=input("Your command: >")
    if choice=='1':
        show_expenseList_ui(expenseList,params)
    elif choice=='2':
        apartment=input("Enter the apartment: >")
        params.append(apartment)
        show_expenseList_ui(expenseList,params)
    elif choice=='3':
        symbol=input("Enter the symbol for the relation(>/</=): > ")
        amount=input("Enter the amount: >")
        params.append(symbol)
        params.append(amount)
        show_expenseList_ui(expenseList,params)
    else:
        print ("Bad command!")
    
def characteristics_chosen(expenseList):
    print("     1.Show the total amount of the expenses having a given type.")
    print("     2.Show the maximum amount per each expense type for a given apartment.")
    print("     3.Show the list of apartments sorted ascending by total amount of expenses.")
    print("     4.Show the total amount of expenses for each type, sorted ascending by amount of money.")
    params=[]
    choice=input("Your command: >")
    if choice=='1':
        etype=input("Enter the type: >")
        params.append(etype)
        sum_by_type_ui(expenseList,params)
    elif choice=='2':
        apartment=input("Enter the apartment: >")
        params.append(apartment)
        max_for_apartment_ui(expenseList,params)
    elif choice=='3':
        params.append('apartment')
        sort_ui(expenseList,params)
    elif choice=='4':
        params.append('type')
        sort_ui(expenseList,params)
    else:
        print ("Bad command!")

