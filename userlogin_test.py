import unittest  # Importing the unittest module

from userlogin import Userlogin


class TestContact(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
    self.new_userlogin = Userlogin("Dodie","si7k998yu") #create contact object
