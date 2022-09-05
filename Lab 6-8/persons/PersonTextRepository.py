from persons.Person import *
from persons.PersonRepository import*

class PersonTextRepository(PRepo):
    def __init__(self, fileName):
        PRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        PRepo.add(self,obj)
        self._saveFile()

    def remove(self, obj):
        PRepo.remove(self,obj)
        self._saveFile()

    def update(self, obj, new_obj):
        PRepo.update(self, obj, new_obj)
        self._saveFile()
    
    def _saveFile(self):
        f = open(self._fileName, 'w')
        for person in PRepo.get_all(self):
            file_person=str(person.personID)+','+str(person.name)+','+str(person.phoneNo)+'\n'
            f.write(file_person)
        f.close()

    def _loadFile(self):
        f = open(self._fileName, "r")
        value = f.readline()
        while value:
            value = value[:-1]
            value = value.split(',')
            if len(value)==3:
                person = Person (value[0], value[1], value[2])
                self.add(person)
            value=f.readline()
        f.close()


