# catching error

# file not found
try:
    file = open("Day30 - JSON & Catching Error/a_file.txt")
    a_dict = {'key': 'value'}
    # ini pasti error
    # print(a_dict['something'])
except FileNotFoundError:
    # we can use this as an alternative so it can giev options
    file = open('Day30 - JSON & Catching Error/a_file.txt', 'w')
    file.write('write something')
    print("there is an error")
except KeyError as error_message:
    # we can use this to debug as well
    print(f'key {error_message} doomed')
else:
    # this will run if the whole try section have no error
    content = file.read()
    print(content)
finally:
    # this finally will run no matter what
    file.close()
    # raise TypeError('this is an error that i made up')

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except:
        print('Fruit pie')
    # finally:
    #     # fruit = fruits[index%len(fruits)]
    #     print(fruit + " pie")

make_pie(0)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except:
            continue
    
    return total_likes


count_likes(facebook_posts)

