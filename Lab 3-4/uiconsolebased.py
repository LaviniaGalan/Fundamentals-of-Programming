from ui import*
def readCommand():     
    '''
    Reads user's command
    output:
        tuple(command word, list of parameters)
    '''
    cmd=input("command: ")
    idx=cmd.find(' ')
    if idx==-1:
        return (cmd,[])
    command=cmd[:idx]
    params=cmd[idx+1:]
    params=params.split(' ')
    return (command,params)


def start():
    expenseList=init_expenses()
    history=[]
    undoable_commandsDict={'add':add_expense_ui,'remove':remove_expense_ui,'replace':replace_expense_ui,'filter':filter_expenses_ui}
    non_undoable_commandsDict={'list':show_expenseList_ui,'sum':sum_by_type_ui,'max':max_for_apartment_ui,'sort':sort_ui}
    print (expenseList)
    while True:
        command=readCommand()
        cmd=command[0]
        params=command[1]
        if cmd=='exit':
            break
        elif cmd in undoable_commandsDict:
            undoable_commandsDict[cmd](expenseList,params,history)
        elif cmd in non_undoable_commandsDict:
            non_undoable_commandsDict[cmd](expenseList,params)
        elif cmd=='undo':
            undo_ui(expenseList,history)
        else:
            print("Bad command")

