def isPrime(j):
    is_prime = True
    for p in range(2, j):
        if j % p == 0:
            is_prime = False
    return is_prime

def main():
    first_two = int(input())
    second_two = int(input())
    diff1 = int(input())
    diff2 = int(input())

    for i in range(first_two, first_two + diff1 + 1):
        if isPrime(i):
            for j in range(second_two, second_two + diff2 + 1):
                if isPrime(j):
                    print(i * 100 + j)
    
    
main()