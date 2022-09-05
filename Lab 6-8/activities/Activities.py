class Activity:
    def __init__(self,activityID,personID,date,time,description):
        self._activityID=activityID
        self._personID=personID
        self._date=date
        self._time=time
        self._description=description

    @property
    def activityID(self):
        return self._activityID
    @property
    def personID(self):
        return self._personID
    @property
    def date(self):
        return self._date
    @property
    def time(self):
        return self._time
    @property
    def description(self):
        return self._description

    @personID.setter
    def personID(self,value):
        self._personID=value

    @date.setter
    def date(self,value):
        self._date=value

    @time.setter
    def time(self,value):
        self._time=value

    @description.setter
    def description(self,value):
        self._description=value
    
    def __str__(self):
        return (str(self.activityID)+'  '+str(self.personID).ljust(65)+'  '+str(self.date)+'  '+str(self.time)+'  '+str(self.description))

    