import random

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]

print("🕹️ Let's play a game of Rock Paper Scissors. 🕹️")
print("0 - Rock")
print("1 - Paper")
print("2 - Scissors")
user_index = int(input("Your choice: "))
index = random.randint(0, 2)

print("You Choose")
print(rps[user_index])

print("Computer Choose")
print(rps[index])

if(index == user_index):
    print("Draw!")
elif((index == 0 and user_index == 1) or (index == 1 and user_index == 2) or (index == 2 and user_index == 0)):
    print("YOU Win!")
else:
    print("COMPUTER Lose!")