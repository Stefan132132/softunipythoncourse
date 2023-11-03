symbol = input()
word = ""
new_word = ""
counter_letters = 0
isCKnown = True
isOKnown = True
isNKnown = True

while symbol != "End":
    if symbol.isalpha():
        if symbol == "c":
            if isCKnown:
                counter_letters += 1
                isCKnown = False
            elif isCKnown == False:
                word = word + "c"
        elif symbol == "o":
            if isOKnown:
                counter_letters += 1
                isOKnown = False
            elif isOKnown == False:
                word = word + "o"
        elif symbol == "n":
            if isNKnown:
                counter_letters += 1
                isNKnown = False
            elif isNKnown == False:
                word = word + "n"
        else:
            word = word + symbol

        if counter_letters == 3:
            isCKnown = True
            isOKnown = True
            isNKnown = True
            counter_letters = 0
            word = word + " "
            new_word = new_word + word
            word = ""
        symbol = input()
    else:
        word = word + ""
        symbol = input()
    
    

if symbol == "End":
    print(new_word)