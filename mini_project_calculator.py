#Sample Calculator

print("\n****** Sample Calculator ******")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

n1 = float(input("Enter first number (n1): "))
n2 = float(input("Enter second number (n2): "))

choice = input("enter choice from (1-5): ")
if choice=="1":
    print("Result: ",add(n1, n2))

elif choice=="2":
    print("Result: ", subtract(n1, n2))

elif choice=="3":
    print("Result: ", multiply(n1, n2))

elif choice=="4":
    print("Result: ",  divide(n1, n2))

elif choice=="5": 
    print("Exit")

else:
    print("Invalid Choice")