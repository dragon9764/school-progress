import random
n = int(input("please enter a number: "))
bot = random.randint(1, n)
guesses = 1
while bot != n:
    bot = random.randint(1, n)
    guesses += 1
else:
    print(" ")
    print("program took", guesses, "guesses guess")
    percent = (1/n) * 100
    rpercent = round(percent, 2)
    print("with a", rpercent, "% chance per guess!")
