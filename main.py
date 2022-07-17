# try and except

print("\n== Basic Math Operation ==")
print("1. Multiplication")
print("2. Division")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n> Multiplication")
        try:
            print("input first number: ")
            first_num = int(input())
            print("input second number: ")
            second_num = int(input())
            result = first_num * second_num
        except ValueError:                                  # input is not a digit
            print("\n[ invalid type input ]")
        except Exception:                                    # something wrong occurred
            print("\n[ Something wrong occurred")
        else:
            print("The result: ", result )

    elif choice == '2':
        print("\n> Division")
        try:
            print("input first number: ")
            first_num = int(input())
            print("input second number: ")
            second_num = int(input())
            result = first_num / second_num
        except ZeroDivisionError:
            print("\n[ Cannot divide by zero ]")
        except ValueError:
            print("\n[ Invalid type input ]")
        except Exception:
            print("\n[ Something wrong occur ]")
        else:
            print("The result: ", result)

    else:
        print("\n[ Invalid choice ]")

    print("\n== Basic Math Operation ==")
    print("1. Multiplication")
    print("2. Division")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")



