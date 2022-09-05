from activities.Activities import*
from collection import*

class ARepo:
    def __init__(self):
        self._container = Collection()

    def add(self,element):
        self._container.append(element)

    def find_by_id(self,activityID):
        for i in self._container:
            if i.activityID==activityID:
                return i
        return None

    def remove(self,element):
        self._container.remove(element)

    def get_all(self):
        return self._container

    def update(self,element,new_activity):
        idx=self._container.index(element)
        self._container[idx]=new_activity

