class movie:#creating a class 
    types="kids movies"#class instance
    def __init__ (self,name,genre,rating):
        self.name=name
        self.genre=genre
        self.rating=rating
mov1=movie("Despicable Me","comedy",7)
mov2=movie("Frozen","Family",9)
print("the movie's name is",mov1.name)
print("the movie's genre is",mov1.genre)
print("the movie's rating is",mov1.rating)

print("I am listing {}, the second movies name is {} an its genre is {} and i rate it a {}".format(mov2.types,mov2.name,mov2.genre,mov2.rating))
