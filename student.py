class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname,year):   
        super().__init__(fname,lname)
        self.year = year
obj = student("Tareef","Toufique",2025)
obj.display()
print(obj.year)