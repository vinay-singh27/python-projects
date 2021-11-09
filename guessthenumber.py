import random

def guess(x) :
    rand_num = random.randint(1,x)
    guess = 0
    trials = 0
    while guess != rand_num :
        guess = int(input(f"Guess a number between 1 & {x} : "))
        trials +=1
        if guess < rand_num :
            print("Sorry, guess again. Too Low ")
        elif guess > rand_num :
            print("Sorry, guess again. Too High")

    print(f"Yay! You have guess the number {rand_num} in {trials} trials")

if __name__ == '__main__' :
    x = int(input("Set the upper limit : "))
    guess(x)
