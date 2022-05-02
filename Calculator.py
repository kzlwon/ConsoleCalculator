def subtract():
        return num1 - num2

def multiply():
    return num1 * num2

def devide():
    return num1 / num2

def add():
    return num1 + num2

while True:
    try:
        num1 = int(input('Choose a number: '))
        num2 = int(input('Choose another number: '))
        choice = input('Type >> +, -, *, /: ')
        if choice == '-':
            print(subtract())
        elif choice == '*':
            print(multiply())
        elif choice == '/':
            print(devide())
        elif choice == '+':
            print(add())
        else:
            print("Type error")
            continue
    except:
        print("enter integer")
    finally:
        again = input("Again? (y/n): ")
        if again == 'n':
            break
        elif again == 'y':
            print("\n")
            continue
        else:
            print("answer error")
            break
