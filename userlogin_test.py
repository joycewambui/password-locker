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

if __name__ == '__main__':
  unittest.main()
