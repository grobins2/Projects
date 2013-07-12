def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+2,2):
            if n % i == 0:
                return False
        return True

def findPrimeFactors(n):
    primeFactors = [i for i in range(n) if isPrime(i) and n % i==0]
    print("The prime factors of {0} are {1}").format(n, primeFactors)

if __name__ == "__main__":
    n = int(raw_input("Enter number: "))
    findPrimeFactors(n)