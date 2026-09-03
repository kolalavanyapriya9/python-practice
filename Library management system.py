class Library:
    def __init__(self):
        self.Book={}
        self.Student={}
        self.Employee={}
    def Add_book(self,obj):
        if obj.b_id not in self.Book:
            self.Book[obj.b_id]=obj
            print("success")
        else:
            print("id already exists")
    def View_books(self):
        if len(self.Book.values())!=0:
            for i in self.Book.values():
                print(i.b_id,i.name,i.author,i.copies)
        else:
            print("no nooks")
    def Add_std(self,std):
        if std.s_id not in self.Student:
            self.Student[std.s_id]=std
            print("student successfully added")
        else:
            print("id already exists")
    def View_std(self):
        for i in self.Student.values():
            print(i.s_id,i.name,i.email)
    def Create_Act(self,emp):
        if emp.e_id in self.Employee:
            print(f"{emp.e_name} alreay exists")
            return
        else:
            self.Employee[emp.e_id]=emp
            print(f"{emp.e_name} creates successfully")
    
        
class Book():
    def __init__(self,b_id,name,author,copies):
        self.b_id=b_id
        self.name=name
        self.author=author
        self.copies=copies
class Student():
    def __init__(self,name,s_id,email):
        self.name=name
        self.s_id=s_id
        self.email=email
class Employee():
    def __init__(self,e_id,e_name):
        self.e_id=e_id
        self.e_name=e_name


l=Library()
while True:
    print("1.add_books\n2.view_books\n3.add_students\n4.view_Students\n5.create account")
    n=int(input())
    if n==1:
        b_id=int(input("b_id:"))
        name=input("book name:")
        author=input("author name:")
        copies=int(input("no of copies:"))
        b=Book(b_id,name,author,copies)
        l.Add_book(b)
    elif n==2:
        l.View_books()
    elif n==3:
        name=input("student name:")
        s_id=int(input("student id:"))
        email=input("email:")
        s=Student(name,s_id,email)
        l.Add_std(s)
    elif n==4:
        l.View_std()
    elif n==5:
        e_id=int(input("employee id:"))
        e_name=input("employee name:")
        e=Employee(e_id,e_name)
        l.Create_Act(e)