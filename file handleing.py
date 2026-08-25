#create file
#file=open("morning.txt",mode="x")  #mode  'x'  is used to create a file
file=open("morning.txt",mode="w")  #mode  'w'  is ised to write a file
'''
file.write("hello") #changes the text from morning to hello [write()]
print("success")  #after changing the file or modifying it gets print success
file.close() #we need to close the file to see the change that we mde
'''
#write mode
'''l=["hello\n", "how are you\n", "where are you\n"]    #create list
file.writelines(l)  #writelines() deals with the writing listed values
print(file.tell()) # tell() gives the curser position after writing the file 
file.write("python")  
print("success")
t=print(file.tell())
print(file.seek(t))
print(file.write("now"))
file.close()
'''
#drawback of write() is the data gwts overrid if new data is writing


#read mode:   file should be exist bedfore reading
'''file=open("me.text",mode="r")    #reading mode or to read  
print(file.read())       #
print(file.readline())   #
content=file.readlines() #
for i in content:
    print(i)
'''
#write+
'''
f=open("just.txt","w+")
f.read()
f.write("hello, how are you")
f.write("i am fine")
print("success")
f.close()
f.open("just.txt","w+")
f.write("completed")
print("success")
f.close()

#read+
doc=open("just.txt","r+")
print(doc.read())
doc.write("I Love Python")
print(doc.read())
doc.close()
'''
#append mode
'''doc=open("j.text","a")
doc.write("adding info ")
#doc.read() (not possible)
print("success")
doc.close()
'''

#append+
#with is used in the place so we need not to use close............
# item=input("Item ordered: ")
# price=Int(input())
# with open ("bill.txt","a+") as file:
#     file.write(f"\n{item:20}  {price:>10}\n")
#     file.write(f"{price:>32}")
#     print("completed")

