class Art:
    def __init__(self, artist, title, year, medium):
        self.artist = artist
        self.title = title
        self.year = year
        self.medium = medium

    def __repr__(self):
        return self.artist + "," + self.title + "," + self.year + "," + self.medium


girl_with_mandolin = Art('Picasso, Pablo','Girl with a Mandolin (Fanny Tellier)','1910','oil in canvas')

print(girl_with_mandolin)