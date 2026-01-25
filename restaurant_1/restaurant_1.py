class Restaurant:
    """
    A class that represents a restaurant.

    Attributes:
        restaurant_name (str): The name of the restaurant.
        cuisine_type (str): The type of cuisine the restaurant serves.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant with a name and a cuisine type.

        Args:
            restaurant_name (str): The name of the restaurant.
            cuisine_type (str): The type of cuisine.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        Print the restaurant's name and cuisine type.
        """
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print()  # Blank line for better readability


# Create three different instances of the Restaurant class
restaurant1 = Restaurant("Athens Taste", "Greek")
restaurant2 = Restaurant("Pasta House", "Italian")
restaurant3 = Restaurant("Sushi Zen", "Japanese")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
