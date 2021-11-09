import random

def play() :
    user = input("Whats your choice 'r' for rock, 'p' for paper , 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer :
        return 'tie'

    if is_win(user, computer) :
        return "You Won!"

    return "You Lose!"


def is_win(player, computer) : 

    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r') :
        return True

if __name__ == '__main__' :
    print(play())
