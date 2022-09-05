from domain import*
from functions import*

def add_expense_ui(expenseList,params,history):
    '''
    Adds a VALID expense to the list.
    params: expenseList - the list of expenses
            params - the list of the elements which form an expense
    output: Error message for fail
            print a message - success
    '''
    try:
        result=add_expense(expenseList,params,history)
        print("The expense was added!")
    except ValueError as v_error:
        print(v_error)

def remove_expense_ui(expenseList,params,history):
    try:
        result=remove_expense(expenseList,params,history)
        print("The expenses were removed!")
    except ValueError as v_error:
        print (v_error)
        
def replace_expense_ui(expenseList,params,history):
    try:
        replace_expense(expenseList,params,history)
        print("The amount was replaced!")
    except ValueError as verror:
        print(verror)
        
def show_expenses(expenseList):
    cnt=1
    for i in expenseList:
        print(cnt,") In apartment",get_apartment(i)," for ",get_etype(i),"the amount is ",get_amount(i),".")
        cnt=cnt+1

def show_expenseList_ui(expenseList,params):
    if params==[]:                                                                                                                                          #if the command is 'list'
        print("The entire list of expenses is: ")
        show_expenses(expenseList)
    elif len(params)==1 and params[0].isdigit()==True:                                                                  #if the command is 'list <apartment>
        res=find_expense_by_apartment (expenseList,params[0],params[0])
        if len(res)==0:
            print ( "There aren't any expenses for this apartment.")
        else:
            show_expenses(res)
    elif len(params)==2 and params[0] in ['<','>','='] and params[1].isdigit()==True:            #if the command is list  '[ < | = | > ] <amount>'
        sign_dict={'<':lower_than_inequality, '>':greater_than_inequality,'=':equality}
        result=[]
        for i in expenseList:
            total=calculate_total_amount_by_apartment (expenseList,get_apartment(i))
            if sign_dict[params[0]](total,params[1])==True:
                result.append(get_apartment(i))
        if len(result)==0:
            print("There are no apartments which satisfy the condition.")
        else:
            finalResult=remove_duplicates_in_list(result)
            print("The requested apartments are: ")
            counter=1
            for i in finalResult:
                print(counter,')',i)
                counter=counter+1
    else:                                                                                                                                                               #if the command is wrong
        print ("Bad command for list!")

def filter_expenses_ui(expenseList,params,history):
    '''
Filters the expenses, keeping only the required expenses.
params: - expenseList - the list of expenses
                - params - the type or the amount introduced by user
output: -printing Error Message if fail
                -return None if success
    '''
    
    try:
        filter_expenses(expenseList,params,history)
        print("The expenses were filtered!")
    except ValueError as verror:
        print(verror)

def sum_by_type_ui(expenseList, params):
    try:
        print(sum_by_type(expenseList,params))
    except ValueError as verror:
        print(verror)

def max_for_apartment_ui(expenseList,params):
    try:
        res=max_for_apartment(expenseList,params)
        for i in range(0,len(etypeList)):
            if res[i]!=0:
                print("The maximum amount per",etypeList[i],"is ",res[i],'.')
    except ValueError as verror:
        print(verror)
    
def sort_apartments_ui(expenseList):
    result=sort_apartments(expenseList)
    counter=1
    for i in result:
        print (counter,") ",i[0],"with a total amount of ",i[1])
        counter=counter+1
    
def sort_type_ui(expenseList):
    result=sort_type(expenseList)
    counter=1
    for i in result:
        if i[1]!=0:
            print (counter,") '",i[0],"' with a total amount of ",i[1])
            counter=counter+1

def sort_ui(expenseList,params):
    sortDict={'apartment':sort_apartments_ui,'type':sort_type_ui}
    if params[0] not in ['apartment','type']:
        raise ValueError ("Bad command for sort!")
    try:
        sortDict[params[0]](expenseList)
    except ValueError as v_error:
        print(v_error)

def undo_ui(expenseList,history):
    try:
        undo(expenseList,history)
    except ValueError as v_error:
        print(v_error)


#start()