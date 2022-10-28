""" START PROGRAM OF GENERATE PRIME NUMBER """

""" ASK UP TO WHICH NUMBER TO DISPLAY THE PROGRAM """
final = int(input("Enter final number: "))


""" DEVELOP """
def generateNumbers(final):
    """ GENERATE LIST AND COUNT, TO ADD THE PRIMES AND NON-PRIMES """
    noPrimos= []
    primos=[1]
    count=2

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

def showNumbersPrimes(primos):
    for x in range(len(primos)):
        print(primos[x])

