class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_time_to_read(self):
        pass

class Book(Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

    def get_time_to_read(self):
        return self.pages * 4 / 60
    
class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator

    def get_time_to_read(self):
        return self.duration_in_hours
    
audiobook = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Hořák")
book = Book("Kadet Hornblower", 399, 242)

total_time = audiobook.get_time_to_read() + book.get_time_to_read()

print(f"celkový čas na užívání produktů je {total_time} hodin.")
