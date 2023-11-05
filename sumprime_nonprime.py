command_n = input()
sum_prime = 0
non_sum_prime = 0
while command_n != "stop":
    current_number = int(command_n)
    isPrime = True
    if current_number < 0:
        print(f"Number is negative.")
        command_n = input()
    else:
        for i in range(2, current_number):
            if current_number % i == 0:
                isPrime = False
                break
        if isPrime:
            sum_prime += current_number
        else:
            non_sum_prime += current_number
        command_n = input()
    
    
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {non_sum_prime}")