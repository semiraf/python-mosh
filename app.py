import random
secret_number = (random.randint(1, 10))

while:
    user_guess = int(input('Guess: '))

    if user_guess == secret_number:
        print("You win!")

    elif user_guess <= secret_number:
        print("Higher!")

    elif user_guess >= secret_number:
        print("Lower!")
