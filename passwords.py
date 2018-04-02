import string
import random


def random_password(size=8, chars=string.ascii_letters + string.digits):
    """
    Returns a string of random characters, used in generating random passwords
    
    """
    p = ''.join(random.choice(chars) for i in range(size))

print( "p" )
    

        



    
