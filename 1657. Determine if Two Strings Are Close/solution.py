def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = {}
        freq2 = {}
        for w1, w2 in zip(word1, word2):
            freq1[w1] = freq1.get(w1, 0) + 1
            freq2[w2] = freq2.get(w2, 0) + 1
        
        return (sorted(freq1.values()) == sorted(freq2.values())) and (sorted(freq1.keys()) == sorted(freq2.keys()))