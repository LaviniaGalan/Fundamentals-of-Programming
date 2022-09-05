from domain import*
import copy
def find_expense_by_apartment (expenseList,start,stop):
    '''
    Finds all the expenses for apartments whose numbers are in [start,stop].
    params: - expenseList: the list of expenses
            - start: lower bound (e.g.: for command "remove 5", start = 5 // for command "remove 5 to 10", start = 5)
            - stop: upper bound (e.g.: for command "remove 5", stop = 5 // for command "remove 5 to 10", stop=10)
    output: -res: the list of all the expenses of apartments with the requested numbers.
    '''
    res=[]
    for i in expenseList:
        if get_apartment(i) in range (int(start),int(stop)+1):
            res.append(i)
    return res

def find_expense_by_type (expenseList,etype):
    '''
    Finds all the expenses for the requested type.
    params: -expenseList: the list of expenses
            -etype: the requested type
    output: -res: the list of all the expenses for the requested type.
    '''
    res=[]
    for i in expenseList:
        if get_etype(i)==etype:
            res.append(i)
    return res 

def add_expense(expenseList,params,history):  
    '''
    Add an expense to the list.
    params: - expenseList: the list of expenses
            - params: the list of the elements which form an expense
            - history: a history list, used for undo
    output: - None if success 
            - Error if failure 
    '''
    if len(params)!=3:
        raise ValueError ("Bad command for add!")
    apartment=params[0]
    amount=params[2]
    e=create_expense(apartment, params[1], amount)
    if e!=None:
        history.append(expenseList[:])
        expenseList.append(e)
    else:
        raise ValueError ("Could not create expense!")

def remove_expense(expenseList,params,history):
    '''
    Analyses the input and removes the requested expense.
    params: - expenseList: the list of expenses
            - params: the expenses to remove
            - history: a history list, used for undo
    output: - None if success.
            - Error if fail.
            '''
    if len(params)==1 and params[0] in etypeList:
        res=remove_expense_by_type(expenseList,params[0],history)
    elif len(params)==1 and params[0].isdigit()==True:
        res=remove_expense_by_apartment(expenseList,params[0],params[0],history)
    elif len(params)==3  and params[0].isdigit()==True and params[1]=='to' and params[2].isdigit()==True and int(params[0])<int(params[2]):
        res=remove_expense_by_apartment(expenseList,params[0],params[2],history)
    else:
        raise ValueError ("Bad command for remove!")

def remove_expense_by_type(expenseList,etype,history):
    '''
    Removes all the expenses for 'etype' from all apartments.
    params: - expenseList: the list of the expenses
            - etype: the required type
            - history: a history list, used for undo
    output: - None if success
            - Error if fail
    '''
    res1=find_expense_by_type(expenseList,etype)
    if len(res1)==0:
        raise ValueError("There aren't any expenses for this type.")
    else:
        history.append(expenseList[:])
        for i in res1:
            expenseList.remove(i)
    

def remove_expense_by_apartment(expenseList,start,stop,history):
    '''
    Removes all the expenses of the required apartments.
    params: - expenseList: the list of the expenses
            - start: lower bound (the same as start in find_expense_by_apartment)
            - stop: upper bound (the same as stop in find_expense_by apartment)
            - history: a history list, used for undo
    output: - None if success
            - Error if fail
    '''
    res1=find_expense_by_apartment(expenseList,start,stop)
    if len(res1)==0:
        raise ValueError("There aren't any expenses for this/these apartment/s.")
    else:
        history.append(expenseList[:])
        for i in res1:
            expenseList.remove(i)
        return None

def replace_expense(expenseList,params,history):
    '''
    Analyses the input and replaces an expense from the list.
    params: - expenseList: the list of expenses
            - apartment: the number of the apartment
            - etype: the type of the expense
            - newamount: the new amount of the expense
    output: - None if succes, Error if fail
'''
    if len(params)==4 and params[0].isdigit()==True and params[1] in etypeList and params[2]=='with' and params[3].isdigit()==True:
        res1=find_expense_by_apartment(expenseList, params[0],params[0])
        res2=find_expense_by_type(expenseList,params[1])
        res=[]
        for i in res1:
            if i in res2:
                res=i
                break
        if len(res)==0:
            raise ValueError("Non-existent expense.")
        else:
            cop=copy.deepcopy(expenseList)
            history.append(cop[:])
            idx=expenseList.index(res)
            set_amount(expenseList[idx],int(params[3]))
    else:
        raise ValueError("Bad command for replace!")

def calculate_general_total_amount (genList):
    '''
    Calculates the total amount for the expenses in a general list.
    params: - genList: a general list of expenses
    output: - total: the total amount for expenses in genList
    '''
    total=0
    for i in genList:
        total=total+int(get_amount(i))
    return total

def calculate_total_amount_by_apartment (expenseList,apartment):
    '''
    Calculates the total amount of expenses for one given apartment.
    params: - expenseList: the list of expenses
            - apartment: the apartment to calculate the total amount for
    output: - total returned
'''
    res=find_expense_by_apartment(expenseList,apartment,apartment)
    if len(res)!=0:
        return calculate_general_total_amount(res)

def calculate_total_amount_by_type (expenseList,etype):
    '''
    Calculates the total amount of expenses for a given type.
    params: - expenseList: the list of expenses
            - etype: the type to calculate the total amount for
    output: - total returned
    '''
    res=find_expense_by_type(expenseList,etype)
    return calculate_general_total_amount(res)

def sum_by_type (expenseList,params):
    '''
    Analyses the input and calculates the total amount for a given type (sum <type>).
    params: - expenseList: the list of expenses
            - params: the type introduced as input
    output: - the total amount for the given apartment if success
            - Error if fail
    '''
    if len(params)==1 and params[0] in etypeList:
        res=find_expense_by_type(expenseList,params[0])
        if len(res)!=0:
            return calculate_general_total_amount(res)
        else:
            raise ValueError ("There aren't any expenses for this type.")
    else:
        raise ValueError("Bad command for sum!")

def calculate_max_for_apartment(resList,apartment):
    '''
    Calculates the maximum amount for each type for a given apartment.
    params: - resList: the list containing all the expenses for the given apartment
            - apartment: the number of the requested apartment
    output: - list_of_maximums: the list of the maximum amount for each type
    '''
    list_of_maximums=[]
    for i in range(len(etypeList)):
        maxim=0
        for elem in resList:
            if get_etype(elem)==etypeList[i]:
                if int(get_amount(elem))>maxim:
                    maxim=get_amount(elem)
        list_of_maximums.append(maxim)
    return list_of_maximums
    
def max_for_apartment(expenseList,params):
    '''
    Analyses the input and calculates the maximum amount for each type for a given apartment.
    params: - expenseList: the list of expenses
            - params: the apartment introduced in input
    output: - the list of maximum amounts if succes
            - Error if fail
    '''
    if len(params)==1 and params[0].isdigit()==True:
        res=find_expense_by_apartment(expenseList,int(params[0]),int(params[0]))
        if len(res)==0:
            raise ValueError ("There aren't any expenses for this apartment!")
        else:
            return calculate_max_for_apartment(res,params[0])
    else:
        raise ValueError("Bad command for max!")

def remove_duplicates_in_list(genList):
    '''
    Removes the duplicates from a list.
    params: - genList - the list to modify
    output: - return the list without duplicates
    '''
    finalList=[]
    for i in genList:
        if i not in finalList:
            finalList.append(i)
    return finalList

def sort_ascending_by_amount(genList):
    '''
    Sorts a general list of amounts for apartments, ascending by the value of the amount.
    params: - genList: the list to sort
    output: - the sorted list
    '''
    for i in range(0,len(genList)-1):
        for j in range (i+1,len(genList)):
            if int(genList[i][1])>int(genList[j][1]):
                aux=genList[i]
                genList[i]=genList[j]
                genList[j]=aux
    return genList

def sort_apartments(expenseList):
    '''
    Sorts apartments ascending by the total amount of expenses.
    params: - expenseList: the list of expenses
    output: - the sorted list of total amount for each apartment
    '''
    list_of_total_amounts=[]
    for elem in expenseList:
        apartment=get_apartment(elem)
        list_of_total_amounts.append([apartment,calculate_total_amount_by_apartment(expenseList,apartment)])
    list_of_total_amounts=remove_duplicates_in_list(list_of_total_amounts)
    list_of_total_amounts=sort_ascending_by_amount(list_of_total_amounts)
    return list_of_total_amounts
    
def sort_type(expenseList):
    '''
    Sorts the types ascending by the total amount of expenses.
    params: - expenseList: the list of expenses
    output: - the sorted list of total amount per each type
    '''
    list_of_total_amounts=[]
    for elem in etypeList:
        total=calculate_total_amount_by_type(expenseList,elem)
        list_of_total_amounts.append([elem,total])
    list_of_total_amounts=sort_ascending_by_amount(list_of_total_amounts)
    return list_of_total_amounts

def lower_than_inequality(x,y):
    return int(x)<int(y)
def greater_than_inequality(x,y):
    return int(x)>int(y)
def equality(x,y):
    return int(x)==int(y)

def filter_expenses(expenseList,params,history):
    '''
    Analyses the input and filters expenses.
    params: - expenseList: the list of expenses
            - params: the element to filter by, introduced as input
            - history: a history list, used for undo
    output: - None if succes
            - Error if fail
    '''
    if len(params)==1 and params[0] in etypeList:
        history.append(expenseList[:])
        res=filter_expenses_by_type(expenseList,params[0],history)
    elif len(params)==1 and params[0].isdigit()==True:
        history.append(expenseList[:])
        res=filter_expenses_by_amount(expenseList,params[0],history) 
    else:
        raise ValueError ("Bad command for filter!")

def general_filter(expenseList, resList):
    i=0
    while i<len(expenseList):
        element=expenseList[i]
        if element not in resList:
            expenseList.remove(element)
        else:
            i=i+1

def filter_expenses_by_type(expenseList, etype,history):
    '''
    Filters expenses by the type.
    params: - expenseList: the list of expenses
            - etype: the type to filter expenses by
            - history: a history list, used for undo
    output: - Error if fail
            - None if success
    '''
    res=find_expense_by_type(expenseList,etype)
    if len(res)==0:
        raise ValueError("There aren't any expenses for this type.")
    else:
        history.append(expenseList[:])
        general_filter(expenseList,res)

def find_expenses_by_smaller_amount(expenseList,amount):
    res=[]
    for i in expenseList:
        if get_amount(i)<int(amount):
            res.append(i)
    return res

def filter_expenses_by_amount(expenseList,amount,history):
    '''
    Filters expenses by the amount.
    params: - expenseList: the list of expenses
            - amount: the amount to filter expenses by
            - history: a history list, used for undo
    output: - Error if fail
            - None if success
    '''
    res=find_expenses_by_smaller_amount(expenseList,amount)
    if len(res)==0:
        raise ValueError("There aren't any expenses with a smaller amount than the introduced value.")
    else:
        history.append(expenseList[:])
        general_filter(expenseList,res)
    
def undo(expenseList,history):
    '''
    Undos the last operation that modified program data.
    params: - expenseList: the list of expenses
            - history: the history of all program data
    output: - None if success
            - Error if fail
    '''
    if len(history)==0:
        raise ValueError("No more undos.")
    expenseList.clear()
    expenseList.extend(history.pop()) 



################################## TESTS ##################################

    
def test_add_expense():
    '''
    Tests the add_expense function.
    output: -quiet if success
    -message if fail
    '''
    expenseList=[]
    history=[]
    params=['21','gas', '150']
    assert add_expense(expenseList,params,history)==None
    assert len(expenseList)==1
    params=['21','other','300']
    assert add_expense(expenseList,params,history)==None
    assert len(expenseList)==2
    
def test_remove_expense_by_type():
    history=[]
    expenseList=[[5,'gas',200],[25,'water',150],[25,'other',150],[20,'gas',100]]
    assert remove_expense_by_type(expenseList,'gas',history)==None
    assert expenseList==[[25,'water',150],[25,'other',150]]
    assert remove_expense_by_type(expenseList,'water',history)==None
    assert len(expenseList)==1
    assert expenseList[0]==[25,'other',150]

def test_remove_expense_by_apartment():
    history=[]
    expenseList=[[5,'gas',200],[25,'water',150],[25,'other',150],[20,'gas',100],[10,'water',150],[10,'gas',150]]
    assert remove_expense_by_apartment(expenseList,10,10,history)==None 
    assert len(expenseList)==4
    assert expenseList[len(expenseList)-1]==[20,'gas',100]
    assert remove_expense_by_apartment(expenseList,5,20,history)==None
    assert len(expenseList)==2

def test_replace_expense():
    history=[]
    expenseList=[[5,'gas',200],[25,'water',150],[25,'other',150],[20,'gas',100],[10,'water',150],[10,'gas',150]]
    params=['10','water','with','200']
    assert replace_expense(expenseList,params,history)==None 
    assert len(expenseList)==6
    assert expenseList[4]==[10,'water',200]
    params[3]='100'
    assert replace_expense(expenseList,params,history)==None
    assert len(expenseList)==6
    assert expenseList[4]==[10,'water',100]

def test_filter_expenses_by_type():
    history=[]
    expenseList=[[5,'gas',200],[25,'water',150],[25,'other',150],[20,'gas',100],[10,'water',150],[10,'gas',150]]
    assert filter_expenses_by_type(expenseList,'gas',history)==None
    assert len(expenseList)==3        
    assert expenseList[1]==[20, 'gas' ,100]
    assert expenseList[2]==[10,'gas',150]
    
def test_filter_expenses_by_amount():
    history=[]
    expenseList=[[5,'gas',200],[25,'water',250],[25,'other',150],[20,'gas',150],[10,'water',150],[10,'gas',100]]
    assert filter_expenses_by_amount(expenseList,300,history)==None
    assert len(expenseList)==6
    assert filter_expenses_by_amount(expenseList,160,history)==None
    assert len(expenseList)==4
    assert filter_expenses_by_amount(expenseList,110,history)==None
    assert len(expenseList)==1
    assert expenseList[0]==[10,'gas',100]

def test_calculate_total_amount_by_type():
    expenseList=[[5,'gas',200],[25,'water',250],[25,'other',150],[20,'gas',100],[10,'water',150],[10,'gas',150]]
    assert calculate_total_amount_by_type(expenseList,'gas')==450
    assert type(calculate_total_amount_by_type(expenseList,'gas'))==int
    assert calculate_total_amount_by_type(expenseList,'electricity')==0
    assert calculate_total_amount_by_type(expenseList,'other')==150

test_add_expense()
test_remove_expense_by_apartment()
test_remove_expense_by_type()
test_filter_expenses_by_type()
test_filter_expenses_by_amount()
test_calculate_total_amount_by_type()


