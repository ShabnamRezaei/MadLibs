import random

def guess(x):
    low = 1  # The = is a simple assignment operator. It assigns values from right side operands to the left side operand.
    high = x  # The == checks if the values of two operands are equal or not. If yes, the condition becomes true and it returns a non zero value.
    feedback = ''  # Initializing and telling the coputer that the feedback exists but not giving any 'c', 'h' or 'l' 
    while feedback != 'c':
        if low != high:  # != (if not)
            guess = random.randint(low, high)
        else:  # otherwise (low = high)
            guess = low  # Can also be high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?') . lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer have guessed the number correctly {guess}')

guess(100)

