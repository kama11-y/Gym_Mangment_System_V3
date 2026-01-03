from datetime import datetime

class Attendance:
    def __init__(self, id, member_id):
        # Public Attibutes
        self.id = id
        self.member_id = member_id
        self.check_in = datetime.now()
        self.check_out = None
        # Protected Attributes
        self._duration_minutes = 0
    def checkout(self):
        if self.check_out is None:
            self.check_out = datetime.now()
            self._calculate_duration()
    def _calculate_duration(self):
        delta = self.check_out - self.check_in
        self._duration_minutes = int(delta.total_seconds() / 60)
    def get_duration(self):
        return self._duration_minutes


    
