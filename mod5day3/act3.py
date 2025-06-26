class family():
    def __init__(self,name,role,gender):
        self.name=name
        self.role=role
        self.gender=gender
    def display(self):
        print("this member of the family's name is",self.name)
        print("this member of the family's role is",self.role)
        print("this member of the family's gender is",self.gender)
class kids(family):
    def __init__(self,name,role,gender,age,number):
        super().__init__(name,role,gender)
        self.age=age
        self.number=number
    def display2(self):
        print("this member of the family's age is",self.age)
        print("this member of the family came at number",self.number)
kid1=kids("nadeen",'daughter','female',17,2)
kid1.display()
kid1.display2()