import pickle
import os
from activities.Activities import *
from activities.ActivityRepository import*

class ActivityBinaryRepository(ARepo):
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
        f = open(self._fileName, "wb")
        for activity in ARepo.get_all(self):
            pickle.dump(activity, f)
        f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "rb")
            if os.path.getsize(self._fileName) > 0:
                activity = pickle.load(f)
                while activity!=None:
                    self.add(activity)
                    try:
                        activity = pickle.load(f)
                    except Exception:
                        activity = None
            f.close()
        except EOFError as error:
            raise error
        except IOError as error:
            raise error