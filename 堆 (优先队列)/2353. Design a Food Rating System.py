class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        import heapq
        self.D = {}
        self.food = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.D:
                self.D[cuisine] = []
            heapq.heappush(self.D[cuisine], (-rating, food))
            self.food[food] = [cuisine, rating]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food[food]
        heapq.heappush(self.D[cuisine], (-newRating, food))
        self.food[food][1] = newRating

    def highestRated(self, cuisine: str) -> str:
        # print(cuisine, self.D)
        while True:
            rating, name = self.D[cuisine][0]
            # print(name, rating, self.food[name][1])
            if self.food[name][1] == -rating:
                return name
            else:
                heapq.heappop(self.D[cuisine])

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
