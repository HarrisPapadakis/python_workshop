class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Όνομα εστιατορίου: {self.restaurant_name}")
        print(f"Τύπος κουζίνας: {self.cuisine_type}")

    def open_restaurant(self):
        print("Το εστιατόριο είναι ανοιχτό!")


# Δημιουργία στιγμιότυπου της κλάσης
restaurant = Restaurant("Αθηναϊκή Γεύση", "Ελληνική")

# Εμφάνιση ιδιοτήτων
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Κλήση μεθόδων
restaurant.describe_restaurant()
restaurant.open_restaurant()
