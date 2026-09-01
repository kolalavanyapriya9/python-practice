beatles=[]
print("step 1: ",beatles)
beatles=["John Lennonm", "Paul McCartney", "George Harrison"]
print("step 2: ",beatles)
for i in range(2):
    eddit=input("enter stu sutcliffe, pete best:")
    beatles.append(eddit)
print("step 3: ",beatles)
del beatles[-1]
del beatles[-1]
print("step 4: ",beatles)
beatles.insert(0, "Ringo Starr")
print("step 5: ",beatles)
print("The Fab", len(beatles))
