#task 1#
import random
num1 = random.randint(1, 6)  # 1 to 6 like a dice
num2 = random.randint(1, 6)
print(num1, "+", num2)  # shows both rolls
print("total: ", num1 + num2)  # adds them up incase needed
#task 2#
num3 = random.randint(1, 2)
if num3 == 1:  # if num3 is 1
    print("Heads")
else:  # as it is 1 or 2 then else means anything other than 1 (meaning only 2)
    print("Tails")
#task 3#
# generates a constant intager number from 1 to 100
number = random.randint(1, 100)
guess = (int(input("guess a number from 1 to 100: ")))  # person's guess input
guess_count = 1
while guess != number:  # wont stop untill person's guess is the same as the number
    print("guess was inccorect")
    print(" ")  # prints nothing just to look better
    guess = (int(input("guess a number from 1 to 100: ")))
    guess_count += 1  # guess counter goes up by 1 per guess
else:  # once the number is guessed
    print(number, "was the number")  # prints what the number was
    print("total guesses: ", guess_count)
