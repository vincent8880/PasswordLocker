import pyperclip
class Credentials:
    '''
    class that creates new accounts and authenticates the user
    '''
    users list =[]
    def _init_(self, identify,user_name,password):
        self.identify = identify
        self.user_name = user_name
        self.password = password
    def create_account(self):
        '''
        function to create a new account
        '''
        Crendentials.users_list.append(self)
    @class method
    def authenticate_account(cls, name, key):
        '''
        method for authenticating created account
        '''
        for user in cls.users_list:
             if user.user_name == name and user.password == key:
                
                return user
            return 0
class UsersData:
    '''
    class that contains user and password data for the user
    '''
    data list =[]
    def _init_(self,ident,data_id,website,web_key,name):
           self.ident = ident
           self.data_id = data_id
           self.website = website
           self.web_key = web_key
           self.name = name

    

    