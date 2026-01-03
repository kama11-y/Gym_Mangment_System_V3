from Database.Models.Person import Person ,datetime

class Member(Person):
    def __init__(self, Id, Full_name, Email, Phone,Membership_id, Is_active=None, Created_at=None, Updated_at=None):
        # Public Attributes 
        super().__init__(Id, Full_name, Email, Phone, Is_active, Created_at, Updated_at)
        self.join_date = datetime.now()
        self.Membership_id = Membership_id

        # Protected Attributes 
        self._Attendance_count = 0

        # Private Attributes 
        self.__Internal_notes = None

    def __str__(self):
        return  super().__str__() + f"""
    Membership Id : {self.Membership_id}
    Attendance Count : {self._attendance_count}
    Internal Notes : {self.__Internal_notes}
    """
    def add_attendance(self): # This Method To Append Attendance
        self._Attendance_count += 1

    def change_membership(self, New_membership_id): # This Method To Change Membership_id 
        self.Membership_id = New_membership_id

    def is_regular(self): # This Method To Check How many times Member Came To Gym
        return self._Attendance_count >= 20

    
