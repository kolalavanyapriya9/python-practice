#classes
'''class Main():             #class
    x="codegnan"   #x is class,s attribute
#creating objects
obj=Main        #assigning class main to object
obj=Main()      #treated as obj if only () included
print(obj)      # gives the adress of the object        (obj.x)    # accesing the class by including .attribute
obj.x=100       # changing x value to 100 inside the object only but not in class
print(obj.x)    #prinys new changed value  
#but if any changes done to classes then the changed obect does not get effected but only chnaged tounchanged objects
#like wise if any changes made in oject then the hange only fixed to that perticular changed object ut not effect other objects or classes
#example:
class phone():
    ringtone="bolo bolo"
lavanya=phone()
print(lavanya.ringtone)
usha=phone()
print(usha.ringtone)
usha.ringtone="chalo chalo"
print(usha.ringtone)
print(lavanya)
print(usha)

#creating method inside a class:
class phone():
    ringtone="Helo Helo"
    def notification(self):      #why pass self means path of the object is mentoned it needs tobe mentioned otherwise gets error
        print(self.ringtone)     #self. menas obj.attribute  #self is actually a reference of objects
obj=phone()
obj.ringtone="bye bye"
obj.notification()
#creating another obj 
obj2=phone()
obj2.ringtone="hi hi"
obj2.notification()

#example: bank account
'''
'''class Bank():
    balence=int(input())
    def check(self):
        print(self.balence)
    def Deposit(this,amount):          #this and self or any can that can be is just a referce to that pertiular object and objects are stored in that selfor referece
        this.balence+=amount

ac1=Bank()
ac1.Deposit(199)
ac1.check()

ac2=Bank()
print(ac2.check())     #here none is printed as its in  function call
ac2.Deposit(456)
ac2.check()
'''
#student details:
# class Student():
#     def __init__(self,name,age):
#         self.name=input()
#         self.marks=int(input())
#     def Details(ref):
#         print(ref.name,ref.marks)
#     def grade(self):
#         if self.marks>550 and self.marks<=600:
#             return f"Grade --A"
#         elif self.marks>=500 and self.marks<=500:
#             return f"Gread --B"
#     print(grade)
# std1=Student("john",435)
# std1.Details()
# std1.grade()


#---> bamk account
''' class BankAct():
    def __init__(self,name,b):
        self.name=name
        self.__balance=b
    def Info(self):
        print(self.name,self.__balance)
    def Deposit(self,amount):
        self.__balance+=amount
        print("amount success credit")
    def Withdraw(self,amount):
        self.__balance=amount
        print(self.__balance)
ac1=BankAct("balayya",500)
# ac1.Info()
# ac1.Deposit(500)
# ac1.Info()
# ac1.Withdraw(600)
ac1.__balance=0
print(ac1.__balance)==0
ac1.Info()
ac1._BankAct__BALANCE=200    #mangling
ac1.Info()
'''


#--->Inheritence:  single
'''class parent():
    def p1(self):
        print("This is parent class")
class child(parent):
    def c1(self):
        print("this is child class")
ch1=child()
ch1.c1()
ch1.p1()

print()
p=parent()
p.p1()


#multi level inheritence:
class Gparent():
    def gp1(self):
        print("this is g-parent class")
class parent(Gparent):
    def p1(self):
        print("this is parent class")
class child(parent):
    def c(self):
        print("this is child class")
obj=child()
obj.c()
obj.p1()
obj.gp1()
print()
pobj=parent()
pobj.p1()
pobj.gp1()
'''
#multiple inheritence:
'''class father():
    def f1(self):
        print("this os father class")
class mother():
    def m1(self):
        print("THis is mother class")
class child(father,mother):
    def c1(self):
        print("this is child class")

'''
#hirarchial:


#example program:
class persion():
    def __init__(self,name,email,mobile,address):
        self.name=name
        self.email=email
        self.mobile=mobile
        self.address=address
    def Info1(self):
        return self.name,self.email,self.mobile,self.address
class students(persion):
    def __init__(self,name,email,mobile,address,marks,course,graduation):
        super().__init__(name,email,mobile,address)
        self.marks=marks
        self.course=course
        self.graduation=graduation
    def Info(self):
        print(self.name,self.email,self.mobile,self.marks,self.address,self.course,self.graduation)
class Trainers(persion):
    def __init__(self,name,email,mobile,address,bank_act):
        super().__init__(name,email,mobile,address)
        self.bank_act=bank_act
    def TInfo(self):
        print(super().Info1())
        print(self.bank_act)



#polymorphism:
#poly +morphism----->many forms1.method over riding    2. method overloading    3.operator over riding
#example:method over riding
class Father:
    def F1(self):
        print("THis is mother class")
class Mother():
    def M1(self):
        print("This is mother")
class child(Father,Mother):
    def x1(self):
        print("this is child class")

c=child()
print(child.mro())              #method resolution order
#upu cssh card also mrthod over riding

#example-----> method over loading:
class Order:
    def items(self,*items):
        print(*items)
c1=Order()
c1.items("chicken","biryani","mutton")

#example----> operator overriding:

