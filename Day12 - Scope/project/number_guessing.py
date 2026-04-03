import random

number = None

def calc(lives):
    global number
    while(lives!=0):
        print(f"you have {lives} to guess the number.")
        guess = int(input("make a guess: "))

        if(guess < number):
            print("too low!")
        elif(guess > number):
            print("too high!")
        else:
            return True

        lives-=1
    return False

def is_easy():
    return calc(10)

def is_medium():
    return calc(5)

def is_hard():
    return calc(3)

def main():
    global number
    number = random.randint(1, 100)
    print("welcome to number guessing game")
    print("the number ranges between 1 and 100")
    choice = input("choose a difficulty. type 'easy', 'medium' or 'hard': ")
    if(choice == 'hard'):
        ans = is_hard()
    elif(choice == 'easy'):
        ans = is_easy()
    elif(choice == 'medium'):
        ans = is_medium()

    if(ans):
        print("Congrats, you guessed the right number!")
    else:
        print("You lose, the correct number is", number)

if __name__ == "__main__":
    main()