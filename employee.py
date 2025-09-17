class person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self, name,idnumber,salary,post):
        self.salary = salary
        self.ghost = post
        person.__init__(self,name,idnumber)
obj = employee("Tareef",25,111,"fresh year")
obj.display()