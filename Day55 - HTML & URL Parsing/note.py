class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
    
def is_authenticated(func):
    def wrapper(user):
        if user.name == "Alice":
            return func(user)
        else:
            return "User is not authenticated."
    return wrapper

def create_blog_post(user):
    return f"<h1>{user.name}'s Blog Post</h1><p>This is the newest blog post.</p>"

new_user = User("Alice")
print(new_user.greet())
create_blog_post(new_user)