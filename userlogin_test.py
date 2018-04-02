import unittest  # Importing the unittest module

from userlogin import Userlogin


class TestContact(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_userlogin = Userlogin("Dodie","si7k998yu") #create contact object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_userlogin.name, "Dodie")
        self.assertEqual(self.new_userlogin.password, "si7k998yu")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Userlogin.userlogin_list = []

    def test_save_multiple_userlogin(self):
            '''
            test_save_multiple_login to check if multiple users can be saved
            '''
            self.new_userlogin.save_userlogin()
            test_userlogin = Userlogin("Jane Driver", "tyhfui78!Y")  # new user
            test_userlogin.save_userlogin()
            self.assertEqual(len(Userlogin.userlogin_list), 2)

    def test_save_userlogin(self):
        '''
        test_save_userlogin test case to test if the userlogin object is saved into
         the userlogin list
        '''
        self.new_userlogin.save_userlogin()  # saving the new userlogin details
        self.assertEqual(len(Userlogin.userlogin_list), 1)

    

if __name__ == '__main__':
  unittest.main()
