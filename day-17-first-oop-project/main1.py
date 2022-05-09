class User:

    def __init__(self, user_id, username):  # parameters
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # self.attribute = value (or parameters)  !!!

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")  # initializing attributes by passing values
user_2 = User("002", "jack")

print(user_1.username + " - " + user_1.id + " - " + str(user_1.followers))

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)