class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.reviews.append(self)
        customer.reviews.append(self)
        restaurant.reviews.append(self)

    def rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant