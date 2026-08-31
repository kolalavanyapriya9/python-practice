#classes
class Main():             #class
    x="codegnan"   #x is class,s attribute
#creating objects
obj=Main        #assigning class main to object
obj=Main()      #treated as obj if only () included
print(obj)      # gives the adress of the object         
print(obj.x)    # accesing the class by including .attribute
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
class Bank():
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
class Student():
    def __init__(self,name,age):
        self.name=input()
        self.marks=int(input())
    def Details(ref):
        print(ref.name,ref.marks)
    def grade(self):
        if self.marks>550 and self.marks<=600:
            return f"Grade --A"
        elif self.marks>=500 and self.marks<=500:
            return f"Gread --B"
    print(grade)
std1=Student("john",435)
std1.Details()
std1.grade()