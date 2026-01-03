from Database.Models.Person import Person ,datetime

class Member(Person):
    def __init__(self, Id, Full_name, Email, Phone,membership_id, Is_active=None, Created_at=None, Updated_at=None):

        # Public Attributes 
        super().__init__(Id, Full_name, Email, Phone, Is_active, Created_at, Updated_at)
        self.join_date = datetime.now()
        self.membership_id = membership_id

        # Protected Attributes 
        self._attendance_count = 0

        # Private Attributes 
        self.__internal_notes = None

    def __str__(self):
        return  super().__str__() + f"""
    Membership Id : {self.membership_id}
    Attendance Count : {self._attendance_count}
    Internal Notes : {self.__internal_notes}
"""