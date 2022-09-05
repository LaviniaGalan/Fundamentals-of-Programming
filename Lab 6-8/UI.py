from persons.PersonService import *
from activities.ActivityService import*
from controller.UndoController import*
class Console:
    def __init__(self,serv,act_serv,undo_controller):
        self._personService=serv
        self._activityService=act_serv
        self.undo_controller=undo_controller

    
    def printMainMenu(self):
        print ("        Main Menu:")
        print("1. Manage the list of people.")
        print("2. Manage the list of activities.")
        print("3. Search for people or activities.")
        print("4. Show statistics.")
        print("5. Undo.")
        print("6. Redo.")
        print("7. Exit.")

    def execute_command(self,commands,exit_command):
        command=input("Enter command: ")
        if command==exit_command:
            return
        elif command in commands:
            try:
                commands[command]()
            except Exception as error:
                print(error)
        else:
            print("Bad command!")

    def menu1(self):
        print("     1. Add a person.")
        print("     2. Remove a person by ID.")
        print("     3. Update a person by ID.")
        print("     4. Show people.")
        print("     5. Back to main menu.")
        commands={'1':self.add_person,
                  '2':self.remove_person,
                  '3':self.update_person,
                  '4':self.show_people}
        self.execute_command(commands,'5')
        

    def menu2(self):
        print("     1. Add an activity.")
        print("     2. Remove an activity.")
        print("     3. Update an activity by ID.")
        print("     4. Show activities.")
        print("     5. Back to main menu.")
        commands={
                  '1':self.add_activity,
                  '2':self.remove_activity,
                  '3':self.update_activity,
                  '4':self.show_activities
                }
        self.execute_command(commands,'5')


    def menu3(self):
        print("     1. Search for people by name.")
        print("     2. Search for people by phone number.")
        print("     3. Search for activities by date.")
        print("     4. Search for activities by time.")
        print("     5. Search for activities by description.")
        print("     6. Back to main menu.")
        commands= {
                  '1':self.find_people_by_name,
                  '2':self.find_people_by_phoneNo,
                  '3':self.find_activities_by_date,
                  '4':self.find_activities_by_time,
                  '5':self.find_activities_by_description
                }
        self.execute_command(commands,'6')

    def menu4(self):
        print("     1. Activites for a  given date.")
        print("     2. Busiest days.")
        print("     3. Activities with a given person.")
        print("     4. Back to main menu.")
        commands={
                  '1':self.stat_activities_for_given_date,
                  '2':self.stat_busiest_days,
                  '3':self.stat_activities_for_given_person
                }
        self.execute_command(commands,'4')

    def run(self):
        menues= {
                    '1': self.menu1,
                    '2': self.menu2,
                    '3': self.menu3,
                    '4': self.menu4,
                    '5': self.undo,
                    '6': self.redo
                }

        while True:
            self.printMainMenu()
            command=input("Enter command:")
            if command=='7':
                break
            elif command in menues:
                #try:
                menues[command]()
                #except ValueError as e:
                    #print(e)
            else:
                print("Bad command!")


    def add_person(self):
        personID=input("Enter an ID: ")
        name=input("Enter a name: ")
        phoneNo=input("Enter a phone number: ")
        try:
            self._personService.add_person(personID,name,phoneNo)
        except Exception as error:
            print(error)
        
    def show_people(self):
        result=self._personService.get_all()
        for i in result:
            print(i)
        
    def remove_person(self):
        personID=input("Enter the ID: ")
        try:
            op=self._personService.remove_by_id(personID)
            self._activityService.update_after_remove_person(personID,op)
        except Exception as error:
            print(error)

    def update_person(self):
        personID=input("Enter the ID of the person you want to update: ")
        new_name=input("Enter a new name: ")
        new_phoneNo=input("Enter a new phone number: ")
        try:
            self._personService.update_person(personID,new_name,new_phoneNo)
        except Exception as error:
            print(error)

    
    def show_activities(self):
        result=self._activityService.get_all()
        for i in result:
            print(i)

    def add_activity(self):
        activityID=input("Enter an ID: ")
        list_of_personIDs=[]
        print("Enter stop to stop reading person IDs.")
        personID=0
        while not personID=='stop':
            personID=input("Enter a person's ID: ")
            list_of_personIDs.append(personID)
        del list_of_personIDs[-1]
        date=input("Enter a date in format dd.mm.yyyy : ")
        time=input("Enter the time in format hh:mm : ")
        description=input("Enter a description: ")
        try:
            self._activityService.add_activity(activityID,list_of_personIDs,date,time,description)
        except Exception as error:
            print(error)

    def remove_activity(self):
        activityID=input("Enter the ID: ")
        try:
            self._activityService.remove_by_id(activityID)
        except Exception as error:
            print(error)

    def update_activity(self):
        activityID=input("Enter the ID: ")
        new_list_of_personIDs=[]
        print("Enter stop to stop reading the new person IDs.")
        personID=0
        while not personID=='stop':
            personID=input("Enter a person's ID: ")
            new_list_of_personIDs.append(personID)
        del new_list_of_personIDs[-1]
        new_date=input("Enter a new date in format dd.mm.yyyy : ")
        new_time=input("Enter the new time in format hh:mm : ")
        new_description=input("Enter a new description: ")
        #try:
        self._activityService.update_activity(activityID,new_list_of_personIDs,new_date,new_time,new_description)
        #except Exception as error:
            #print(error)

    def find_people_by_name(self):
        name=input("Enter the name: ")
        try:
            result=self._personService.find_people_by_name_2(name)
            for i in result:
                print(i)
        except Exception as error:
            print(error)

    def find_people_by_phoneNo(self):
        phoneNo=input("Enter the phone number: ")
        try:
            result=self._personService.find_people_by_phoneNo_2(phoneNo)
            for i in result:
                print(i)
        except Exception as error:
            print(error)

    def find_activities_by_date(self):
        date=input("Enter the date: ")
        try:
            result=self._activityService.find_activities_by_date(date)
            for i in result:
                print(i)
        except Exception as error:
            print(error)
    
    def find_activities_by_time(self):
        time=input("Enter the time: ")
        try:
            result=self._activityService.find_activities_by_time(time)
            for i in result:
                print(i)
        except Exception as error:
            print(error)

    def find_activities_by_description(self):
        description=input("Enter the description: ")
        try:
            result=self._activityService.find_activities_by_description(description)
            for i in result:
                print(i)
        except Exception as error:
            print(error)

    def stat_activities_for_given_date(self):
        date=input("Enter the date: ")
        try:
            result=self._activityService.stat_activities_for_given_date(date)
            for i in result:
                print(i)
        except Exception as error:
            print(error)

    def stat_busiest_days(self):
        result=self._activityService.stat_busiest_days()
        for i in result:
            print("     "+i[0].date+':')
            for j in i:
                print(j)

    def stat_activities_for_given_person(self):
        personID=input("Enter the person ID: ")
        try:
            result=self._activityService.stat_activities_for_given_person(personID)
            for i in result:
                print(i)
        except Exception as error:
            print(error)

    def undo(self):
        try:
            self.undo_controller.undo()
        
        except Exception as error:
            print (error)

    def redo(self):
        try:
            self.undo_controller.redo()
        except Exception as error:
            print (error)
       

undo_controller=UndoController()
prepo = PRepo()
arepo = ARepo()
pServ=PService(undo_controller,prepo)
aServ=AService(pServ._repo,undo_controller,arepo)
c=Console(pServ,aServ,undo_controller)
c.run()
