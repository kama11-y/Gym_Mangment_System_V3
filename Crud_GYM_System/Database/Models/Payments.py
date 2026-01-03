from datetime import date
class Payment:
    def __init__(self, Id, Member_id, Amount, Payment_date, Status, Payment_method, Transaction_ref):
        # Public Attributes
        self.Id = Id
        self.Member_id = Member_id
        self.Amount = Amount
        self.Payment_date = date.today()
        self.Status = "Pending"
        
        # Protected Attributes
        self._Payment_method = None

        # Private Attributes 
        self.__Transaction_ref = None