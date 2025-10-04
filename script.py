balance=1000
print(" Welcome to the ATM\n your balance is",balance)
print(" 1.Check Balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n ")
option=int(input("Choose an option:"))
while option!=4:
    if option==1:
        print("Check Balance:your balance is",balance)
    elif option==2:
        deposit=int(input("Enter amount to deposit:"))
        balance=balance+deposit
        print("Deposit successful. New balance =",balance)
    elif option==3:
        withdrow=int(input("Enter amount to withdraw:"))
        if balance<withdrow:
            print("Insufficient funds!")
        else:
             balance=balance-withdrow
             print("Withdrawal successful. New balance =",balance)
    option=int(input("Choose an option:"))
if option==4:
    print("Goodbye!")