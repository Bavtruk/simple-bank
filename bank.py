# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = 0

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        balance = balance + int(input("How much do you want to deposite?Enter ammount:"))
        if (balance<=0):
            print("Invalid value,make a different choise")
        pass
    elif choice == '2':
        balance = balance - int(input("How much do you want to withdraw?Enter ammount:"))
        if (balance<=0):
            print("Invalid value,make a different choise")
        pass
    elif choice == '3':
        print("Your balance", balance)
        pass
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")