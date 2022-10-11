while True:
    
    print("------------------------------")
    print("    What do you want to do    ")
    print("------------------------------")
    print("1. Show primes numbers")
    print("2. Stop the program")
    print("------------------------------")
    chose = int(input("Write your option: "))
    if chose == 1:
        final = int(input("Enter a final point to show all corresponding numbers: "))
        number = 1
        while number <= final:
            count = 1
            x = 0
            while count <= number:
                if number % count == 0:
                    x += 1
                count += 1
            if x == 2:
                print(number)

            number += 1
    elif chose == 2:
        break
    
    else:
        print("invalid option, please enter a valid one")