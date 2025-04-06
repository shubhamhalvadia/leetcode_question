def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a','e','i','o','u']
        counter = 0
        curr_counter = counter
        for i in range(len(s[:k])):
            if s[i] in vowel:
                counter += 1

        curr_counter = counter

        for i in range(len(s) - k):
            if s[i] in vowel:
                curr_counter -= 1
            if s[k+i] in vowel:
                curr_counter += 1

            if curr_counter > counter:
                counter = curr_counter
        
        return counter
    