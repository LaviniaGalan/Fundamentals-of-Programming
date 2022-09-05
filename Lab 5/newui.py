from service import *
from domain import*
class newConsole:
    def __init__(self,serv):
        self._service=serv
    def run (self):
        commands_with_params={'add':self.add,'filter':self.filter_books}
        commands_without_params={'show':self.show,'undo':self.undo}
        while True:
            commands=input("     Enter commands:")
            commands=commands.split(',')
            for i in range(0,len(commands)):
                complete_command=commands[i]
                split_command=self.analyse_command(complete_command)
                command=split_command[0]
                params=split_command[1]
                if command in commands_without_params:
                    try:
                        commands_without_params[command]()
                    except ValueError as e:
                        print(e)
                elif command in commands_with_params:
                    try:
                        commands_with_params[command](params)
                    except ValueError as e:
                        print(e)
                else:
                    print("The command number "+str(i+1)+" is incorrect!")
                print('')

    def analyse_command(self,complete_command):
        complete_command=complete_command.split(' ')
        command=complete_command[0]
        params=[]
        if len(complete_command)>1:
            for j in range(1,len(complete_command)):
                params.append(complete_command[j])
        return (command,params)

    def show(self):
        for i in self._service._books:
            print(i)
            
    def undo(self):
        try:
            self._service.undo()
        except ValueError as e:
            print(e)

    def add(self,params):
        if len(params)!=3:
            raise ValueError("Invalid number of parameters for add!")
        isbn=params[0]
        author=params[1]
        title=params[2]
        book=Book(isbn,author,title)
        self._service.add(book)
    
    def filter_books(self,params):
        if len(params)!=1:
            raise ValueError("Invalid number of parameters for filter!")
        first_word=params[0]
        self._service.filter_books(first_word)
        
serv=Service()
c=newConsole(serv)
c.run()
