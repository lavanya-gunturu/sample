import random

def play():
    user = input(" 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

if user == computer:
    return 'tie'

#r>s, s>p, p>r
if is_win(user, computer):
    return 'won';

    if is_win(computer, user):
        return 'lost';

    
