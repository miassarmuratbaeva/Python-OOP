class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre =genre
        self.duration = int(duration)
        self.rating = float(rating)
    def show_summary(self):
        print(f"{self.title} — {self.genre} janridagi film. Reyting: {self.rating}/10.")
movie1 = Movie("Inception", "fantastika", 148, 8.8)
movie2 = Movie("Titanic", "drama", 195, 9.0)
movie1.show_summary()
movie2.show_summary()