import string,random,time
from locker import Credentials,UsersData
def new_account(id,user_name,password):
    '''
    Function to creating new account
    '''
    new_user = Credentials(id,user_name,password)
    return new_user
def create_user(user):
    '''
    Function that saves the user's credentials
    '''
    user.create_account()
