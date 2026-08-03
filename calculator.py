history = []

print("===== Calculator =====")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
print("6. View History")

def add():
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    result = num1 + num2
    print("Result:", result)
    history.append(f"{num1} + {num2} {result}")

def subtract():
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    result = num1 - num2
    print("Result:", result)
    history.append(result)

def multiply():
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    result = num1 * num2
    print("Result:", result)
    history.append(result)

def divide():
    try:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        result = num1 / num2
        print("Result:", result)
    except:
        print("Cannot divide by zero!")
    history.append(result)

def view_history():
    print("History:")

    for item in history:
        print(item)

while True:
    choice = input("Choose an option: ")
    print("You selected:", choice)

    if choice == "1":
        print("You chose addition")
        add()

    elif choice == "2":
        print("You chose subtraction")
        subtract()

    elif choice == "3":
        print("You chose multiplication")
        multiply()

    elif choice == "4":
        print("You chose division")
        divide()

    elif choice == "5":
        print("Goodbye!")
        break

    elif choice == "6":
        view_history()

    else:
        print("Invalid option!")