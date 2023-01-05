import random

def guess(x):  # Defining a function
    random_number = random.randint (1, x)
    guess = 0  # To initialize and tell the coputer that this number exists, but it is not in the range between 1 and x.
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))  # Notice one space after x
        if guess < random_number:
            print('Sorry! guess again, too low.')
        elif guess > random_number:  
            print('Sorry, guess again, too high.')
# One empty line here
    print(f'Congrats, you have guessed the number {random_number}')
# One empty line here
guess(10)