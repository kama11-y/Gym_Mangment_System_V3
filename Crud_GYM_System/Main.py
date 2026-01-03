from Database.Models import Members,Coaches,Person,Attendance
import time 

m = Members.Member(11,'kamal','kamal@gmail.com','1234567890',1)
c = Coaches.Coach(11,'ali','ali@gmail.com','1234567890','Gym',3500)
a = Attendance.Attendance(12,11)

print (a.check_in)
time.sleep(4500)
print (a.checkout())
print (a._duration_minutes)