import pickle
import os
from persons.Person import *
from persons.PersonRepository import*

class PersonBinaryRepository(PRepo):
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
        f = open(self._fileName, "wb")
        for person in PRepo.get_all(self):
            pickle.dump(person, f)
        f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "rb")
            if os.path.getsize(self._fileName) > 0:
                person = pickle.load(f)
                while person!=None:
                    self.add(person)
                    try:
                        person = pickle.load(f)
                    except Exception:
                        person = None
            f.close()
        except EOFError as error:
            raise error
        except IOError as error:
            raise error
        