class User:
    # initialise attribute
    def __init__(self, seats, username):
        print("new user being created...")
        # the seats parameter tells us that we can set something into the attribute
        self.id = seats
        self.username = username
        self.followers = 0
        self.following = 0

    def say_hi(self):
        print("hii i am", self.username)
        return
    
    def add_follower(self):
        self.followers+=1

    def add_following(self):
        self.following+=1
    

user_1 = User(1, 'kenzie')
user_2 = User(2, 'mm')
print(user_1.id)
print(user_1.username)
# this is different
print(user_1.say_hi)
user_1.add_follower()
print(user_1.followers)
user_1.add_follower()
print(user_1.followers)
# with this one
user_1.say_hi()

# print(user_2.followers)

# to add attribute outside class
# user_1.id = '001'
# user_1.username = 'angela'
# print(user_1)

#but if we use this, it is a bit of a hassle to 