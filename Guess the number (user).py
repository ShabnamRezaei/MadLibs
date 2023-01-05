import random

def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: # otherwise (low = high)
            guess = low  # Can also be high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?') . lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Congrats, the computer have guessed the number correctly {guess}')

guess(100)

