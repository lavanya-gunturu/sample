import random

def play():
    user = input("what is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n" )
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'ITS A TIE'

    #r>s, s>p, p>r
    if is_win(user, computer):
        return 'YOU WON!!!'

    return 'YOU LOST :('

def is_win(player, opponent):
    #return true if player wins
    #r>s, s>p, p>r
    if (player =='r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 'r'):
        return True

print(play())