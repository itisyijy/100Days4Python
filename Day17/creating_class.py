# Day17 for 100Days4Python
# Day17 : Creating Own Class

# PascalCase    : ClassName
# camelCase     : notForPython
# snake_case    : otherName

class User: # declare class
    # Constructor specifies what should happen when object is constructed : initialize object!
    def __init__(self, user_id, username):  # self : initialized actual object
        print("initializing object")
        
        # initialize attributes which are variables associated with object
        self.user_id = user_id  # parameter : getting data for initializing attributes
        self.username = username
        self.followers = 0      # setting default value
        self.following = 0
    
    # declare method
    def follow(self, user):   # 'self' is mandatory
        print(f"{self.username} follows {user.username}")
        self.following += 1
        user.followers += 1

    def unfollow(self, user):   # 'self' points the object itself
        print(f"{self.username} unfollows {user.username}")
        if self.following > 0 and user.followers > 0:
            self.following -= 1
            user.followers -= 1

    pass    # continue to next code line without error

user_1 = User("00", "Micky")        # making object based on class
print(user_1.user_id, user_1.username)
user_1.user_id = "37"           # making or modify attributes of object one by one.
print(user_1.user_id, user_1.username)
print("-------------------------------------------")
user_2 = User("21", "Dejan")
print(user_2.user_id, user_2.username)

print("-------------------------------------------")

user_1.follow(user_2)
print(f"{user_1.username} follwers : {user_1.followers}, following : {user_1.following}")
print(f"{user_2.username} follwers : {user_2.followers}, following : {user_2.following}")
print("-------------------------------------------")
user_1.unfollow(user_2)
print(f"{user_1.username} follwers : {user_1.followers}, following : {user_1.following}")
print(f"{user_2.username} follwers : {user_2.followers}, following : {user_2.following}")