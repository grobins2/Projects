from getch import getch

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

def nextPrime(currentPrime):

    n = currentPrime + 1

    while not isPrime(n):
        n += 1

    return n


def start():
    print "Press N to find the next prime."
    print "Press Q to Exit."

    currentPrime = 2

    while True:
      keyPress = ord(getch())
      
      if keyPress in [110,78]: #'N' or 'n'          
        print currentPrime
        currentPrime = nextPrime(currentPrime)

      elif keyPress in [113, 81]: #'Q' or 'q'
        return False

      else:
        print "Unrecognized command. N for next prime, Q to quit."


if __name__ == "__main__":
    start()