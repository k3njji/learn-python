from random_word import RandomWords

r = RandomWords()
word = r.get_random_word()

lives = 10

guessed_char_false = []
guessed_char_right = []

while(lives != 0):

    print(f"you have {lives} lives left")
    count = 0
    print("word to guess:", end=" ")
    for i in word:
        found = False
        for j in guessed_char_right:
            if j == i:
                print(i, end="")
                found = True
                count = count+1
                break
        if not found:
            print("_", end="")
    
    if(count == len(word)):
        print("congrats! you have won")
        break

    print("")
            
    guess = input("guess the letter: ").lower()

    if guess not in word:
        guessed_char_false.append(guess)
        print(f"you guessed {guess}, thats not in the word")
        lives -= 1
    else:
        guessed_char_right.append(guess)

if(lives <= 0):
    print(f"you lose, the word is {word}")