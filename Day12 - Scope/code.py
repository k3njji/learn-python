#local and global variabel
enemies = 1

#consts variabel pake all caps
PI = 3.14


def increase_enemies():
    enemiese = 2
    #to call global scope
    global enemies
    enemies = 3
    print(f"enemes inside func", enemiese)

increase_enemies()
print("enemies outside of the function", enemies)

print(PI)

