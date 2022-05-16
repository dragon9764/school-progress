while True:
    n = input("enter a number between 1 and 10: ")  # request any input
    try:  # attempts to use it in command below
        n = int(n)  # confirming its an intager
        if n <= 10 and n >= 1:  # custom peramiters (not needed)
            print("you chose:", n)  # result if it matches
            break  # ends sequence
        else:  # if its not inside peramiters (not needed)
            print("this number is outside the range set. Please try again")
    except ValueError:  # if it isnt an intager
        print("invalid input, please try again")

#without comments#

while True:
    n = input("enter a number between 1 and 10: ")
    try:
        n = int(n)
        if n <= 10 and n >= 1:
            print("you chose:", n)
            break
        else:
            print("this number is outside the range set. Please try again")
    except ValueError:
        print("invalid input, please try again")
