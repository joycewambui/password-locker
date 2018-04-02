import time


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

def main():
    print("Welcome to The Droid Den.Please sign up if you are a human")

    name = input("Your human name: ")

    print(f"Hello {name} the human,input your password")
    print('\n')

    password =input("Your password: ")
    print('\n')

    print("Your credentials have been saved!")

    answer = input()

    




if __name__ == "__main__":
    main()


        

    
        


