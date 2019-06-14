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
def authenticate(username,passkey):
    '''
    Function responsible for signing in
    '''
    return Credentials.authenticate_account(username,passkey)

def my_new_data(user_id,data_id,website,web_key,name):
    '''
    Function that creates new data for storing password
    '''
    new_data = UsersData(user_id,data_id,website,web_key,name)
    return new_data

