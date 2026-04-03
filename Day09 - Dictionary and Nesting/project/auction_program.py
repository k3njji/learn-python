print("welcome to auction")

save_list = []

while(True):
    name = input("what is your name? ")
    bid = int(input("what is your bid? "))

    dictionary = {
        'name': name,
        'bid': bid 
    }

    save_list.append(dictionary)
    boolean = input("are there any other bidders? type 'yes' or 'no': ")
    if(boolean == 'no'):
        break

biggest_bid = 0
save = 0

for i in range(len(save_list)):
    if(save_list[i]['bid'] > biggest_bid):
        biggest_bid = save_list[i]['bid']
        save = i

print(f"the winner is {save_list[i]['name']} with a bid of ${save_list[i]['bid']}")