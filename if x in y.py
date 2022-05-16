#if x in y#
passlist = ["pass", "password"]  # list
guess = input("enter password: ")  # input
if guess in passlist:  # if person's guess is in the list
    print("correct")
else:  # if person's guess isnt in the list
    print("incorrect")
