#employee inheritance 
class employee():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("the employee's name is ",self.name)
        print("the employee's id number is ",self.id)
class person(employee):
    def __init__(self,name,id,salary,phone):
        self.salary=salary
        self.phone=phone
        employee.__init__(self,name,id)
    def display2(self):
        print("the employee's salary is",self.salary)
        print("the employee's phone number is",self.phone)
emp1=person("nadeen",9820,3000,"0595679023")
emp1.display()
emp1.display2()