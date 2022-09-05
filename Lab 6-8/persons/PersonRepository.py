from persons.Person import*
from collection import*
class PRepo:
    def __init__(self):
        self._container = Collection()

    def add(self,element):
        self._container.append(element)

    def find_by_id(self,personID):
        for i in self._container:
            if i.personID == personID:
                return i
        return None

    def remove(self,element):
        self._container.remove(element)

    def get_all(self):
        return self._container._data

    def update(self,element,new_person):
        idx = self._container.index(element)
        self._container[idx] = new_person

    def no_of_people(self):
        return len(self._container)

        
