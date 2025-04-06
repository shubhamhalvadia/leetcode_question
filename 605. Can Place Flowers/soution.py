def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
        
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            n -= 1
            flowerbed[0] = 1

        for i in range(2, len(flowerbed)-2):
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                n -= 1
                flowerbed[i] = 1
        if n <= 0:
            return True
        else:
            return False