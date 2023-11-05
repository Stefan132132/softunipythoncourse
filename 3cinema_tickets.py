command_movie = input()
std_counter = 0
stud_counter = 0
kid_counter = 0
ticket_counter = 0
tickets = 0


while command_movie != "Finish":
    seats = int(input())
    ticket_category = input()
    while ticket_category != "End":
        ticket_counter += 1
        if ticket_category == "standard":
            std_counter += 1
        elif ticket_category == "kid":
            kid_counter += 1
        elif ticket_category == "student":
            stud_counter += 1
        if ticket_counter == seats:
            break
        ticket_category = input()
    print(f"{command_movie} - {((ticket_counter / seats) * 100):.2f}% full.")
    tickets = tickets + ticket_counter
    ticket_counter = 0
    command_movie = input()
    
print(f"Total tickets: {tickets}")
print(f"{((stud_counter / tickets)* 100):.2f}% student tickets.")
print(f"{((std_counter / tickets) * 100):.2f}% standard tickets.")
print(f"{((kid_counter / tickets) * 100):.2f}% kids tickets.")
            