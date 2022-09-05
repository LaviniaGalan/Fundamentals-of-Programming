from activities.ActivityRepository import*
from Exceptions import*
from persons.PersonRepository import*
from controller.UndoController import*
import random
import datetime
import copy
class AService:
    def __init__(self,pers_repo,undoController,act_repo):
        self._personRepo=pers_repo
        self._repo=act_repo
        self.init_list_of_activities()
        self._undoController=undoController

    def init_list_of_activities(self):
        list_of_IDs=range(1000,9999)
        list_of_personIDs=[]
        people=self._personRepo.get_all()
        max_no_of_people=len(people)
        for i in people:
            list_of_personIDs.append(i._personID)
        list_of_dates=['24.11.2019','28.11.2019','23.10.2019','10.08.2019','10.10.2020','31.12.2020','31.12.2021','04.05.2020','16.07.2020','17.05.2021','13.05.2021','26.06.2020','30.11.2020','28.02.2020','01.12.2021']
        list_of_hours=range(0,24)
        list_of_minutes=range(0,60)
        list_of_descriptions=['reading','watching movies','playing tennis','doing homework','eating','dancing','watching TV','concert','teambuilding']
        for i in range(10):
            chosen_id=str(random.choice(list_of_IDs))
            if self.validate_ID(chosen_id)=='valid':
                personIDs=self.generate_personIDs(list_of_personIDs,max_no_of_people)
                date=random.choice(list_of_dates)
                time=self.generate_valid_time(list_of_hours,list_of_minutes)
                description=random.choice(list_of_descriptions)
                try:
                    if self.validate_activity(chosen_id,personIDs,date,time,description)=='valid':
                        activity=Activity(chosen_id,personIDs,date,time,description)
                        self._repo.add(activity)
                except Exception:
                    i=i-1
                    pass
            else:
                i=i-1

    def generate_valid_time(self,list_of_hours,list_of_minutes):
        hour=str(random.choice(list_of_hours))
        minute=str(random.choice(list_of_minutes))
        time=hour+':'+minute 
        return self.formatting_time(time)

    def generate_personIDs(self,list_of_personIDs,max_no_of_people):
        personIDs=[]
        chosen_no_of_people=random.choice(range(max_no_of_people+1))
        for i in range(chosen_no_of_people+1):
            chosed_personID=random.choice(list_of_personIDs)
            if chosed_personID not in personIDs:
                personIDs.append(chosed_personID)
            else:
                i=i-1
        return personIDs


    def validate_ID(self,value):
        '''
        Validates a given ID.
        params: >value = an activity ID
        output: >'empty' if the ID is none
                >'invalid' if the ID is invalid
                >'valid' if the ID is valid
        '''
        if value==None:
            return 'empty'
        result=self._repo.find_by_id(value)
        if result!=None:
            return 'invalid'
        return 'valid'

    def formatting_date(self,value):
        '''
        Formates date in the form: dd.mm.yyyy
        params: >value = the date to be formatted
        output: the formatted date
        '''
        date=value.split('.')
        day=date[0]
        month=date[1]
        year=date[2]
        if len(month)==1:
                month='0'+month
        if len(day)==1:
            day='0'+day
        return day+'.'+month+'.'+year

    def formatting_time(self,time):
        '''
        Formates time in the form: hh:mm
        params: >value = the time to be formatted
        output: the formatted time
        '''
        time=time.split(':')
        hour=time[0]
        minute=time[1]
        if len(hour)==1:
            hour='0'+hour
        if len(minute)==1:
            minute='0'+minute
        return hour+':'+minute

    def validate_date(self,value):
        '''
        Checks if the date is valid or not.
        params: >value = the date to be checked
        output: >'invalid' if the date is not valid
                >'valid' if the date is valid
        '''
        if '.' not in value:
            return 'invalid'
        date=value.split('.')
        if len(date)!=3:
            return 'invalid'
        day=date[0]
        month=date[1]
        year=date[2]
        if day.isdigit()==False or month.isdigit()==False or year.isdigit()==False:
            return 'invalid'
        months_with_31=[1,3,5,7,8,10,12]
        if int(month) not in range(1,13):
            return 'invalid'
        elif int(month)==2 and int(year)%4==0 and int(day)>29:
            return 'invalid'
        elif int(month)==2 and not(int(year)%4==0) and int(day)>28:
            return 'invalid'
        elif int(month) not in months_with_31 and int(day)>30:
            return 'invalid'
        elif int(year) not in range(2015,2027):
            return 'invalid'
        return 'valid'
        

    def validate_personIDs(self,list_of_personIDs):
        '''
        Checks if the list of person IDs is valid or not.
        params: >list_of_personIDs = the list to be checked
        output: >the first person ID which is not in the planner if the list is not valid
                >'valid' if the list is valid
        '''
        people=self._personRepo.get_all()
        valid_personIDs=[]
        for i in people:
            valid_personIDs.append(i._personID)
        if len(list_of_personIDs) == 0:
            return None
        for i in list_of_personIDs:
            if i not in valid_personIDs:
                return i
        return 'valid'

    def validate_time(self,value):
        '''
        Checks if the time is valid or not.
        params: >value = the time to be checked
        output: >'invalid' if the time is not valid
                >'valid' if the time is valid
        '''
        if ':' not in value:
            return 'invalid'
        time=value.split(':')
        if len(time)!=2:
            return 'invalid'
        hour=time[0]
        minute=time[1]
        if hour.isdigit()==False or minute.isdigit()==False:
            return 'invalid'
        if int(hour) not in range(0,24) or int(minute) not in range(0,60):
            return 'invalid'
        return 'valid'

    def validate_activity(self,activityID,personIDs,date,time,description):
        '''
        Checks if an activity is valid or not.
        params: >activityID = the ID of the activity
                >personIDs = the list of IDs of the people taking part of the activity
                >date = the date of the activity
                >time = the time of the activity
                >description = the description of the activity
        output: >raise Error if one of the atributes of the activity is not valid
                >'valid' if all of the atributes are valid
        '''
        if self.validate_ID(activityID)=='empty':
            raise BadIDError("The ID can not be empty!")
        if self.validate_ID(activityID)=='invalid':
            raise BadIDError("This ID already exists!")
        i=self.validate_personIDs(personIDs)
        if i!='valid':
            raise NonExistentID("The ID "+i+" is not in the planner.") 
        if self.validate_date(date)=='invalid':
            raise BadDateError("Invalid date!")
        formatted_date=self.formatting_date(date)
        if self.validate_time(time)=='invalid':
            raise BadTimeError("Invalid time!")
        formatted_time=self.formatting_time(time)

        result=self.verify_overlapping_for_a_list_of_people(personIDs,formatted_date,formatted_time)
        if result!='valid':
            raise OverlapError ("The activities for "+result+" overlap!")
        return 'valid'


    def verify_overlapping_for_one_person(self,personID,date,time):
        '''
        Verifies if the activity of a person, taking place at date/time, overlaps with another activities of that person.
        params: >personID = the ID of the person
                >date = the date of activity
                >time = the time of activity
        output: >'Overlap' if they overlap
                >'valid' if not
        '''
        result=self.find_all_activities_for_a_person(personID)
        if result==[]:
            return 'valid'
        for i in result:
            if i.date==date and i.time==time:
                return  'Overlap'
        return 'valid'

    def verify_overlapping_for_a_list_of_people(self,personIDs,date,time):
        '''
        For every person in a list, verifies if the activity of a person, taking place at date/time, overlaps with another activities of that person.
        params: >personIDs = the list of IDs of the people
                >date = the date of activity
                >time = the time of activity
        output: >'Overlap' if they overlap
                >'valid' if not
        '''
        for j in personIDs:
            result=self.verify_overlapping_for_one_person(j,date,time)
            if result=='Overlap':
                return j
        return 'valid'

    def find_all_activities_for_a_person(self,personID):
        '''
        Finds all activities for a given person.
        params: >personID = the ID of the person
        output: >result = the list of activities of that person
        '''
        result=[]
        activities=self._repo.get_all()
        for activity in activities:
            for pID in activity.personID:
                if pID==personID:
                    result.append(activity)
                    break
        return result

    def get_all(self):
        '''
        Returns all the activities from the list.
        output: >the list of all activities
        '''
        return self._repo.get_all()

    def add_activity(self,activityID,list_of_personIDs,date,time,description):
        '''
        Adds an activity to the list.
        params: >activityID = the ID of the activity
                >personIDs = the list of IDs of the people taking part of the activity
                >date = the date of the activity
                >time = the time of the activity
                >description = the description of the activity
        output: >None if success
        '''
        if self.validate_activity(activityID,list_of_personIDs,date,time,description)=='valid':
            activity=Activity(activityID,list_of_personIDs,self.formatting_date(date),self.formatting_time(time),description)
            self._repo.add(activity)

            undo = FunctionCall(self.remove_by_id, activityID)
            redo = FunctionCall(self.add_activity, activityID,list_of_personIDs,date,time,description)
            op = Operation(undo, redo)
            self._undoController.recordOperation(op)

    def remove_by_id(self,activityID):
        '''
        Removes an activity with a given ID.
        params: >activityID = the ID of the activity
        output: >raise Error if fail
                >None if success
        '''
        element=self._repo.find_by_id(activityID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of activities!")

        undo = FunctionCall(self.add_activity, element.activityID,element.personID,element.date,element.time,element.description)
        redo = FunctionCall(self.remove_by_id, activityID)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        self._repo.remove(element)



    def update_activity(self,activityID,new_personIDs,new_date,new_time,new_description):
        '''
        Updates a person by ID.
        params: >activityID = the ID of the activity
                >new_personIDs = the updated list of IDs of the people taking part of the activity
                >new_date = the updated date of the activity
                >new_time = the updated time of the activity
                >new_description = the updated description of the activity
        output: >raise Error if fail
                >None if success
        '''
        element=self._repo.find_by_id(activityID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of activities!")
        if self.validate_activity_for_update(activityID,new_personIDs,new_date,new_time,new_description)=='valid':
            new_activity=Activity(activityID,new_personIDs,self.formatting_date(new_date),self.formatting_time(new_time),new_description)
            undo = FunctionCall(self.update_activity, activityID, element.personID, element.date, element.time, element.description)
            redo = FunctionCall(self.update_activity, activityID,new_personIDs,new_date,new_time,new_description)
            op = Operation(undo, redo)
            self._undoController.recordOperation(op)
            
            self._repo.update(element,new_activity)


    def validate_activity_for_update(self,activityID,personIDs,date,time,description):
        if self.validate_personIDs(personIDs)!='valid':
            raise NonExistentID("The ID "+i+" is not in the planner.") 
        if self.validate_date(date)=='invalid':
            raise BadDateError("Invalid date!")
        formatted_date=self.formatting_date(date)
        if self.validate_time(time)=='invalid':
            raise BadTimeError("Invalid time!")
        formatted_time=self.formatting_time(time)
        result=self.verify_overlapping_for_a_list_of_people_update(personIDs,formatted_date,formatted_time,activityID)
        if result!='valid':
            raise OverlapError ("The activities for "+result+" overlap!")
        return 'valid'

    def verify_overlapping_for_one_person_update(self,personID,date,time,activityID):
        result=self.find_all_activities_for_a_person(personID)
        if result==[]:
            return 'valid'
        for j in result:
            if activityID!=j.activityID and j.date==date and j.time==time:
                return  'Overlap'
        return 'valid'

    def verify_overlapping_for_a_list_of_people_update(self,personIDs,date,time,activityID):
        for j in personIDs:
            result=self.verify_overlapping_for_one_person_update(j,date,time,activityID)
            if result=='Overlap':
                return j
        return 'valid'

    def update_after_remove_person(self,removed_person_ID,op_person):
        '''
        Updates the list of activities after a person is removed.
        params: >removed_person_ID = the Id of the removed person
                >op_person = the operations of undo/redo for removing the person
        '''
        result=self.find_all_activities_for_a_person(removed_person_ID)
        if result==[]:
            self._undoController.recordOperation(op_person)
            return None
        final_operation=[]
        final_operation.append(op_person)
        for element in result:
            if len(element.personID)==1:
                undo = FunctionCall(self.add_activity, element.activityID,element.personID,element.date,element.time,element.description)
                redo = FunctionCall(self.remove_by_id, element.activityID)
                op_activity = Operation(undo, redo)
                final_operation.append(op_activity)
                self.remove_by_id(element.activityID)
            else:
                new_personIDs=copy.deepcopy(element.personID)
                new_personIDs.remove(removed_person_ID)
                new_activity=Activity(element.activityID,new_personIDs,element.date,element.time,element.description)
                undo = FunctionCall(self.update,new_activity,element)
                redo = FunctionCall(self.update,element,new_activity)
                op_activity = Operation(undo, redo)
                final_operation.append(op_activity)
                self.update(element,new_activity)
        op=CascadedOperation(final_operation)
        self._undoController.recordOperation(op)

    def update(self,element,new_activity):
        self._repo.update(element, new_activity)

    '''
    def find_activities_by_date(self,date):
        list_of_activities=self._repo.get_all()
        result=[]
        for i in list_of_activities:
            if date in i.date:
                result.append(i)
        if len(result)==0:
            raise NonExistentDate ("No match for this date!")
        return result

    def find_activities_by_time(self,time):
        list_of_activities=self._repo.get_all()
        result=[]
        for i in list_of_activities:
            if time in i.time:
                result.append(i)
        if len(result)==0:
            raise NonExistentTime ("No match for this time!")
        return result

    def find_activities_by_description(self,description):
        list_of_activities=self._repo.get_all()
        result=[]
        for i in list_of_activities:
            if description.lower() in i.description.lower():
                result.append(i)
        if len(result)==0:
            raise NonExistentDescription ("No match for this description!")
        return result
    '''
    def accept_func_given_date(self, activity, date):
        if  date in activity.date:
            return 1
        return 0

    def find_activities_by_date(self, date):
        activities = self._repo.get_all()
        result = filter(activities, self.accept_func_given_date, date)
        if len(result)==0:
            raise NonExistentName ("No match for this date!")
        return result

    def accept_func_given_time(self, activity, time):
        if  time in activity.time:
            return 1
        return 0

    def find_activities_by_time(self, time):
        activities = self._repo.get_all()
        result = filter(activities, self.accept_func_given_time, time)
        if len(result) == 0:
            raise NonExistentName("No match for this time!")
        return result

    def accept_func_given_description(self, activity, description):
        if  description in activity.description:
            return 1
        return 0

    def find_activities_by_description(self, description):
        activities = self._repo.get_all()
        result = filter(activities, self.accept_func_given_description, description)
        if len(result) == 0:
            raise NonExistentName("No match for this descriprion!")
        return result

    def stat_activities_for_given_date(self,date):
        result=[]
        result=self.find_activities_by_date(date)
        if len(result)==0:
            raise NonExistentDate ("No match for this date!")
        result=self.sort_activities_by_time(result)
        return result
        
    def sort_activities_by_time(self, list_of_activities):
        result = sort(list_of_activities, self.comp_by_time, 1)
        return result

    def comp_by_time(self, act1, act2):
        hour_1 = act1.time[0] + act1.time[1]
        minute_1 = act1.time[3] + act1.time[4]
        hour_2 = act2.time[0] + act2.time[1]
        minute_2 = act2.time[3] + act2.time[4]
        if hour_1 > hour_2 or hour_1 == hour_2 and minute_1 > minute_2:
            return 1
        elif hour_1 == hour_2 and minute_1 == minute_2:
            return 0
        else:
            return -1

    def find_upcoming_dates(self,list_of_activities):
        result=[]
        today=datetime.datetime.now()
        for i in list_of_activities:
            date=i.date.split('.')
            if date[2]>str(today.year) or date[2]==str(today.year) and date[1]>str(today.month) or date[2]==str(today.year) and date[1]==str(today.month) and date[0]>=str(today.day):
                result.append(i)
        return result


    def stat_activities_for_given_person(self,personID):
        result=[]
        list_of_activities=self._repo.get_all()
        list_of_activities=self.find_upcoming_dates(list_of_activities)
        for i in list_of_activities:
            if personID in i.personID:
                result.append(i)
        if len(result)==0:
            raise NoUpcomingActivities("No upcoming activities for this person!")
        return result


    def list_of_dates(self,list_of_activities):
        list_of_dates=[]
        for i in list_of_activities:
            if i.date not in list_of_dates:
                list_of_dates.append(i.date)
        return list_of_dates

    def stat_busiest_days(self):
        result=[]
        list_of_activities=self._repo.get_all()
        list_of_activities=self.find_upcoming_dates(list_of_activities)
        list_of_dates=self.list_of_dates(list_of_activities)
        for date in list_of_dates:
            activities_with_same_date=[]
            for i in list_of_activities:
                if i.date==date:
                    activities_with_same_date.append(i)
            result.append(activities_with_same_date)
        result=self.sort_by_no_of_activities(result)
        return result

    def comp_no_of_activities(self, date1, date2):
        if len(date1)<len(date2):
            return -1
        elif len(date1) == len(date2):
            return 0
        else:
            return 1

    def sort_by_no_of_activities(self, list_of_activities_grouped_by_date):
        result = sort(list_of_activities_grouped_by_date, self.comp_no_of_activities, -1)
        return result

