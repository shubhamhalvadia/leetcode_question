def equalPairs(self, grid: List[List[int]]) -> int:
        transposed = [list(row) for row in zip(*grid)]
        freq = {}
        count = 0
        for r in grid:
            freq[tuple(r)] = freq.get(tuple(r), 0) + 1
        values = freq.values()
        
        print(freq.items())
        for c in transposed:
            if freq.get(tuple(c)):
                count += freq.get(tuple(c))
        
        print(freq.items())
        return count