import random

def computer_guess(x) :
    low = 1
    high = x
    feedback = ''
    trials = 0
    while feedback != 'C' :
        trials +=1
        if low != high :
            guess = random.randint(low,high)
        else :
            guess = low
        feedback = input(f'Is {guess} too high (H) or too low (L) or correct (C)  : ')
        if feedback == 'H' :
            high = guess
        elif feedback == 'L' :
            low = guess

    print(f'Cool! I am able to guess the number {guess} in {trials} trials')

if __name__ == '__main__' :
    x = int(input('Set the high limit : '))
    computer_guess(x)

