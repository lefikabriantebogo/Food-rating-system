import heapq
from collections import defaultdict


class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        # Map food -> (cuisine, rating)
        self.food_info = {}
        # Map cuisine -> max heap of (-rating, food)
        self.cuisine_heap = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = [cuisine, rating]
            # Use negative rating for max-heap
            heapq.heappush(self.cuisine_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        # Push the new rating onto the heap
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_heap[cuisine]
        # Pop elements that are outdated
        while True:
            rating, food = heap[0]
            current_rating = self.food_info[food][1]
            if -rating == current_rating:
                return food
            heapq.heappop(heap)


