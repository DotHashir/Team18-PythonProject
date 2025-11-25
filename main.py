import random


score = 0
attempts = 0
choice = 1

while choice:

  number = random.randint(1, 50)

  while True:

    guess = int(input("Guess a number between 1 and 50: "))
    attempts +=1

    if number == guess:

      print("Correct!")

      score +=1

      print(f"Your score = {score}")

      break

    else:

      if guess > number:

        print("Too high")

      else:

        print("Too low")

  while True:
    print("Number of attemots: ")
    print (attempts)
    choice = int(input("Input 1 if you want to play again or 0 if you want to exit: "))

    if choice == 0 or choice == 1:
        break

    else:

      print("You input the wrong number")