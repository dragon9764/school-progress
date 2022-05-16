C_Username = "O5-2"
C_Password = "password"
guess = " "
guess_count = 0
guess_limit = 3
limit = 3
out_of_guesses = False

while guess != C_Username and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter username: ")
        guess_count += 1
        limit -= 1
    else:
        out_of_guesses = True
    if guess != C_Username and limit > 0:
        print("Username not in database.", limit, "Attempt(s) left.")
    else:
        print("")

guess = " "
guess_count = 0
guess_limit = 3
limit = 3

while guess != C_Password and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter Password: ")
        guess_count += 1
        limit -= 1
    else:
        out_of_guesses = True
    if guess != C_Password and limit > 0:
        print("Incorrect password.", limit, "Attempts left.")
    else:
        print("")

if out_of_guesses:
    print("Security lockdown protacol active. shutting down...")
else:
    print("Welcome,", C_Username)
