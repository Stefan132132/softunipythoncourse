def isPrime(j):
    is_prime = True
    for p in range(2, j):
        if j % p == 0:
            is_prime = False
    return is_prime
        

def main():
    firstN = int(input())
    secondN = int(input())
    thirdN = int(input())

    for i in range(2, firstN + 1, 2):
        for j in range(2, secondN + 1):
            if isPrime(j):
                for g in range(2, thirdN + 1, 2):
                    print(f"{i} {j} {g}")
            
        
        
        
main()