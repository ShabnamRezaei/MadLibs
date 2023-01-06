import random 

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer: 
        return 'It\'s a tie'  # It's returns error, needs to add a backslash
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    # if is_win(computer, user): is default 
    return 'You lost!'

def is_win(player, opponent):
# Return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

