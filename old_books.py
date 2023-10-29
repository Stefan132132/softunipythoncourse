searched_book = input()
book = input()
counter = 0

while True:
    if searched_book == book:
        print(f"You checked {counter} books and found it.")
        break
    elif book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    else:
        counter += 1
        book = input()


        