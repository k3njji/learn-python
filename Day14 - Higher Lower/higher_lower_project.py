import data
import random
import art

print("welcome to higher or lower")
datas = data.data
prev = random.randint(0, 50)
score = 0

while(True):
    next = random.randint(0, 50)
    print(art.logo)
    if(score!=0):
        print("You are right! Current score: ", score)
    print(f"Compare A: {datas[prev]['name']}, a {datas[prev]['description']}, from {datas[prev]['country']}")
    print(art.vs)
    print(f"Compare B: {datas[next]['name']}, a {datas[next]['description']}, from {datas[next]['country']}")

    choice = input("who has more followers? Type 'A' or 'B': ")

    if(choice == 'A'):
        if(datas[prev]['follower_count'] >= datas[next]['follower_count']):
            score+=1
        else:
            break
    elif(choice == 'B'):
        if(datas[prev]['follower_count'] <= datas[next]['follower_count']):
            score+=1
        else:
            break
    prev = next
print("You just lost")