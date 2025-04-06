def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        result = []
        result=[False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_value:
                result[i] = True
        return result