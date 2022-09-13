import pickle
# import He
# from Stud_Helper.StudentCls import Student
from Stud_Helper.StudentCls import Student
 # from .StudentCls i.mport Student

def searchByName(listStud, name):
    for x in range(0,len(listStud)):
        if(listStud[x].name == name):
            listStud[x].display()
def sortByName(listStud):
    for x in range(0,len(listStud)-1):
        for y in range(x+1,len(listStud)):
            if(listStud[x].name > listStud[y].name):
             (listStud[x],listStud[y]) = (listStud[y],listStud[x])

def sortById(listStud):
    for x in range(0,len(listStud)-1):
        for y in range(x+1,len(listStud)):
            if(listStud[x].id > listStud[y].id):
             (listStud[x],listStud[y]) = (listStud[y],listStud[x])

def show(listStud):
    for x in listStud:
        x.display()

def insert():
    s = Student()
    file = open("D:\Puja\Python Study\Practice\Stud_Helper\StudentData.txt","ab+") 
    s.accept()      
    pickle.dump(s,file)
    file.close()

def displayStud():
    file = open("D:\Puja\Python Study\Practice\Stud_Helper\StudentData.txt","rb+")
    file.seek(0)
    listStud=[]
    while True:
            try:
              data =pickle.load(file)
              listStud.append(data)
            except: 
                print("Exception Occure")
                break
        # print(len(listStud))
    for x in listStud:
            x.display()
    file.close()

def search():
    file=open("D:\Puja\Python Study\Practice\Stud_Helper\StudentData.txt","rb+")
    listStud=[]
    while True:
            try:
              data=pickle.load(file)
              listStud.append(data)
            except: 
                break
    name = input("Enter a Name for Search")
    searchByName(listStud,name)
    file.close()

def sortID():
     file = open("D:\Puja\Python Study\Practice\Stud_Helper\StudentData.txt","rb+")
     listStud=[]
     while True:
            try:
              data=pickle.load(file)
              listStud.append(data)
            except: 
                break
     print("Before swapping")
     show(listStud)
     sortById(listStud)
     print("After swapping")
     show(listStud)
     file.close()

def sortName():
     file = open("D:\Puja\Python Study\Practice\Stud_Helper\StudentData.txt","rb+")
     listStud=[]
     while True:
            try:
              data=pickle.load(file)
              listStud.append(data)
            except: 
                break
     print("Before swapping")
     show(listStud)
     sortByName(listStud)
     print("After swapping")
     show(listStud)
     file.close()
 