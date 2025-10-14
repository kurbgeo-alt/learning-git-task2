import random
class Media:
    """Klasa bazowa dla filmów i seriali."""
    def __init__(self, title, year, genre, play_counter):
        self.title = title
        self.year = year
        self.genre = genre
        self.play_counter = play_counter = 0

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}"
    def play(self):
        self.play_counter += 1

    def generate_views(self):
        self.play_counter *= 10        


class Movie(Media):
    """Klasa reprezentująca film."""
    def __init__(self, title, year, genre, play_counter, duration):
        super().__init__(title, year, genre,play_counter)
        self.duration = duration  # Czas trwania w minutach

    def __str__(self):
        return super().__str__() + f", {self.duration} min"


class Series(Media):
    """Klasa reprezentująca serial."""
    def __init__(self, title, year, genre,play_counter, seasons):
        super().__init__(title, year, genre,play_counter)
        self.seasons = seasons  # Liczba sezonów

    def __str__(self):
        return super().__str__() + f", {self.seasons} sezonów"


class MediaLibrary:
    """Klasa zarządzająca biblioteką filmów i seriali."""
    def __init__(self):
        self.collection = []

    def add_media(self, media):
        """Dodaje film lub serial do kolekcji."""
        self.collection.append(media)
    def get_movies(self):
          return [i for i in self.library if type(i) == Movie]
    def get_series(self):
        return[i for i in self.library if type(i) == Series]
    def generate_views(self):
     k = random.choice(self.library)      
         



      

    def search_by_title(self, title):
        """Wyszukuje media po tytule."""
        results = [media for media in self.collection if title.lower() in media.title.lower()]
        return results
    
    


#


    def top_titles(self, n=5, content_type=None):
        """
        Zwraca najpopularniejsze tytuły na podstawie oceny.
        :param n: Liczba tytułów do zwrócenia
        :param content_type: Typ (film/serial) lub None dla obu
        :return: Lista najpopularniejszych tytułów
        """
        filtered = self.library
        if content_type:
            filtered = [item for item in self.library if item["content_type"] == content_type.lower()]
        
        # Sortowanie po ocenie malejąco
        sorted_titles = sorted(filtered, key=lambda x: x["rating"], reverse=True)
        return sorted_titles[:n]

 
# Przykład użycia
if __name__ == "__main__":
    library = MediaLibrary()

    # Dodawanie filmów i seriali
    library.add_media(Movie("Inception", 2010, "Sci-Fi",22, 148))
    library.add_media(Series("Breaking Bad", 2008, "Drama", 75, 155))
    library.add_media(Movie("The Matrix", 1999, "Sci-Fi",234, 136))
    library.add_media(Movie("James Bond",2021, "Action", 345,154))

    # Wyświetlanie wszystkich mediów
    print("Biblioteka filmów:")
    

    

    # Wyszukiwanie po tytule
    print("\nWyniki wyszukiwania dla 'James Bond':")
    results = library.search_by_title("James Bond")
    for media in results:
        print(media)
    print("Najpopularniejsze filmy i seriale dnia {data}")    
    print("Top 3 filmy:") 
    for title in library.top_titles(3, content_type="film"):
        print(f"{title['title']} ({title['year']}) - Ocena: {title['rating']}")

    print("\nTop 2 seriale:")

    for title in library.top_titles(2, content_type="serial"):
        print(f"{title['title']} ({title['year']}) - Ocena: {title['rating']}")