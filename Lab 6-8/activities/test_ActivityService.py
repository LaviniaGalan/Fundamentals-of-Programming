import unittest
from ActivityService import*
from PersonService import*
from Exceptions import*

class TestPersonService(unittest.TestCase):

    def test_add_activity(self):
        pServ = PService()
        test=AService(pServ._repo)
        activity=test.get_all()[5]
        self.assertEqual(test.add_activity('100',activity.personID,'2.7.2026','12:40','singing'),None)
        self.assertRaises(BadIDError,test.add_activity,'100',activity.personID,'2.8.2026','12:40','football')
        self.assertRaises(NonExistentID,test.add_activity,'101','11111','2.8.2026','12:40','football')
        self.assertRaises(BadDateError,test.add_activity,'101',activity.personID,'28.2026','12:40','football')
        self.assertRaises(BadTimeError,test.add_activity,'101',activity.personID,'2.8.2026','12:90','football')

    def test_remove_by_id(self):
        pServ = PService()
        test = AService(pServ._repo)
        activity = test.get_all()[5]
        self.assertEqual(test.remove_by_id(activity.activityID),None)
        self.assertEqual(len(test.get_all()),9)
        self.assertRaises(NonExistentID,test.remove_by_id,activity.activityID)
        self.assertEqual(len(test.get_all()), 9)

    def test_update_activity(self):
        pServ = PService()
        test = AService(pServ._repo)
        activity1 = test.get_all()[5]
        activity2 = test.get_all()[3]
        self.assertEqual(test.update_activity(activity1.activityID,[activity1.personID[0]],activity1.date,activity1.time,'football'),None)
        self.assertEqual(test.get_all()[5].description,'football')
        self.assertRaises(OverlapError,test.update_activity,activity1.activityID,[activity2.personID[0]],activity2.date,activity2.time,'football')

    def test_find_activity_by_date(self):
        pServ = PService()
        test = AService(pServ._repo)
        activities_with_given_date=test.find_activities_by_date('.')
        self.assertEqual(len(activities_with_given_date),10)
        activities_with_given_date = test.find_activities_by_date('1')
        self.assertLessEqual(len(activities_with_given_date), 10)
        self.assertRaises(NonExistentDate,test.find_activities_by_date,'123')

    def test_find_activity_by_time(self):
        pServ = PService()
        test = AService(pServ._repo)
        activities_with_given_time=test.find_activities_by_time(':')
        self.assertEqual(len(activities_with_given_time),10)
        activities_with_given_time = test.find_activities_by_time('1')
        self.assertLessEqual(len(activities_with_given_time),10)
        self.assertRaises(NonExistentTime,test.find_activities_by_time,'123')

    def test_find_activities_by_description(self):
        pServ = PService()
        test = AService(pServ._repo)
        activities_with_given_description = test.find_activities_by_description('ing')
        self.assertLessEqual(len(activities_with_given_description), 10)
        self.assertRaises(NonExistentDescription, test.find_activities_by_description, '123')

