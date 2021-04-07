import random

randn = random.randint(1,80)

name = input("Please May I know your name?")

valid = True

while valid:
    guess = None
    try:

        guess = int(input("Please guess a number between 1 and 80 : "))
        if type(guess) == int:
            break

    except Exception:
        try:

            guess = int(input("Please input the correct datatype "))

        except Exception:
            if type(guess) != int:
                continue

count = 1

if randn == guess:
    print("Good job!",name,"You Guessed the number in "+ str(count)+" guess")


while randn != guess:
    count = count + 1
    if guess < randn:
        print("Hard luck,You need to guess again,Hint: go higher")

    else:
        print("Hard luck,You need to guess again,Hint: go lower")
    print()
    guess = int(input("\nPlease guess a number again between 1 and 80 : "))


print(name,"you guessed the number "+str(guess)+" with "+str(count)+" chances")