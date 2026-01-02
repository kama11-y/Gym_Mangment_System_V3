class Member():
    def __inti__(self, id, full_name, age, gender, phone, email, join_date, membership_id, is_active):
        if isinstance(full_name,str):
            self.id = id 
            self.full_name = full_name 
            self.age = age
            self.gender = gender 
            self.phone = phone 
            self.email = email
            self.join_date = join_date
            self.membership_id = membership_id
            self.is_active = is_active