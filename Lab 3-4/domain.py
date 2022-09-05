def create_expense (apartment, etype, amount): 
    '''
    Creats an expense.
    params:
        - apartment: number of apartment, positive integer
        - etype: a string indicating one of the categories: water, heating, electricity, gas, other
        - amount: positive intege
    output:
        - expense returned if success
        - None returned if failure
    '''
    if apartment.isdigit()!=True or int(apartment)<0 or amount.isdigit()!=True or int(amount)<0 or etype not in etypeList:
        return None
    the_list=[int(apartment),etype,int(amount)]
    return the_list

def get_apartment(expense):
    return int(expense[0])
def get_etype(expense):
    return expense[1]
def get_amount(expense):
    return int(expense[2])

'''
^^^^ getters; Each function returns a different element of the expense.
params: - expense: the expense
output: -> get_apartment : expense[0] = number of the apartment
        -> get_etype : expense[1] = the type of the expense
        -> get_amount : expense[2] = the amount of the expense
        
'''
def set_apartment(expense,apartment):
    expense[0]=apartment
def set_etype(expense,etype):
    expense[1]=etype
def set_amount(expense,amount):
    expense[2]=amount
'''
^^^^ setters; Each function sets a value for a different element of the expense.
params: - expense: the expense
        - apartment/etype/amount: the value to be set        
'''

def init_expenses():
    '''
Initializes the list of expenses.
output: - the list of expenses, having 12 items
'''
    res=[]
    res.append(create_expense('5','gas','200'))
    res.append(create_expense('25','water','150'))
    res.append(create_expense('25','other','150'))
    res.append(create_expense('20','gas','100'))
    res.append(create_expense('10','water','150'))
    res.append(create_expense('10','gas','150'))
    res.append(create_expense('15','heating','200'))
    res.append(create_expense('16','water','150'))
    res.append(create_expense('17','electricity','150'))
    res.append(create_expense('36','electricity','100'))
    res.append(create_expense('21','water','150'))
    res.append(create_expense('9','other','150'))
    return res

def init_etype():
    '''
Initializes the etype list.
output: the list of types for expenses, including the pre-defined categories: water, heating, electricity, gas, other
'''
    etypeList=[]
    etypeList.append('water')
    etypeList.append('heating')
    etypeList.append('electricity')
    etypeList.append('gas')
    etypeList.append('other')
    return etypeList

etypeList=init_etype()

def test_create_expense():  
    '''
    Tests the create_expense function.
    output: -quiet if success
    -message if fail
    '''
    assert create_expense('25','water', '200')!=None
    assert create_expense('-1','gas','200')==None 
    assert create_expense('25','abc','200')==None 
    assert create_expense('25','other','-600')==None

test_create_expense()