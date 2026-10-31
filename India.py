class India():
    def capital(self):
        print("New Delhi is the Capital of India")

    def language(self):
        print("Hindi is the Most Spoken Language of India")

    def type(self):
        print("India is a Developing Country")

class America():
    def capital(self):
        print("Washington D.C is the Capital of America")

    def language(self):
        print("English is the Most Spoken Language of America")

    def type(self):
        print("America is a Developed Country")

obj_ind=India()
obj_ame=America()

for country in (obj_ind, obj_ame):
    country.capital()
    country.language()
    country.type()