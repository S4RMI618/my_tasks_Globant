""" START PROGRAM OF GENERATE PRIME NUMBER """

count = 0

def generatePrimes(n):
    global count
    primos = []
    noPrimos = []
    for i in range(2, n + 1):
        count += 1
        if i not in noPrimos:
            primos.append(i)
            for j in range(i * i, n + 1, i):
                count += 1
                noPrimos.append(j)
    return primos


print(generatePrimes(200))
print(count)

