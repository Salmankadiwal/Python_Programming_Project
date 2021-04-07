import random

round = 1
user_chance = 0
comp_chance = 0

choose_from = ['g','w','s']

print("=======Snack-gun-Water Game=========")
print()

print("Snake - 's'\nGun - 'g'\nWater - 'w'\n")

is_valid = True
while(is_valid):
    try:
        n = None
        n = int(input("Enter Number of rounds?\n"))
    except Exception as e:
        print(e)

    if type(n) != int:
        print("Invalid datatype..try again..")
        continue
    else:
        is_valid=False



while round<=n:

    print(f"Here begins the round {round}")

    computer = random.choice(choose_from)

    try:
        player = input("Choose your Option : (g) for gun,(w) for water and (s) for snake : ")[0]
    except ValueError as e:
        print(e)


    if player !='w' and player !='s' and player !='g':
        print("Invalid output try again\n")
        continue

    if computer == 's':
        if player == 'w':
            comp_chance +=1
        elif player == 'g':
            user_chance +=1

    elif computer == 'w':
        if player == 'g':
            comp_chance +=1
        elif player == 's':
            user_chance +=1

    elif computer == 'g':
        if player == 's':
            comp_chance +=1
        elif player == 'w':
            user_chance +=1


    if user_chance > comp_chance:
        print(f"You won round {round}\n")
    elif user_chance < comp_chance:
        print(f"Comp won round {round}\n")
    else:
        print("Draw...!!!\n")


    round +=1


print("Final Winner on the number of wons is :\n")
if user_chance > comp_chance:
    print("Congragualtions! you Won")
elif user_chance < comp_chance:
    print("Hard luck!!you lost the game")
else:
    print("Match Draw...!!!")






