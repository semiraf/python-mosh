import random
secret_number = (random.randint(1, 10))
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_guess = int(input('Guess: '))

    if user_guess == secret_number:
        print("You win!")

    elif user_guess <= secret_number:
        print("Higher!")

    elif user_guess >= secret_number:
        print("Lower!")
