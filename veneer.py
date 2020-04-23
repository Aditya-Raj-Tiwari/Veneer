class Art:
    def __init__(self, artist, title, year, medium,owner):
        self.artist = artist
        self.title = title
        self.year = year
        self.medium = medium
        self.owner = owner
    def __repr__(self):
        return '%s. "%s". %s. "%s". "%s" , "%s". ' % (self.artist, self.title, self.year, self.medium,self.owner.name,self.owner.location)

class Marketplace:
    def __init__(self):
        self.listings = []
    def add_listing(self,new_listing):
        self.listings.append(new_listing)
    def remove_listings(self,expired_listing):
        self.listings.remove(expired_listing)
    def show_listings(self):
        for items in self.listings:
            print(items)

class Client:
    def __init__(self,name,location,is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum







vaneer = Marketplace()
print(vaneer.show_listings())

edytta = Client("Edytta Halpirt","Private Collection", is_museum=False)
moma = Client("The MOMA", "New York", is_museum=True)

girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', '1910', 'oil in canvas',moma)
print(girl_with_mandolin)

