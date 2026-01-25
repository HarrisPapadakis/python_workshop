class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Όνομα εστιατορίου: {self.restaurant_name}")
        print(f"Τύπος κουζίνας: {self.cuisine_type}")
        print()  # κενή γραμμή για καλύτερη εμφάνιση


# Δημιουργία τριών διαφορετικών στιγμιότυπων
restaurant1 = Restaurant("Αθηναϊκή Γεύση", "Ελληνική")
restaurant2 = Restaurant("Pasta House", "Ιταλική")
restaurant3 = Restaurant("Sushi Zen", "Ιαπωνική")

# Κλήση της describe_restaurant() για κάθε στιγμιότυπο
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
