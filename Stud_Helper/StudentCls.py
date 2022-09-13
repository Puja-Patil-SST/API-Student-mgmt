class Student:
    name =""
    id=0
    age=0
    # def __init__(self,name,id,age):
        # self.name = name
        # self.id = id
        # self.age = age

    def __init__(self):
        pass

    def accept(self):
        self.name= input("enter a name")
        self.id= int(input("Enter a id"))
        self.age=int(input("Enter a Age"))
        return (self.name,self.id,self.age)

    def display(self):
        print("Name   : ", self.name)
        print("ID : ", self.id)
        print("Age : ", self.age)
