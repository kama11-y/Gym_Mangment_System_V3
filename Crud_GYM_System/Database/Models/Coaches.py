from Database.Models.Person import Person
from datetime import date

class Coach(Person):
    def __init__(self, Id, Full_name, Email, Phone,speciality,salary, Is_active=None, Created_at=None, Updated_at=None):

        # Public Attributes 
        super().__init__(Id, Full_name, Email, Phone, Is_active, Created_at, Updated_at)
        self.speciality = speciality
        self.hire_date = date.today()

        # Protected Attributes 
        self._salary = salary

        # Private Attributes
        self.__Bank_account = None 
    def __str__(self):
        return super().__str__() + f"""
    Speciality : {self.speciality}
    Hire Date : {self.hire_date}
    Salary : {self._salary}
    Bank Account : {self.__Bank_account}
"""