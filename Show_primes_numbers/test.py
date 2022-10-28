""" START PROGRAM OF GENERATE PRIME NUMBER """
while True:
    
    print("------------------------------")
    print("    What do you want to do    ")
    print("------------------------------")
    print("1. Show primes numbers")
    print("2. Stop the program")
    print("------------------------------")

    """ ASK UP TO WHICH NUMBER TO DISPLAY THE PROGRAM """

    choose = int(input("Write your option: "))
    if choose == 1:
        final = int(input("Enter a final point to show all corresponding numbers: "))
        """ GENERATE LIST AND COUNT, TO ADD THE PRIMES AND NON-PRIMES """
        noPrimos= []
        primos=[1]
        count=2

        """ DEVELOP """
        while count <= final :
            if not(count in noPrimos):
                primos.append(count)
                for x in range(final+1):
                    if not((count * x) > final):
                        noPrimos.append(count*x)
                    else:
                        break;
            count +=1

        """ PRINT LIST OF PRIMES NUMBERS  """

        for x in range(len(primos)):
            print(primos[x])
        
        """ STOP THE PROGRAM  """
    elif choose == 2:
        break
        
        """ IF ANOTHER OPTION """
    else:
        print("invalid option, please enter a valid one")