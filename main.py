import calculator  as cal
def menu():
    print("1. Addition")
    print("2. Substract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        menu()
        try:
            option = int(input("Choose an operation: "))
            if option == 5:
                print("Exiting calculator. Goodbye!")
                break
            if option in [1, 2, 3, 4]:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                if option == 1:
                    print(cal.add(a, b))
                elif option == 2:
                    print(cal.sub(a, b))
                elif option == 3:
                    print(cal.multiply(a, b))
                elif option == 4:
                    print(cal.div(a, b))
            else:
                print("Invalid operation entered: please choose from 1 to 5.")
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()
