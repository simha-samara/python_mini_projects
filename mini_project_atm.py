print("\n****** ATM ******")
print("1. check_balance")
print("2. deposit")
print("3. withdraw")
print("4. Exit")

balance=10000

def check_balance():
    print(f"your available balance is RS{balance}")

def deposit():
    global balance
    amount = float(int(input("enter amount to deposit: RS")))
    if amount <= 0:
        print("amount is greater than zero.")
    else:
        balance += amount
        print(f"RS{amount}deposited sucessfully.")


def withdraw ():
    global balance
    amount = float(int(input("enter amount to deposit: RS")))
    if amount <= 0:
        print("amount is greater than zero.")

    elif amount > balance:
        print("insufficent funds.")

    else:
        balance -= amount
        print(f"RS(amount) withdraw sucessfully.")

choice = input("enter choice from (1-4): ")
if choice=="1":
    check_balance()

elif choice=="2":
    deposit()

elif choice=="3":
    withdraw()

elif choice=="4":
    print("thankyou for using the atm.")

else:
    print("invalid choice:pls select (1-4).")