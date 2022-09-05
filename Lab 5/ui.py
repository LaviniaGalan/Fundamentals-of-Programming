from service import *
from domain import*
class Console:
    def __init__(self,serv):
        self._service=serv
        
    def printMenu(self):
        print("1. Add a book.")
        print("2. Show books.")
        print("3. Filter books.")
        print("4. Undo.")
        print("5. Exit.")
    
    def run (self):
        commands={'1':self.add,
                  '2':self.show,
                  '3':self.filter_books,
                  '4':self.undo}
        while True:
            self.printMenu()
            command=input("     Enter command:")
            if command=='5':
                break
            elif command in commands:
                try:
                    commands[command]()
                except ValueError as e:
                    print(e)
            else:
                print("Bad command!")

    def add(self):
        isbn=input("Introduce ISBN: ")
        author=input("Introduce author: ")
        title=input("Introduce title: ")
        book=Book(isbn,author,title)
        self._service.add(book)
        
    def show(self):
        for i in self._service._books:
            print(i)
    
    def filter_books(self):
        first_word=input("Introduce the first word: ")
        self._service.filter_books(first_word)

    def undo(self):
        try:
            self._service.undo()
        except ValueError as e:
            print(e)

serv=Service()
c=Console(serv)
c.run()
