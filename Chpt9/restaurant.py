class Restaurant: 

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type
        self.number_served=0 #default value for an attribute

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that offers {self.cuisine_type} type of cuisine!")
    
    def open_restaurant(self):
        print("Restaurant is now open.")

    def set_number_served(self, num):
        self.number_served= num

    def increment_number_served(self, num):
        self.number_served+=num
        
    
restaurant= Restaurant("Oporto", "Portuguese")
print(f"Name of the restaurant is: {restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type} food is offerent at this restaurant.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} people")
restaurant.set_number_served(10)
print(f"{restaurant.restaurant_name} has now served {restaurant.number_served} people")
restaurant.increment_number_served(2)
print(f"{restaurant.restaurant_name} has now served {restaurant.number_served} people")
