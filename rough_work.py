class Rough:

    def __init__(self,name):
        self.name=name
        self.fullname="Seh"

class Student:

    def __init__(self,name, mark1, mark2, mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def marks_avg(self):
        return round(int(self.mark1)+int(self.mark2)+int(self.mark3)/3,0)



o1=Rough("aka")
print(o1.name,o1.fullname)
o2=Student("aka",2,3,4)
print(o2.marks_avg())