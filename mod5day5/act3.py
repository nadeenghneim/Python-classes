class Palestine:
    def capital(self):
        print("Jerusalem is the capital of Palestine")
    def language(self):
        print("Arabic is the common language in Palestine")
    def type(self):
        print("Palestine is a developing country")

class Jordan:
    def capital(self):
        print("Amman is the capital of Jordan")
    def language(self):
        print("Arabic is the common language in Jordan")
    def type(self):
        print("Jordan is a developing country")
p=Palestine()
j=Jordan()
for country in (p,j):
    country.capital()
    country.language()
    country.type()