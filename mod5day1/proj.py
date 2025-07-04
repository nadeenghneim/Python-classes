class dogs:
    type="pet friendly"
    def __init__(self,breed,size):
        self.breed=breed
        self.size=size
dog1=dogs("Golden Retriever","30kg")
dog2=dogs("Husky","20kg")
print("we will be talking about dogs who are",dog1.type)
print("the first type of dog is a ",dog1.breed,"and its average size is around",dog1.size)
print("the second type of dog is a ",dog2.breed,"and its average size is around",dog2.size)