import unittest
from PersonService import*
from Exceptions import*

class TestPersonService(unittest.TestCase):

    def test_add_person(self):
        test=PService()
        test.add_person('100','Eugenia Popescu','07222222')
        self.assertEqual(len(test._repo.get_all()),11)

        self.assertRaises(BadIDError,test.add_person,'100', 'Eugeniu Popescu', '07333333')
        self.assertEqual(len(test._repo.get_all()),11)
        self.assertEqual(str(test._repo.get_all()[len(test._repo.get_all()) - 1]),'100 Eugenia Popescu 07222222' )

        self.assertRaises(BadIDError,test.add_person,None, 'Eugeniu Popescu', '07333333')
        self.assertEqual(len(test._repo.get_all()), 11)
        self.assertRaises(BadNameError, test.add_person, '123', 'E320','071111')
        self.assertEqual(len(test._repo.get_all()), 11)
        self.assertRaises(BadPhoneNo, test.add_person,'123','Eugeniu','07abc')

    def test_remove_person_by_id(self):
        test=PService()
        ID=test._repo.get_all()[5].personID
        lenght=len(test._repo.get_all())
        self.assertEqual(test.remove_by_id(ID),None)
        self.assertEqual(len(test._repo.get_all()),lenght-1)
        self.assertRaises(NonExistentID,test.remove_by_id,ID)

    def test_update_person(self):
        test=PService()
        ID = test._repo.get_all()[5].personID
        lenght = len(test._repo.get_all())
        self.assertEqual(test.update_person(ID,'Victoria Campeanu','07899999'),None)
        self.assertEqual(str(test._repo.get_all()[5]),ID+' Victoria Campeanu 07899999')
        self.assertEqual(len(test._repo.get_all()),lenght)
        self.assertRaises(NonExistentID,test.update_person,'100','Vicky','0722')

    def test_find_people_by_name(self):
        test=PService()
        people_with_given_name=test.find_people_by_name(' ')
        self.assertEqual(test.find_people_by_name(' '),people_with_given_name)
        self.assertEqual(len(people_with_given_name),10)
        self.assertRaises(NonExistentName,test.find_people_by_name,'abcd')

    def test_find_people_by_phoneNo(self):
        test=PService()
        people_with_given_phoneNo=test.find_people_by_phoneNo('07')
        self.assertEqual(test.find_people_by_phoneNo('07'),people_with_given_phoneNo)
        self.assertEqual(len(people_with_given_phoneNo),10)
        self.assertRaises(NonExistentPhoneNo,test.find_people_by_phoneNo,'00000000000')

