name=input("Enter your name:")
account_number=input("Enter your Account Number:")
balance=5000.0
transactions=[]
def check_balance():
    print("Current balance:",balance)
def deposit(amount):
    global balance
    balance=balance+amount
    transactions.append("Deposited rs."+str(amount))
    print("Amount deposited succesfully")
    print("Updated Balance:", balance)
def withdraw(amount):
    global balance
    if amount<=balance:
        balance=balance-amount
        transactions.append("Withdrawn rs."+ str(amount))
        print("Amount withdraw succesfully")
        print("REmaining balance:",balance)
    else:
        print("Insufficient balance")
while True:
    print("\n.......BANK MENU.......")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        check_balance()
    elif choice=="2":
        amount=float(input("Enter deposit amount:"))
        if amount>0:
            deposit(amount)
        else:
            print("Enter a valid amount")
    elif choice=="3":
        amount=float(input("Enter withdrawl amount:"))
        if amount>0:
            withdraw(amount)
        else:
            print("enter valid amount")
    elif choice=="4":
        print("Thank you for using our banking systam.")
        break
    else:
        print("Invalid choice.Please Try again.")