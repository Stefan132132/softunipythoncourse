M = int(input())
pass_counter = 0
password = 0
foundPass = False

for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:
                        if a*b + c*d == M:
                            pass_counter += 1
                            print(f"{a}{b}{c}{d}", end= " ")
                            if pass_counter == 4:
                                password = a * 1000 + b * 100 + c * 10 + d
                                foundPass = True
if foundPass:
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")