from persons.PersonRepository import*
from controller.UndoController import*
import random
class PService:
    def __init__(self,undoController,repo):
        self._repo=repo
        self.init_list_of_people()
        self._undoController = undoController

    def init_list_of_people(self):
        list_of_ids=range(1000,9999)
        list_of_first_names=['Ion','Maria','Olga','Lenuta','Mihai','Diana','Viorica','Constantin','Carmen','Alex','Dan','Stefan Jr']
        list_of_last_names=['Popescu','Enescu','Vasile','Vasilica','Lazar','Dumitrescu','Manole','Daesei','Ionescu','Ungureanu']
        list_of_phoneNo=range(1000000,9999999)
        for i in range(10):
            chosen_id=str(random.choice(list_of_ids))
            chosen_first_name=random.choice(list_of_first_names)
            chosen_last_name=random.choice(list_of_last_names)
            chosen_name=chosen_first_name+' '+chosen_last_name
            chosen_phoneNo='07'+str(random.choice(list_of_phoneNo))
            person=Person(chosen_id,chosen_name,chosen_phoneNo)
            if self.validateID(chosen_id)=='valid':
                self._repo.add(person)
            else:
                i=i-1 

    def validateID(self,value):
        '''
        Checks if a given ID is valid or not.
        params: >value = the ID to be checked
        output: >'empty' or 'invalid' if the ID is None or invalid
                >'valid' if the ID is valid
        '''
        if value==None or len(value)==0:
            return 'empty'
        result=self._repo.find_by_id(value)
        if result!=None:
            return 'invalid'
        return 'valid'

    def validate_name(self,value):
        '''
        Checks if a given name is valid or not.
        params: >value = the name to be checked
        output: >'invalid' if the name is invalid
                >'valid' if the name is valid
        '''
        if value==None or len(value)==0:
            return 'invalid'
        for i in value:
            if not(i>='a' and i<='z' or i>='A' and i<='Z' or i==' '):
                return 'invalid'
        return 'valid'

    def validate_phoneNo(self,value):
        '''
        Checks if a given phone number is valid or not.
        params: >value = the phone number to be checked
        output: >'invalid' if the phone number is invalid
                >'valid' if the phone number is valid
        '''
        if value==None or len(value)==0:
            return 'invalid'
        if value.isdigit()==False:
            return 'invalid'
        return 'valid'

    def validate_person(self,personID,name,phoneNo):
        '''
        Checks if all atributes of a person are valid.
        params: >personID = the ID of the person
                >name = the name of the person
                >phoneNo = the phone number of the person
        output: >raise Error if one of the atributes are invalid
                >'valid' if they all are valid
        '''
        if self.validateID(personID)=='empty':
            raise BadIDError("The ID can not be empty!")
        if self.validateID(personID)=='invalid':
            raise BadIDError("The ID " +personID+ " already exists!")
        if self.validate_name(name)=='invalid':
            raise BadNameError("Invalid name!") 
        if self.validate_phoneNo(phoneNo)=='invalid':
            raise BadPhoneNo("Invalid phone number!")
        return 'valid'


    def add_person(self,personID,name,phoneNo):
        '''
        Adds a person to the list.
        params: >personID = the ID of the person
                >name = the name of the person
                >phoneNo = the phone number of the person
        output: >None if success
        '''
        result=self.validate_person(personID,name,phoneNo)
        if result=='valid':
            person=Person(personID,name,phoneNo)
            self._repo.add(person)

            undo = FunctionCall(self.remove_by_id, personID)
            redo = FunctionCall(self.add_person, personID, name, phoneNo)
            op = Operation(undo, redo)
            self._undoController.recordOperation(op)
    
    def get_all(self):
        '''
        Returns all the people from the list.
        output: >the list of all people
        '''
        return self._repo.get_all()

    def remove_by_id(self,personID):
        '''
        Removes a person with a given ID.
        params: >personID = the ID of the person
        output: >raise Error if fail
                >operation if success
        '''
        element=self._repo.find_by_id(personID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of people!")
        undo = FunctionCall(self.add_person, element.personID, element.name, element.phoneNo)
        redo = FunctionCall(self.remove_by_id, personID)
        op = Operation(undo, redo)
        self._repo.remove(element)
        return op

    def update_person(self,personID,new_name,new_phoneNo):
        '''
        Updates a person by ID.
        params: >personID = the ID of the person
                >new_name = the new name of the person
                >new_phoneNo = the new phone number of the person
        output: >raise Error if fail
                >None if success
        '''
        element=self._repo.find_by_id(personID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of people!")
        if self.validate_name(new_name)=='valid' and self.validate_phoneNo(new_phoneNo)=='valid':
            new_person=Person(personID,new_name,new_phoneNo)

            undo = FunctionCall(self.update_person, personID, element.name, element.phoneNo)
            redo = FunctionCall(self.update_person, personID, new_name,new_phoneNo)
            op = Operation(undo, redo)
            self._undoController.recordOperation(op)

            self._repo.update(element,new_person)



    def find_people_by_name(self,name):
        list_of_people=self._repo.get_all()
        result=[]
        for i in list_of_people:
            if name.lower() in i.name.lower():
                result.append(i)
        if len(result)==0:
            raise NonExistentName ("No match for this name!")
        return result

    def find_people_by_phoneNo(self,phoneNo):
        list_of_people=self._repo.get_all()
        result=[]
        for i in list_of_people:
            if phoneNo in i.phoneNo:
                result.append(i)
        if len(result)==0:
            raise NonExistentPhoneNo ("No match for this phone number!")
        return result

    def accept_func_given_name(self, person, name):
        if  name.lower() in person.name.lower():
            return 1
        return 0

    def find_people_by_name_2(self, name):
        people = self._repo.get_all()
        result = filter(people, self.accept_func_given_name, name)
        if len(result)==0:
            raise NonExistentName ("No match for this name!")
        return result

    def accept_func_given_phoneNo(self, person, phoneNo):
        if phoneNo in person.phoneNo:
            return 1
        return 0

    def find_people_by_phoneNo_2(self, phoneNo):
        people = self._repo.get_all()
        result = filter(people, self.accept_func_given_phoneNo, phoneNo)
        if len(result)==0:
            raise NonExistentName ("No match for this phone number!")
        return result

