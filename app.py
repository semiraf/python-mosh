import random
secret_number = (random.randint(1, 10))
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_guess = int(input('Guess: '))
    guess_count += 1

    if user_guess == secret_number:
        print("You win!")

    elif user_guess <= secret_number:
        print("Higher!")

    elif user_guess >= secret_number:
        print("Lower!")
        
    elif guess_limit == guess_limit:
        print('You lose!')