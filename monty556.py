import random
class Media:
    """Klasa bazowa dla filmów i seriali."""
    def __init__(self, title, year, genre, play_counter = 0):
        self.title = title
        self.year = year
        self.genre = genre
        self.play_counter = play_counter

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}"
    def play(self):
        self.play_counter += 1

    def generate_views(self):
        self.play_counter += random.randint(1,100)       


class Movie(Media):
    """Klasa reprezentująca film."""
    def __init__(self, title, year, genre, play_counter):
        super().__init__(title, year, genre,play_counter)
        self.title = title
        self.year = year
        self.genre = genre
        self.play_counter = play_counter
        

    


class Series(Media):
    """Klasa reprezentująca serial."""
    def __init__(self, title, year, genre,play_counter, seasons,episodes,):
        self.title = title
        self.year = year
        self.genre = genre
        self.play_counter = play_counter
        self.seasons = seasons  # Liczba sezonów
        self.episodes = episodes # Liczba odcinków
        

    def __str__(self):
        return super().__str__() + f", S{self.season:02}E {self.episode:02}"
    

class MediaLibrary:
    """Klasa zarządzająca biblioteką filmów i seriali."""
    def __init__(self):
        self.collection = []

    def add_media(self, media):
        """Dodaje film lub serial do kolekcji."""
        self.collection.append(media)
    def get_movies(self):
          return [i for i in self.collection if type(i) == Movie]
    def get_series(self):
        
        return[i for i in self.collection if type(i) == Series]
    def generate_views(self):
        media= random.choice(self.collection)
        media.play_counter +=random.randit(1,100)
        
        
    def run_views_generation(self, times =10) :
        for _ in range(times):
            self.generate_views()
        
         
         



      

    def search_by_title(self, title):
        """Wyszukuje media po tytule."""
        results = [media for media in self.collection if title.lower() in media.title.lower()]
        return results
    
    


#


    def top_titles(self, n=5, content_type =None):
        """
        Zwraca najpopularniejsze tytuły na podstawie oceny.
        :param n: Liczba tytułów do zwrócenia
        :param content_type: Typ (film/serial) lub None dla obu
        :return: Lista najpopularniejszych tytułów
        """
        
        if content_type == "Movie": 
         filtered = [item for item in self.collection if isinstance(item, Movie)]
        elif content_type == "Series":
            filtered = [item for item in self.collection if isinstance(item,Series)]

 

 
# Przykład użycia
if __name__ == "__main__":
    library = MediaLibrary()

    # Dodawanie filmów i seriali
    library.add_media(Movie("Inception", 2010, "Sci-Fi",217))
    library.add_media(Series("Breaking Bad", 2008, "Drama",345, 15, 155))
    library.add_media(Movie("The Matrix", 1999, "Sci-Fi", 136))
    library.add_media(Movie("James Bond",2021, "Action",154))

    # Wyświetlanie wszystkich mediów
    print("Biblioteka filmów:")
    

    

    # Wyszukiwanie po tytule
    print("\nWyniki wyszukiwania dla 'James Bond':")
    results = library.search_by_title("James Bond")
    for media in results:
        print(media)
        print("Najpopularniejsze filmy i seriale dnia {data}")    
        print("Top 3 filmy:")    
    for media in library.top_titles(3, "Movie"):
        print(f"{media.title} ({media.year}) - Odtworzenia: {media.play_counter}")
    for media in library.top_titles(2, "Series"):
        print(f"{media.title} {media.year} - Odtworzenia: {media.play_counter}")
if __name__ == "__main__":
    library = MediaLibrary()
    
    
  
  