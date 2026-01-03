from datetime import datetime
class Person:
    def __init__(self, Id, Full_name, Email, Phone, Is_active = None, Created_at =None, Updated_at= None):

        # Public Attributes
        self.id = Id 
        self.Full_name = Full_name
        self.Email = Email
        self.Phone = Phone
        self.Is_active = True

        # Protected Attributes
        self._Created_at = datetime.now()
        self._Updated_at = None
    
    def __str__(self):
        return f'''
    Id : {self.id }
    Full Name : {self.Full_name }
    Email : {self.Email}
    Phone : {self.Phone}
    Is Active :{self.Is_active}
    Created At : {self._Created_at }
    Updated at : {self._Updated_at}
    '''

    def deactivate(self): # This Method To Make Member Desactive
        self.Is_active = False
        self._Updated_at = datetime.now()

    def activate(self): # This Method To Make Member Active
        self.Is_active = True
        self._Updated_at = datetime.now()

    def update_contact(self, Email=None, Phone=None): # Method To Update Members Info
        if Email:
            self.Email = Email
        if Phone:
            self.Phone = Phone
        self._Updated_at = datetime.now()
    

