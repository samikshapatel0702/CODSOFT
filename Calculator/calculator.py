while True:
    print("\n" + "="*30)
    print("      SIMPLE CALCULATOR")
    print("="*30)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Thank you for using Calculator!")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            print("Result =", result)

        elif choice == "2":
            result = num1 - num2
            print("Result =", result)

        elif choice == "3":
            result = num1 * num2
            print("Result =", result)

        elif choice == "4":
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result =", result)

        elif choice == "5":
            result = num1 ** num2
            print("Result =", result)

        elif choice == "6":
            result = num1 % num2
            print("Result =", result)

    else:
        print("Invalid choice! Please select between 1 and 7.")