def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("CLI Calculator")

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Pick 1-5: ")
    

    if choice == '5':
        print("Bye!")
        break

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    if choice == '1':
        answer = add(num1, num2)
        print("Answer:", answer)
    elif choice == '2':
        answer = subtract(num1, num2)
        print("Answer:", answer)
    elif choice == '3':
        answer = multiply(num1, num2)
        print("Answer:", answer)
    elif choice == '4':
        answer = divide(num1, num2)
        print("Answer:", answer)
    else:
        print("Wrong choice!")