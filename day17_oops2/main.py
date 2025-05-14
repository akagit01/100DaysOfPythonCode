class User:
    #this is a constructor
    def __init__(self,userid,username):
        self.id=userid
        self.name=username
        self.followers=0
        self.following=0

        #this is a method
    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=User("001","Aakash")
print(user1.id,user1.name)

user2=User("002","Kaka")
user3=User("003","Baba")

user1.follow(user2)
print(user1.following)
print(user2.followers)

