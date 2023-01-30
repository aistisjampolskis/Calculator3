import action


result = 0


while True:
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. n-root")
    print("7. Memory")
    print("8. Memory reset")
    print("9. Exit")
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")
    if choice == '1':
        num1, num2 = action.get_numbers()
        result += action.add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        num1, num2 = action.get_numbers()
        result += action.subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        num1, num2 = action.get_numbers()
        result += action.multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        num1, num2 = action.get_numbers()
        result += action.divide(num1, num2)
        print("Result:", result)
    elif choice == '5':
        num1, num2 = action.get_numbers()
        result += action.power(num1, num2)
        print("Result:", result)
    elif choice == '6':
        num1, num2 = action.get_numbers()
        result += action.n_root(num1, num2)
        print("Result:", result)
    elif choice == '7':
        print("Current Memory:", result)
    elif choice == '8':
        result = 0
        print("Memory reset:", result)
    elif choice == '9':
        break
    else:
        print("Invalid Input")
