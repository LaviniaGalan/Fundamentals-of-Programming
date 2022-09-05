from Exceptions import*
class Person:
    def __init__(self,personID,name,phoneNo):
        self._personID=personID
        self._name=name
        self._phoneNo=phoneNo
    @property
    def personID(self):
        return self._personID
    @property
    def name(self):
        return self._name
    @property
    def phoneNo(self):
        return self._phoneNo

    @name.setter
    def name(self,value):
        self._name=value

    @phoneNo.setter
    def phoneNo(self,value):
            self._phoneNo=value

    def __str__(self):
        return (str(self.personID)+' '+str(self.name)+' '+str(self.phoneNo))
        