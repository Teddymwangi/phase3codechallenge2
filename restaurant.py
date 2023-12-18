class Restaurant:
    restaurants = []

    def __init__(self, name):
        self._name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls.restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        reviewers = [review.customer() for review in self.reviews]
        return list(set(reviewers))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating() for review in self.reviews)
        return total_ratings / len(self.reviews)