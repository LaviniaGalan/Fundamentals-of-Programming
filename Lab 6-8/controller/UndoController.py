import copy
class UndoController:
    def __init__(self):
        #history of the program's undoable operations
        self._history = []
        #Keep the position  in the undo/redo list
        self._index=0
        #True if we are during an undo/redo operation
        self._duringUndo = False

    def recordOperation(self, operation):
        '''
            Record an operation in the history for undo/redo.
            params: operation - the operation that was carried out
        '''
        if self._duringUndo == True:
            return
        if self._index!=len(self._history):
            new_history=[]
            new_history=self._history[:self._index]
            self._history=new_history
            self._history.append(operation)
            self._index = len(self._history)
        else:
            self._history.append(operation)
            self._index += 1
        

    def undo(self):
        if self._index == 0:
            raise ValueError ("No more undos!")
        self._duringUndo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndo = False

    def redo(self):
        if self._index == len(self._history):
            raise ValueError ("No more redos!")
        self._duringUndo = True
        self._history[self._index].redo()
        self._index += 1
        self._duringUndo = False
'''
1. Remember what we need to do for undo/redo
(remember = what functions to call and with which parameters)

2. Remember the order in which operations were made
(remember = keep a list of prorgam operations)

3. Carry out the operations when user requests undo(),redo()
(call the right functions with right parameters)
'''
    #1. Keep a reference to a function and its params
    #We use the command design pattern
#either undo or redo (a simple one, not cascade)
class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._params = parameters
        
    def call(self):
        self._function(*self._params)          #without * => tuple of parameters as a single parameter!!!

    def __call__(self):
        self.call()

class Operation:
    '''
    Store the function reference and params for both undo and redo.
    '''
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction
    def undo(self):
        self._undo()    #self._undo.call()
    def redo(self):
        self._redo()
    
'''
UndoController.undo() calls CascadeOperation.undo() which calls Operation.undo() for each operation which calls UndoFunction.call()
which calls: 
    clientController.delete
    carController.create
    ...
'''

class CascadedOperation:
    '''
    Store the function reference and params for both undo and redo.
    '''
    def __init__(self, operations):
        self._oper = operations

    def undo(self):
        for o in self._oper:
            o.undo()

    def redo(self):
        for o in self._oper:
            o.redo()




