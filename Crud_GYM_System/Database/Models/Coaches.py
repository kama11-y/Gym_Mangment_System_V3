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
    def get_salary(self): # This Method To Get Coach Salary
        return self._salary
    
    def update_salary(self,new_salary): # This Method To Update Coach's Salary
        if new_salary > 0:
            self._salary = new_salary

    def change_speciality(self,new_speciality): # This Method To Change Coach's Speciality
        self.speciality = new_speciality

    def apply_bunos(self,bouns): # This Method To Append Bonus To Coach
        if bouns > 0:
            self._salary += bouns