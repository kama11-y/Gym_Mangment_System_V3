class Membership:
    def __init__(self, Id, Name, Price, Duration_days, Features,Internal_code):
        # Public Attributes
        self.Id = Id
        self.Name = Name
        self.Price = Price
        self.Duration_days = Duration_days

        # Protected Attributes
        self._feautures = []

        # Private Attributes
        self.__internal_code = None
