income = float(input("Enter the annual income: "))

if income<=85528:
    tax=(((18/100)*income)-557.57)
else:
    tax=(14841.57+((32/100)*(income-85528)))
    
    
if tax<0:
   tax=0.0
tax = round(tax,0)
print("The tax is:", tax, "thalers")
