class movie:

    def __init__ (self,name,genre,rating):
        self.name=name
        self.genre=genre
        self.rating=rating
mov1=movie("Despicable Me","comedy",7)
print("the movie's name is",mov1.name)
print("the movie's genre is",mov1.genre)
print("the movie's rating is",mov1.rating)