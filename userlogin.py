class Userlogin:
    
    '''
    Class that generates new instances of username information 
    '''

    def __init__(self, name, password):
        self.name = name
        self.password = password

    userlogin_list = []

    def save_userlogin(self):

        Userlogin.userlogin_list.append(self)
        

    
        


