import random
actual_num = random.randint(1, 75)
print("G A M E   B E G I N S !!! \n")
print("""RULES OF THE GAME :
      # rule 1: Three chances will be given to player to guess the number. 
      # rule 2: The player will have 2 lifeline.
      # rule 3: 1 lifeline = 3 chances.
      # rule 4: once the lifeline used it cannot be regained.
      # rule 5: if player is unable to guess the correct number in given chances he/she will lose the game.
      # rule 6: further instruction will be given while playing the game.
""")

actual_num  # the randomly generated number
guess = int(input("guess a number between 1 to 75 :"))

count = 1
lifeline = 2
used_lifelines = 0

while True:
    if guess == actual_num:
        print("congratulations you guessed the number correctly in ", count, " attempt 🥳🥳 !!")
        print("chal ab party de 🥳🥳!!")
        break
    elif guess > actual_num:
        print(f"guess lower number than {guess}!")
    elif guess < actual_num:
        print(f"guess higher number than {guess}!")

    count += 1

    # When player has completed 3 attempts, offer lifeline
    if count == 4 and used_lifelines == 0:
        print("you have lost 3 chances !")
        ll = int(input("want to use lifeline ? (1 for yes and 0 for no) :"))
        if ll == 0:
            print("G A M E   O V E R")
            exit()
        elif ll == 1:
            lifeline -= 1
            used_lifelines += 1
            print(f"Now you have left with only {lifeline} lifeline !")
            print("3 additional chances are given to you !")
        else:
            print("invalid choice !")
            print("G A M E   O V E R")
            exit()

    # When player has completed 6 attempts, offer second lifeline
    elif count == 7 and used_lifelines == 1:
        print("again you have lost 3 chance ! ")
        print("you have lost total 6 chances !")
        ll_2 = int(input("want to use another lifeline ? (1 for yes and 0 for no) :"))

        if ll_2 == 0:
            print("G A M E   O V E R")
            exit()
        elif ll_2 == 1:
            lifeline -= 1
            used_lifelines += 1
            print(f"Now you have left with only {lifeline} lifeline !")
            print("2 additional chances are given to you !")
        else:
            print("invalid choice !")
            print("G A M E   O V E R")
            exit()

    elif count > 8:
        print("G A M E   O V E R \nBETTER LUCK NEXT TIME  😢 ")
        exit()

    # Ask again only if game is still going
    guess = int(input("try again :"))
