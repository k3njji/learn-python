print("welcome to treasure island!\nyour mission is to find the treasure")

direction = input("do you want to go left or right? ")

if(direction == 'left'):
    print("passed stage 1")
    swim = input("do you want to swim or not? (y for yes): ")
    if(swim == 'y' or swim == 'yes'):
        print("passed stage 2")
        door = input("we have 3 colored doors (blue, red, yellow), pick one: ")
        if(door == 'yellow'):
            print("you win!")
        elif(door == 'blue'):
            print("got beat up, you lose")
        elif(door == 'red'):
            print("burned by fire, you lose")
    else:
        print("attacked by trout, you lose")
else:
    print("fell into a hole, you lose")

print("game over!")