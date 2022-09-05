from activities.Activities import *
from activities.ActivityRepository import*

class ActivityTextRepository(ARepo):
    def __init__(self, fileName):
        ARepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        ARepo.add(self,obj)
        self._saveFile()

    def remove(self, obj):
        ARepo.remove(self,obj)
        self._saveFile()

    def update(self, obj, new_obj):
        ARepo.update(self, obj, new_obj)
        self._saveFile()

    def _saveFile(self):
        f = open(self._fileName, 'w')
        for activity in ARepo.get_all(self):
            file_activity=str(activity.activityID)+',['
            for personID in activity.personID:
                file_activity = file_activity+str(personID)+';'
            file_activity = file_activity[:-1]
            file_activity = file_activity+'],'+str(activity.date)+','+str(activity.time)+','+str(activity.description)+'\n'
            f.write(file_activity)
        f.close()

    def _loadFile(self):
        f = open(self._fileName)
        value = f.readline()
        while value:
            value = value[:-1]
            value = value.split(',')
            if len(value)==5:
                list_of_personIDs = []
                value[1] = value[1][1:]
                value[1] = value[1][:-1]
                value[1] = value[1].split(';')
                for  personID in value[1]:
                    list_of_personIDs.append(personID)
                activity = Activity (value[0], list_of_personIDs, value[2], value[3], value[4])
                self.add(activity)
            value=f.readline()
        f.close()
