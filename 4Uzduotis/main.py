# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.


class Movie:
    def __init__(self,title,director,budget):
        self.title = title
        self.director = director
        self.budget = budget
    def was_expensive(self):
        return self.budget > 100000000


titanikas = Movie("Titanikas","Arnolas Svarcgeneris",1000000)
print(titanikas.was_expensive())
    